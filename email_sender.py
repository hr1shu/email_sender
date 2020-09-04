import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'RISHAV KUMAR'   ##ur username
email['to'] = 'pritamk774@gmail.com'
email['subject'] = 'sending it via coding bITCH !!'

email.set_content('Happy halloweeen  hosss:P:;-)!!!!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('merishujaiswal@gmail.com', 'Rishav@11')
    smtp.send_message(email)
    print('all good hoss!!!!!')
