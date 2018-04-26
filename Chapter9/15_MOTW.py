### Sending email

# imports
import smtplib
import email.utils
from email.mime.text import MIMEText

# Variables for mailtrap.io
RECIPENT    = 'test@kolo.com'
EMAIL_HOST  = 'smtp.mailtrap.io'
EMAIL_HOST_USER = 'f8b375ef9a1a90'
EMAIL_HOST_PASSWORD = 'a249e76f0a4964'
EMAIL_PORT = 2525

# Configurations
server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
server.set_debuglevel = True

server.ehlo()
print('logging in')
server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)

# Create the message
msg = MIMEText('Hello Email. Test Email sent from Python')
msg.set_unixfrom('Isfaaq')
msg['To'] = email.utils.formataddr(('PikPik', RECIPENT))
msg['From'] = email.utils.formataddr(('Isfaaq',
                                      'isfaaq@pype.com'))
msg['Subject'] = 'Test from PyMOTW'

# Sending email
server.sendmail('isfaaq@pype.com',
                [RECIPENT],
                msg.as_string())
server.quit