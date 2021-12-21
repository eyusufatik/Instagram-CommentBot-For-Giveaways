# Instagram-CommentBot-For-Giveaways
This is the bot I used to win a 3d printer filament giveaway on Instagram.

Usually giveaways require you to tag other people, so I made a bot to tag people in the commments.

It works with macros on a browser.

## Usage is simple:

1. Configure `instabot.py` by changing:
   - Number of giveaways the bot will work for.
   - The number of accounts needed for a comment.
   - Prefixes (hashtags or words if needed).
   - The main modifier key for changing tabs in the browser (Cmd for mac in safari and chrome, Ctrl for windows)
2. Create a file named `names.txt`and add account names (in seperate lines) you want to use in the comments. (e.g. @eyusufatik)
3. Run the bot with `python3 instabot.py`.
4. Open up tabs for the giveaways (these tabs must be the only tabs in that window) and leave the pointer on the comment input box.
5. Press `*` to start the bot.
6. Press `-` to stop the bot.

The bot doesn't stop when it hits the Instagram per-hour-comment limit. I had written `observer.js` to try and see if I can catch the limit pop-up to make the bot stop, but I haven't fully implemented it yet. The plan is when the pop-up is "catched" the js code will send some message to my bot over sockets and let the bot know it should go into cooldown mode. To be honest, I haven't made any changes to the project in over a year and I don't plan to; so this feature won't be ever implemented probably.
