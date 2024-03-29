# Teleport Bot as a Full-time background service
A simple and effective way to discover the Global IP of your domestic Raspbery pi server when you're not at home and don't want to spend money in fixed IP or DNS services.

It creates a full-time background service at your Pi Server which anwsers for your mobile commands all the time and returns the values for the programmed function in the script.

Therefore, it's a base for ANY KIND of remote controlled aplications using a telegram bot, just need to implement the actions on the .py file.

Created using the <a href="https://core.telegram.org/bots">Telegram Bot</a>, the <a href="https://github.com/nickoala/telepot">Telepot</a> Raspbery Pi/Raspbian Python Package, an adapted version of the <a href="https://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/" title="Set Up Telegram Bot on Raspberry Pi">"Set Up Telegram Bot on Raspberry Pi by NickL17"</a> tutorial and the <a href="http://ipify.org/">ipify.org API</a>.


## Instalation Steps:

**1 - Configure your telegram bot as taught in the mentioned tutorial:**

"Open Telegram on your phone, search for a user called BotFather. (...) To obtain a bot account, text him /newbot. (you need the slash '/' in front) He will then ask a couple of questions. (...) At the end of process, you will be given a token, something like 123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ. This token represents the bot account. You are going to put this token on the Pi."

**2 - Install the telepot package:**

  On the command line, run these two commands:

    sudo apt-get install python-pip
    sudo pip install telepot

**3 - Save the ipbot.py file inside your RaspberryPi:**

Edit the script changing the **```TOKEN HERE```** field with your Telegram Token (you can use the web version of the App to Copy & Paste it).

**4 - Create a service script:**

Save the ```"telegram.service"``` file inside the raspberry services default folder: 
 
    /lib/systemd/system
  
Edit it's [Service] section accordingly, changing the *```PyScriptAdressHere```* for the real local adress to the script.

**5 - Turn it into a full-time background running service:**

Run the following line on your command prompt:

    sudo systemctl enable telegram.service
    
It should put it auto-running in every boot of your RaspPi. 

To confirm it works, send the "/ip" command from your phone and know your server's Global IP.

I use it for torrent management, and SSH control of my server, among other stuff.

You can always implement new features and new commands to the .py script.


