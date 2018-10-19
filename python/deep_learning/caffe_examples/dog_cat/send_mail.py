import smtplib
from email.mime.text import MIMEText
import sys

def gen_one(content, username,password):
    content = '''
    The test has finished.
'''

    from_addr = 'colin@ec2gpu.com'
    to_addrs = "jichen3000@gmail.com"

    msg = MIMEText(content)
    msg['Subject'] = 'finished'
    msg['From'] = from_addr
    msg["To"] = to_addrs

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_addr, to_addrs, msg.as_string())
    server.quit()

if __name__ == '__main__':
    # import print_helper
    # sys.argv.p()
    # len(sys.argv).p()
    content = "The test has finished."
    if len(sys.argv) >= 2:
        content = sys.argv[1]
    gen_one(content,"jicheng3000@gmail.com","hw7brmsm8lsbOo9LzS16Jycglc0LuM")
    print("Send OK!")