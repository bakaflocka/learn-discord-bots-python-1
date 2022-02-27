# Learning Discord Bots with Python
### Introduction</br>
The first in a series to document my path to applying Python knowledge and understanding towards something practical. Feel free to follow along and implement these bots in a Discord server. I am planning to add documentation to use alongside programs to elaborate what is needed and what each line is accomplishing.

This particular Discord Bot, programmed with Python, will post a message (application side) that it is ready once the script is run. The Bot will also reply to certain messages with a simple text reply. This GitHub repo is mostly used as an initalization - to get your bot created, and to learn how your scripts interact with Discord at a basic level.

### Needed <br/>
Python 3.10.X <br/>
Discord and Discord Bot account created through Developer Portal (instructions below) <br/>
discord.py Library(also below)</br>
Text Editor/IDE <br/>
Basic understanding of Python/programming<br/>

## Initial Setup
### Creating a Discord Bot
1. Visit the [Discord Developer Portal](https://discord.com/developers/applications) and log in with your Discord account. 
2. Select "New Application" in the top right. </br>
![New Application Button in the top right](https://i.imgur.com/q80dwZa.png)
3. "Create an Application" should pop up. Enter a name, which we will keep as your Discord Bot's name. </br>
![Create an Application pop up](https://i.imgur.com/foBx65h.png)
4. Congrats! You've made your first Discord Developer application. Update that resume! </br>
5. Left-hand side: Select "Bot" under the Settings list. </br>
![Bot setting selection on left](https://i.imgur.com/qjZ18y6.png)
6. Build-A-Bot should appear if you have no bots created with this application. Select "Add bot" on the right-hand side.
![Build-a-bot menu](https://i.imgur.com/kAGkRNz.png) </br>
![Add bot button on right](https://i.imgur.com/IBvJ28m.png)
7. At the "Bot" page is where you can manage permissions for your bot, as well as access your Token. This Token is the main identifier for how your programs will communicate with the Discord API (Application Programming Interface) through your scripts and programs. </br>
![Bot token image](https://i.imgur.com/MRuujdk.png) </br>
Keep this token secret. I saved a txt file on my machine with the Token for easy reference in the future.

### Inviting your Discord Bot to your server
Note: You will need administrative level permissions to add the Discord bot to the Discord Server you are implementing it on. </br>
1. Left-hand side: Select "OAuth2" under the Settings list. Then select "URL Generator". </br>
![0Auth2 on the left hand side](https://i.imgur.com/yABhJFh.png)
2. The OAuth2 URL Generator should appear. This is where we are defining what your bot can accomplish in the server. Under "Scopes", check off the "bot" button. </br>
![URL Generator and Scope](https://i.imgur.com/sMBUlHR.png)
3. Under "Bot Permissions" is where we can specifically define what the bot can do in the server. Once you are implementing the bot into a bigger server with practical uses, you will **100% need to take care with your choices here**. For learning purposes, I selected Administrator, which will help act as a catch-all for all uses. </br>
![Bot Permissions](https://i.imgur.com/xTXpCEv.png)
4. A URL should be generated under the permissions. Copy the text and paste into your browser. </br>
![URL has been generated](https://i.imgur.com/NCyodF7.png)
5. You will now be able to select which server you can add your bot to, from the drop down list. Once you've selected your server, click Continue and through the Authorization menu next. The bot should now be added to your server! </br>
![Adding the bot to your server](https://i.imgur.com/Qavj9uW.png) </br>
![Bot added](https://i.imgur.com/AmynN5p.png)

### Installing the discord.py Library
1. Using your command line, enter the text below to install the Library locally.
```
py -3 -m pip install -U discord.py
```
You will see your command line "go crazy" with different text and graphics. This is okay, and means that the library is installing! You may need to use pip3, depending on your OS. </br>
![terminal installing Discord library](https://i.imgur.com/eX4WkCU.png) </br>
2. You should now be ready to begin scripting Discord bots in your preferred IDE!

## Running Python Scripts
There are many ways to run scripts once they are saved. Extensive documentation on how to run scripts is located on this RealPython's [How to Run Your Python Scripts](https://realpython.com/run-python-scripts/) instruction article.
