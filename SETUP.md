# Setting Up the Cryptocurrency Price Monitor

This guide will help you set up and run the Cryptocurrency Price Monitor application.

## Prerequisites

- Python 3.7 or higher
- A Telegram bot token (obtained from BotFather)
- Your Telegram chat ID

## Step 1: Set Up the Environment

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Step 2: Configure Environment Variables

1. Create a `.env` file by copying the example:
```bash
cp .env.example .env
```

2. Edit the `.env` file with your details:
- `TELEGRAM_TOKEN`: Your Telegram bot token from BotFather
- `CHAT_ID`: Your Telegram chat ID (you can get this using the "Test Telegram" button in the app)
- `SESSION_SECRET`: Any secure random string for session encryption

## Step 3: Start the Application

1. Run the application:
```bash
python main.py
```

2. Access the web interface at: http://localhost:5000

## Step 4: Configure Your Watchlist

1. In the dashboard, add the cryptocurrencies you want to monitor
2. Set appropriate threshold percentages for each coin
3. Configure alert hours in the Settings page

## Troubleshooting

- **Telegram Notifications Not Working**: Ensure your bot token is correct and you've started a conversation with your bot
- **API Rate Limiting**: The application uses batch API calls to avoid rate limiting, but if you experience issues, consider reducing the frequency of checks or the number of coins monitored
- **Error Logs**: Check the application logs for detailed error information