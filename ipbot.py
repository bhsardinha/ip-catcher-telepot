import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from requests import get

async def ip_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responds with the public IP when receiving /ip command"""
    ip = get('https://api.ipify.org').text
    await update.message.reply_text(f'My Mac Server IP: {ip}')
    print(f'Sent IP {ip} to user {update.effective_user.id}')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responds to /start command"""
    await update.message.reply_text('Bot is active! Use /ip to see the IP address.')

def main():
    # Create the Application with your token
    # Replace TOKEN_HERE with your actual Telegram Bot token
    app = Application.builder().token('TOKEN_HERE').build()
    
    # Add command handlers
    app.add_handler(CommandHandler('ip', ip_command))
    app.add_handler(CommandHandler('start', start_command))
    
    # Start the bot
    print('IP Bot is running...')
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
