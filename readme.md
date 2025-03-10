# Timestamp API Caller script

## Description
This script schedules API calls at specified timestamps. 

## Features
- Schedule API calls based on a list of timestamps.
- Logs all actions to both the console and a log file (`api_caller.log`).
- Includes a test function to generate timestamps for testing.
- Accepts timestamps via the Terminal.
- Utilizing API_URL globally to make api calls which is returning IPV6

## Requirements
- Python 3.6 or later and python packages like time, datetime, urllib, logging and argparse.
- No third-party dependencies.

## Step by Step implementation: 
- Unzip the directory
- You will have files included time_api_caller.py
- Open it into editor as use below commands to test the script.


## Command to hit test function i.e. generate_test_timestamps
- Run the below command in the termina at the same directory:  
- >>> python3 -c 'from time_api_caller import generate_test_timestamps; print(generate_test_timestamps())'
- Response would be like: ['17:46:14', '17:46:19', '17:46:24']

## Command to test our main call
- Make sure to change the timestamp before hitting below comamand
- >>> python3 time_api_caller.py --timestamps "17:34:10,17:35:10,17:36:10"
- Response would be like: API Response: "IPV6"
