# Amicable Bot
This is was a project of mine that took around 1 month to get to this point. After leaving it for awhile, I've come back to it made it ready for Github.
## What Can This Bot Do?

- Music
- Black Jack
- Simple Moderation:
	- Purging
	- Reaction Roles
- Leveling
- Simple Economy

## Using The Bot
If you'd like to have this bot in your server, you can invite it [**here**](https://discord.com/api/oauth2/authorize?client_id=807842570695868436&permissions=8&scope=bot).  
Make sure you have a role called ``Bot`` and give it to the people that you want to have admin privileges.  
You can also use the ``!help`` command to get an understanding of the bot's ablities.

## How To Install
I've tried to make the install process as easy as possible but there's still some steps that are a little bit complicated.

- Install [Python 3.8](https://www.python.org/downloads/release/python-387/)
- Make a Python 3.8 virtual environment ``python3 -m venv /path/to/new/virtual/environment``.
- Download requirements. (This is where it might get a bit tricky):

	- In the virtual environment, pip install requirements.txt. To do this type ``pip install -r 		requirements.txt``.
	- Next, you'll need [discord-ext-menus](https://github.com/Rapptz/discord-ext-menus).
	- Make sure you have git installed and then run the command ``pip install git+https://github.com/Rapptz/discord-ext-menus`` in the virtual environment.


- Next, [make a bot account](https://discordpy.readthedocs.io/en/latest/discord.html). Make sure that you enable both privilege gateways intents. 
- Now with your Token, you can customize the bot to your liking in the ``settings.py`` file.

## Getting Music To Work

Music for the bot is handled by Lavalink. To get Lavalink to work, you need to download JDK 11 and the [Lavalink.jar](https://github.com/Frederikam/Lavalink/releases/tag/3.3.2.3). Make sure to snag the [application.yml](https://github.com/Frederikam/Lavalink/blob/master/LavalinkServer/application.yml.example) too. Make sure to change the password and match it in the ``settings.py`` file. To launch the server, use the command ```java -jar Lavalink.jar```.

## Take off!

You can now invite the bot to your server if you haven't already and launch the bot. To do so, in the Python virtual environment run ``main.py`` and fingers crossed, everything will work.

## Problems and contributing

If you want to contribute the project, you are more than welcome to, all you have to do is submit a pull request! If you have any problems or questions about the bot you can shoot me a message at ``Lemon ^-^#5752`` on discord.
