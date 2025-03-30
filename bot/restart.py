from config import *
import os
import sys
import asyncio
import logging
from telethon import events

# Configure logging
LOGS = logging.getLogger("Restart_Bot")

def register_restart_handler(bot):
    @bot.on(events.NewMessage(pattern='/restart'))
    async def restart_bot(event):
        LOGS.info(f"Received /restart command from user: {event.sender_id}")

        if str(event.sender_id) not in Config.OWNER:  # Ensure this matches your config
            return await event.reply("🚫 **You're not authorized to restart the bot!**")

        LOGS.info("Restarting bot in 2 seconds...")
        await event.reply("🔄 **Restarting bot...**")

        # Gracefully disconnect the bot
        await bot.disconnect()

        # Non-blocking sleep before restart
        await asyncio.sleep(2)

        # Restart the bot process
        os.execl(sys.executable, sys.executable, *sys.argv)