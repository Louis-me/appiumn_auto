__author__ = 'Administrator'
import configparser
from Common import  OperateFile as oa
def read_email(f="email.ini"):
    if oa.base_file(f, "r").check_file() == False:
        print("文件不存在")
        return
    config = configparser.ConfigParser()
    config.read(f,encoding='utf-8')
    to_addr = eval(config['DEFAULT']['to_addr'])
    mail_host = config['DEFAULT']['mail_host']
    mail_user = config['DEFAULT']['mail_user']
    mail_pass = config['DEFAULT']['mail_pass']
    port = config['DEFAULT']['port']
    headerMsg = config['DEFAULT']['headerMsg']
    attach = config['DEFAULT']['attach']
    result = to_addr, mail_host, mail_user, mail_pass, port, headerMsg, attach
    return result

