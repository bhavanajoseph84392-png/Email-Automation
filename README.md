# Email Automation Using Python (SMTP)

## 📌 Project Overview

The **Email Automation Using Python** project is a simple Python application that sends emails automatically to multiple recipients using Gmail's SMTP (Simple Mail Transfer Protocol) server.

The application uses Python's built-in `smtplib` module to connect to Gmail's SMTP server and the `EmailMessage` class to create and send email messages. It sends a welcome email to each recipient from a predefined list.

This project was developed using **Python IDLE** to practise email automation, SMTP communication, and Python programming fundamentals.

## 🎯 Project Objectives

- Understand the working principle of SMTP.
- Automate email sending using Python.
- Send emails to multiple recipients using a list.
- Create email messages dynamically for each recipient.
- Learn how to connect and authenticate with an SMTP server.
- Practise Python modules, loops, and message handling.

## ✨ Features

- **Automated Email Sending:** Sends emails programmatically without manually composing each message.
- **Multiple Recipients:** Sends individual emails to multiple email addresses.
- **Custom Email Subject:** Sets a subject for each outgoing email.
- **Custom Email Content:** Defines the body of each welcome email.
- **Gmail SMTP Integration:** Uses Gmail's SMTP server to send messages.
- **Secure SMTP Connection:** Uses STARTTLS to encrypt the connection.
- **Reusable Logic:** Uses a loop to send emails to all recipients in a list.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Development Environment:** Python IDLE
- **Libraries and Modules:**
  - `smtplib` — connects to the SMTP server and sends emails.
  - `email.message.EmailMessage` — creates structured email messages.
  - `os` — reads credentials from environment variables in the secure version.

## 📚 Concepts Used

### 1. SMTP (Simple Mail Transfer Protocol)

SMTP is a protocol used to send emails between mail servers. This project uses Gmail's SMTP server to send outgoing emails.

### 2. Python `smtplib`

The `smtplib` module provides functionality to connect to an SMTP server, authenticate, and send emails.

### 3. EmailMessage Class

The `EmailMessage` class helps create an email by specifying its subject, sender, recipient, and body.

### 4. STARTTLS

STARTTLS upgrades the SMTP connection to an encrypted connection. This project uses port **587**, commonly used for SMTP with STARTTLS.

### 5. Lists and Loops

A Python list stores the recipient email addresses, and a `for` loop sends an individual message to each recipient.

## 📂 Project Structure

```text
Email-Automation/
│
├── email_automation.py
└── README.md
```

## ⚙️ Requirements

- Python 3.x
- Python IDLE or Visual Studio Code
- A Gmail account with SMTP access
- A Google App Password, when required and supported by the account

The project uses Python's standard library, so no external packages are required.

## 🚀 How to Run the Project

### Step 1: Create the Python File

Open Python IDLE and create a new file named:

```text
email_automation.py
```

Paste the project code into the file and save it.

### Step 2: Configure Your Credentials

For security, do not hardcode your Gmail address or App Password in the Python file.

Set these environment variables before running the program:

- `SMTP_EMAIL` — your sender Gmail address
- `SMTP_APP_PASSWORD` — your Gmail App Password

Use a Google App Password rather than your regular Gmail password. App Passwords generally require two-step verification to be enabled on the Google Account.

### Step 3: Add Recipient Email Addresses

Add the intended recipients to the `receiver_` list in the Python program.

```python
receiver_ = [
    "recipient1@example.com",
    "recipient2@example.com"
]
```

Replace these examples with email addresses you have permission to contact.

### Step 4: Run the Program

In Python IDLE, open the saved file and select **Run → Run Module**, or press **F5**.

The application connects to Gmail's SMTP server and sends a welcome email to each configured recipient.

## 💻 Secure Example Code

The following version demonstrates the same workflow while keeping credentials outside the source code.

```python
import os
import smtplib
from email.message import EmailMessage

sender = os.environ.get("SMTP_EMAIL")
password = os.environ.get("SMTP_APP_PASSWORD")

receivers = [
    "recipient1@example.com",
    "recipient2@example.com"
]

if not sender or not password:
    raise RuntimeError(
        "Set SMTP_EMAIL and SMTP_APP_PASSWORD first."
    )

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)

        for email in receivers:
            msg = EmailMessage()
            msg["Subject"] = "Welcome Mail"
            msg["From"] = sender
            msg["To"] = email
            msg.set_content("Hi buddy")

            server.send_message(msg)
            print(f"Email sent to {email}")

except (smtplib.SMTPException, OSError) as error:
    print(f"Email sending failed: {error}")
```

**Note:** Configure the two environment variables in your operating system before running this example. The recipient addresses above are placeholders.

## 🔄 Application Workflow

1. Import the required Python modules.
2. Read the sender email and App Password from environment variables.
3. Define the list of recipients.
4. Connect to Gmail's SMTP server using port 587.
5. Enable encryption using STARTTLS.
6. Authenticate with the sender's Gmail credentials.
7. Iterate through the recipient list.
8. Create a separate email message for each recipient.
9. Set the subject, sender, recipient, and message body.
10. Send the email using `send_message()`.
11. Close the SMTP connection after processing.

## 📧 Example Email

**Subject:** Welcome Mail

**Message:**

Hi buddy

Each recipient receives an individual email with the configured subject and body.

## 🔐 Security Considerations

- Never publish Gmail passwords or App Passwords in source code.
- Store credentials in environment variables or a suitable secrets manager.
- Revoke any App Password accidentally exposed in code, screenshots, or a public repository.
- Send emails only to intended recipients and comply with applicable email and anti-spam rules.
- Avoid sending repeated or unsolicited bulk messages.
- Do not commit credential files to GitHub.

## ⚠️ Limitations

- The project uses a predefined list of recipients.
- The email subject and message body are fixed in the example.
- It does not use a database to store recipients or email history.
- It does not include a retry system for failed deliveries.
- Gmail sending limits and account security policies may affect delivery.
- Successful submission to the SMTP server does not guarantee delivery to the recipient's inbox.

## 🔮 Future Enhancements

- Allow users to enter recipients and message content dynamically.
- Add HTML email templates and attachments.
- Add logging to track successful and failed send attempts.
- Implement retry logic and better error handling.
- Store recipient details and delivery records in a database.
- Build a graphical interface using Tkinter or a web interface using Flask.
- Add scheduling functionality for sending emails at a specified time.

## 📚 Learning Outcomes

Through this project, I practised:

- Connecting Python applications to an SMTP server.
- Sending emails programmatically using Gmail.
- Creating email messages using `EmailMessage`.
- Working with Python lists and loops.
- Understanding SMTP authentication and STARTTLS.
- Managing credentials more securely.
- Organizing a small automation project.


