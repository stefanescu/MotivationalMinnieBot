# Motivational Minnie Bot
Telegram bot. Use to brighten someone's day
Used to run on Google App Engine. Porting to Cloud Run SOON

# Usage:
1. Add @MotivationalMinnie on Telegram and use the /start command in his chat
2. Talk to him directly, or use him inline in any chat with `@MotivationalMinnie` 


# How it works:
1. Telegram bot api Webhook waits for REST hit from Telegram chat
1. Hits *website*, gets string
3. Parse and return string to Telegram bot api

# Dependencies:
Telegram bot api
https://core.telegram.org/bots/api

Flask, beautifulsoup4
