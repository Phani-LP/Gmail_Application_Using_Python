# Gmail Application Using Python

This project demonstrates how to send emails using Python's `smtplib` library. The application allows users to input sender and receiver email addresses, a subject, and a message, and then sends the email via Gmail's SMTP server.

## Features

- Send emails using Gmail's SMTP server.
- Input-based configuration for sender and receiver email addresses, subject, and message.
- Basic error handling for email sending.

## Project Structure

- **`SendMsgUsingGmail.py`**: Contains the main implementation for sending emails using the `PythonGmail` class.

## How to Use

1. Clone the repository or download the project files.
2. Open the `SendMsgUsingGmail.py` file in your Python environment.
3. Run the script:
   ```bash
   python SendMsgUsingGmail.py
   ```
4. Enter the following details when prompted:
<ul>
<li>Sender email address</li>
<li>Receiver email address</li>
<li>Email subject</li>
<li>Email message</li>
</ul>

5. The script will attempt to send the email and display a success or error message.

### Prerequisites
<ul>
<li>Python 3.x installed on your system.</li>
<li>Enable "Less secure app access" in the sender's Gmail account settings. (Note: This is not recommended for production use due to security concerns.)</li>
<li>Replace the placeholder Gmail app password ('kghv ilil rsta zbcd') in the script with your actual Gmail app password.</li>
</ul>

### Future Enhancements
<ul>
<li>Add support for attaching files to emails.</li>
<li>Implement encryption for secure email communication.</li>
</ul>

## Disclaimer
This project is for educational purposes only. Use it responsibly and ensure compliance with Gmail's terms of service and security guidelines.
