import smtplib
from email.mime.text import MIMEText

def gen_one(username,password):
    content = '''
    This is a test by python
'''

    from_addr = 'colin@ec2gpu.com'
    to_addrs = "jicheng3000@gmail.com"

    msg = MIMEText(content)
    msg['Subject'] = 'test'
    msg['From'] = from_addr
    msg["To"] = to_addrs

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_addr, to_addrs, msg.as_string())
    server.quit()

if __name__ == '__main__':
    gen_one("jicheng3000@gmail.com","hw7brmsm8lsbOo9LzS16Jycglc0LuM")