# -*- coding:utf-8 -*-

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib
import configparser
from common import operateFile as oa

def read_email(Memail):
    if oa.OperateFile(Memail.file, "r").check_file() == False:
        print("文件不存在")
        return
    config = configparser.ConfigParser()
    config.read(Memail.file, encoding='utf-8')
    Memail.report = "report.xlsx"
    Memail.to_addr = eval(config['DEFAULT']['to_addr'])
    Memail.mail_host = config['DEFAULT']['mail_host']
    Memail.mail_user = config['DEFAULT']['mail_user']
    Memail.mail_pass =  config['DEFAULT']['mail_pass']
    Memail.port = config['DEFAULT']['port']
    Memail.headerMsg = config['DEFAULT']['headerMsg']
    Memail.attach = config['DEFAULT']['attach']
    return Memail


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
def send_mail(Memail):
    '''

    :param f: 附件路径
    :param to_addr:发给的人 []
    :return:
    '''
    from_addr = Memail.mail_user
    password = Memail.mail_pass
    # to_addr = "ashikun@126.com"
    smtp_server =Memail.mail_host

    msg = MIMEMultipart()

    # msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
    msg['From'] = _format_addr('施坤<%s>' % from_addr)
    msg['To'] = _format_addr('大人 <%s>' % Memail.to_addr)
    msg['Subject'] = Header(Memail.headerMsg, 'utf-8').encode()

    msg.attach(MIMEText(Memail.attach, 'plain', 'utf-8'))
    part = MIMEApplication(open(Memail.report, 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=Memail.report)
    msg.attach(part)

    server = smtplib.SMTP_SSL(smtp_server, Memail.port)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, Memail.to_addr, msg.as_string())
    server.quit()
