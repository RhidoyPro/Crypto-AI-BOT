# Cryptocurrency Price Monitor

A Flask-powered cryptocurrency monitoring application that provides real-time price tracking and alerts via Telegram when prices exceed configured thresholds.

## Features

- Real-time cryptocurrency price monitoring via CoinGecko API
- Telegram notifications for price movements
- Configurable alert thresholds for each cryptocurrency
- Dashboard for monitoring bot status and watchlist management
- Alert history tracking
- Configured alert hours to receive notifications only during specific times

## Installation

1. Clone this repository:
```
git clone <repository-url>
cd crypto-price-monitor
```

2. Install required dependencies:
```
pip install -r requirements.txt
```

3. Set up your Telegram bot:
   - Create a bot with [BotFather](https://t.me/botfather) and get your bot token
   - Set the token as an environment variable:
   ```
   export TELEGRAM_TOKEN="your_telegram_bot_token"
   ```

## Usage

1. Start the application:
```
python main.py
```

2. Access the web interface at `http://localhost:5000`

3. Configure your watchlist and notification settings through the interface

## Configuration

- **Watchlist**: Add cryptocurrencies to monitor with specific alert thresholds
- **Alert Hours**: Set hours during which alerts will be sent (default: 7am - 11pm)
- **Telegram Chat ID**: Configure where the alerts should be sent

## Technical Details

- Uses CoinGecko's batch API endpoint to avoid rate limiting
- Logs alerts to local storage
- Monitors price changes in a background thread
- Provides a web-based dashboard for configuration