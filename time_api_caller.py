import time
from datetime import datetime, timedelta
import urllib.request
import logging
import argparse

## Defining URL globally
API_URL = "https://ifconfig.co"

## logging implmentation
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("api_caller.log"), logging.StreamHandler()],
)


def parse_timestamps(input_timestamps):
    """
    Parses the input string of timestamps and returns a sorted list of unique datetime objects.
    """
    today = datetime.now().date()
    try:
        parsed_times = [datetime.strptime(f"{today} {ts}", "%Y-%m-%d %H:%M:%S") for ts in input_timestamps.split(",")]
        return sorted(parsed_times)
    except ValueError as e:
        logging.error(f"Invalid timestamp format: {e}")
        raise

def make_api_call():
    """
    Makes a request to the global API_URL.
    """
    ## user-agent in Headers are mandatory to have to restrict forbidden error
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/plain', #This is needful as api is returning webpage by default
    }
    try:
        req = urllib.request.Request(API_URL, headers=headers)
        with urllib.request.urlopen(req) as response:
            result = response.read().decode('utf-8')
            logging.info(f"API Response: {result}")
    except Exception as e:
        logging.error(f"Failed to make API call: {e}")

def schedule_api_calls(timestamps):
    """
    Need to Wait until the specified timestamps call and sends API requests.
    """
    for ts in timestamps:
        now = datetime.now()
        wait_time = (ts - now).total_seconds()
        
        if wait_time > 0:
            logging.info(f"Waiting for {wait_time:.2f} seconds until {ts}.")
            time.sleep(wait_time) #sleep time implementation to hold on to run next timestamp
        logging.info(f"Making API call at {ts}.")
        make_api_call()

def generate_test_timestamps(seconds=5, count=3):
    """
    Test function to Generates a list of timestamps a few seconds apart from now.
    """
    now = datetime.now()
    test_times = [(now + timedelta(seconds=i * seconds)).strftime("%H:%M:%S") for i in range(count)]
    return test_times

def main():
    """
    Main function for the script.
    """
    parser = argparse.ArgumentParser(description="Schedule API calls at specific timestamps.")
    parser.add_argument("--timestamps", type=str, required=True, help="Comma-separated list of timestamps (HH:MM:SS).")
    args = parser.parse_args()

    try:
        timestamps = parse_timestamps(args.timestamps)
        logging.info(f"Parsed timestamps: {timestamps}")
        schedule_api_calls(timestamps)
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()
