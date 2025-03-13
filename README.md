#WhatsApp Message Scheduler

## Overview

This Python script allows users to schedule WhatsApp messages to be sent at a specific date and time using the Twilio API. The script takes user inputs, calculates the delay required, and sends the message at the scheduled time.

## Prerequisites

Before running the script, ensure you have the following:

- A Twilio account with a verified WhatsApp sender number
- Twilio Account SID and Auth Token
- Python installed on your system
- Required dependencies installed

## Installation

1. Install the necessary Python libraries using pip:
   ```sh
   pip install twilio
   ```
2. Set up your Twilio account and get the Account SID and Auth Token.

## Usage

1. Run the script using a Python environment.
2. Enter the required details when prompted:
   - Your name
   - Recipient's WhatsApp number (including the country code, e.g., +91)
   - Message to be sent
   - Date and time when the message should be sent (in `YYYY-MM-DD ``HH:MM` format)
3. The script calculates the delay and waits until the scheduled time.
4. Once the time arrives, it sends the message via Twilio WhatsApp API.

## License

This project is open-source and for educational purposes. Please feel free to modify and distribute it as needed.

