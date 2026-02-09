# Telegram Bot as a Full-time Background Service on macOS

> **Note:** This approach was tested and confirmed working in February 2026 on macOS using Python 3.13 and the latest python-telegram-bot library.

A simple and effective way to discover the Global IP of your Mac Server when you're not at home and don't want to spend money on fixed IP or DNS services.

It creates a full-time background service on your Mac which answers your mobile commands all the time and returns the values for the programmed functions in the script.

Therefore, it's a base for ANY KIND of remote controlled applications using a Telegram bot - just implement the actions in the .py file.

Created using the <a href="https://core.telegram.org/bots">Telegram Bot API</a>, the <a href="https://github.com/python-telegram-bot/python-telegram-bot">python-telegram-bot</a> Python package (the modern replacement for the deprecated telepot), and the <a href="http://ipify.org/">ipify.org API</a>.

## Installation Steps:

**1 - Configure your Telegram bot:**

Open Telegram on your phone and search for a user called **BotFather**. To obtain a bot account, text him `/newbot` (you need the slash '/' in front). He will ask a couple of questions about your bot's name and username. At the end of the process, you will be given a token, something like `123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ`. This token represents the bot account. You are going to put this token in the Python script.

**2 - Install Python 3 and required packages:**

macOS comes with Python, but you may need to install pip3 if you don't have it. On the command line, run:

```bash
pip3 install python-telegram-bot requests
```

**3 - Create the ip.py script:**

Save the `ip.py` file in your home directory (`/Users/yourusername/`). Edit the script and replace the token with your actual Telegram Bot token.

**4 - Create the LaunchAgent directory (if it doesn't exist):**

```bash
mkdir -p ~/Library/LaunchAgents
```

**5 - Create a launchd service plist file:**

Save the `com.yourusername.telepot.plist` file inside:

```
~/Library/LaunchAgents/
```

Edit the plist file accordingly, changing:
- `yourusername` to your actual macOS username
- `/usr/local/bin/python3` to your actual Python 3 path (find it with `which python3`)
- Verify the path to `ip.py` matches your file location

**6 - Create logs directory:**

```bash
mkdir -p ~/logs
```

**7 - Turn it into a full-time background service:**

Run the following command to load and start the service:

```bash
launchctl load ~/Library/LaunchAgents/com.yourusername.telepot.plist
```

The service will auto-run on every boot of your Mac.

**Managing the service:**

```bash
# Start the service
launchctl start com.yourusername.telepot

# Stop the service
launchctl stop com.yourusername.telepot

# Check if it's running
launchctl list | grep telepot

# View logs
tail -f ~/logs/telepot.log
tail -f ~/logs/telepot_error.log

# Unload (disable) the service
launchctl unload ~/Library/LaunchAgents/com.yourusername.telepot.plist
```

To confirm it works, send the `/ip` command from your phone and receive your Mac's Global IP address.

You can use this for remote SSH access, file management, system monitoring, or any other automated tasks. Just implement new features and commands in the .py script!
