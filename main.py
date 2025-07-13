from flask import Flask, request
import telebot
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("8108946102:AAGxJvPu8zm75ar7-Sgdog16uhjAyfIOmgc")
bot = telebot.TeleBot(BOT_TOKEN)

GROUP_CHAT_ID = -1002793890547  # Replace with your group ID

@app.route('/')
def home():
    return "✅ Backend is alive"

@app.route('/verified', methods=['POST'])
def handle_verified():
    data = request.json
    uid = data.get("uid", "N/A")
    region = data.get("region", "N/A")
    status = data.get("status", -1)
    player = data.get("player", "N/A")
    before = data.get("likes_before", 0)
    after = data.get("likes_after", 0)
    added = data.get("likes_added", 0)

    # 📢 Format message
    msg = f"""
🎯 *Like Result*

👤 *Player:* `{player}`
🆔 *UID:* `{uid}`
🌍 *Region:* `{region}`

👍 *Before:* `{before}`
❤️ *After:* `{after}`
📦 *Added:* `{added}`

✅ *Status:* {'Success' if status == 1 else 'Already Liked' if status == 2 else 'Error'}
"""

    bot.send_message(GROUP_CHAT_ID, msg, parse_mode="Markdown")
    return "✅ Posted to Telegram", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))