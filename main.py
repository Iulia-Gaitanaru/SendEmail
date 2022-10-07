import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# Customize email to each specific person
if __name__ == '__main__':
    html = Template(Path('index.html').read_text())
    email = EmailMessage()
    email['from'] = 'Gaitanaru Iulia'
    # TODO: write the email of the person to whom you are sending mail
    email['to'] = ''
    email['subject'] = 'You won 1,000,000 $$$'
    email.set_content(html.substitute(name='dummy'), 'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        # TODO: write your email and password
        smtp.login('', '')
        smtp.send_message(email)
        print("Sent it!")
