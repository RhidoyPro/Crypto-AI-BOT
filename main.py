from app import app, crypto_monitor
import logging

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.DEBUG)
    
    # Start the cryptocurrency monitoring thread
    crypto_monitor.start()
    
    # Start the Flask server
    app.run(host='0.0.0.0', port=5000)
