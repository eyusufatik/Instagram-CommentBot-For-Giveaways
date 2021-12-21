from pynput import keyboard
from pynput.mouse import Button, Controller as mController
from pynput.keyboard import Key, Controller as kController
from threading import Lock
from threading import Thread
import time 
import random
import os

#####BELOW ARE THE THINGS YOU SHOULD MODIFY
ACC_NUM_FOR_COMMENT = [2,3]  #ARRAY OF HOW MANY ACCOUNTS ARE REQUIERED IN A COMMENT FOR EACH GIVEAWAY
COMMENT_PREFIXES = ["",""]   #ARRAY TO BE FILLED IF GIVEAWAYS NEED HASHTAGS OR STUFF IN COMMENTS
CHANGE_BROWSER_TAB_MODIFIER_KEY = Key.cmd #Key.crtl for windows etc.
NUMBER_OF_GIVEAWAYS = 2 
#####ABOVE ARE THE THINGS YOU SHOULD MODIFY

last_key = ""
mutex = Lock()
my_mouse = mController()
my_keyboard = kController()
work = False
index = 0
current_giveaway = 1

def type_with_speed(string, t):
    wait_time = t/len(string)
    for s in string:
        my_keyboard.press(s)
        time.sleep(wait_time)

def change_tabs(tab_num):
    with my_keyboard.pressed(CHANGE_BROWSER_TAB_MODIFIER_KEY):
        time.sleep(0.5)
        my_keyboard.press(str(tab_num))
        time.sleep(0.5)
        my_keyboard.release(str(tab_num))
    time.sleep(1)
    my_mouse.press(Button.left)
    time.sleep(0.5)

def send_comment():
    my_keyboard.press(Key.enter)
    time.sleep(5)
    my_mouse.press(Button.left)

def on_press(key):
    global last_key
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        mutex.acquire()
        last_key = key.char
        mutex.release()
        if(key.char == "ü"):
            os._exit(1)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

names_file = open("names.txt", "r")
names = ""
for name in names_file:
    names += name
names = names.split("\n")
random.shuffle(names)

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

while True:
    if work:
        time.sleep(0.1)
        change_tabs(current_giveaway)
        accs = names[index:index+ACC_NUM_FOR_COMMENT[current_giveaway-1]]
        comment = COMMENT_PREFIXES[current_giveaway-1]
        for a in accs:
            comment += a + " "
        type_with_speed(comment,2)
        send_comment()
        time.sleep(1)
        if index + ACC_NUM_FOR_COMMENT[current_giveaway-1] > len(names)-1:
            index = 0
            random.shuffle(names)
        index += ACC_NUM_FOR_COMMENT[current_giveaway-1]
        current_giveaway += 1
        if current_giveaway == NUMBER_OF_GIVEAWAYS + 1:
            current_giveaway=1
            

    mutex.acquire()
    if last_key == "*":
        my_keyboard.press(Key.backspace)
        time.sleep(0.1)
        work = True
    elif last_key == "-":
        work = False
    mutex.release()