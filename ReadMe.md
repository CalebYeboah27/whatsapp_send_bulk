# WhatsApp Bulk Messaging

## Overview

This Python script automates the process of sending bulk messages via WhatsApp. It is designed to be integrated into a Customer Relationship Management (CRM) system to send messages to clients and customers of an organization. By using this script, you can streamline your communication efforts and reach a large number of contacts efficiently.

## Features

- **Bulk Messaging**: Send messages to multiple contacts simultaneously.
- **Customizable Messages**: Personalize messages for each contact.
- **Contact List**: Import a list of contacts from a CSV file.
- **Automated Messaging**: Send messages at scheduled times.
- **Logging**: Keep track of sent messages and any errors.

## Prerequisites

Before using this script, make sure you have the following prerequisites:

- Python 3.6 or higher installed on your system.
- The `selenium` library installed. You can install it using `pip`:

  ```
  pip install selenium
  ```

- The [Chrome WebDriver](https://chromedriver.chromium.org/downloads) compatible with your Chrome browser version. Make sure to place the WebDriver executable in a directory that is included in your system's PATH.

## Getting Started

1. Clone or download this repository to your local machine.

2. Install the required dependencies if you haven't already (see Prerequisites above).

3. Create a CSV file containing the list of contacts you want to send messages to. The CSV should have at least two columns: `Name` and `Phone`. You can add more columns for additional information if needed.

4. Edit the `config.json` file to configure your WhatsApp login credentials and other settings:

   ```json
   {
       "webdriver_path": "/path/to/chromedriver",
       "whatsapp_url": "https://web.whatsapp.com/",
       "message_delay": 2,
       "contacts_csv": "contacts.csv",
       "message_template": "Hello {Name}, this is a test message.",
       "scheduled_time": "2023-09-30 10:00:00"
   }
   ```

   - `webdriver_path`: The path to your Chrome WebDriver executable.
   - `whatsapp_url`: The URL for WhatsApp Web.
   - `message_delay`: Delay in seconds between sending messages (to avoid being flagged as spam).
   - `contacts_csv`: The name of the CSV file containing your contact list.
   - `message_template`: The message template with placeholders for contact information.
   - `scheduled_time`: The date and time when you want to start sending messages (optional).

5. Run the script:

   ```
   python whatsapp_bulk_messaging.py
   ```

6. Follow the on-screen instructions to log in to WhatsApp Web by scanning the QR code with your mobile device.

7. The script will automatically send messages to your contacts based on the configured settings.

## Usage Tips

- Make sure to keep your WhatsApp Web session open while the script is running.

- Adjust the `message_delay` to control the rate at which messages are sent to avoid being blocked by WhatsApp.

- Customize the `message_template` to include personalized information from your contact list.

- You can schedule the messaging process to start at a specific time by setting the `scheduled_time` in the `config.json` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

Please use this script responsibly and ensure compliance with WhatsApp's terms of service and any applicable laws and regulations. The authors of this script are not responsible for any misuse or violation of WhatsApp's policies.