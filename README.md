# Telegram Welcome Bot

A simple Telegram bot that:
- Welcomes new members and deletes join messages
- Deletes /start message after 10 seconds

## Deploy on Render

1. Go to https://render.com
2. Click **New → Web Service**
3. Connect your GitHub repo
4. Use the following setup:

- **Start Command**: `python bot.py`
- **Runtime**: Python
- **Environment Variable**:
  - `BOT_TOKEN = your_telegram_bot_token`

## Local Run

```bash
pip install -r requirements.txt
python bot.py
```
