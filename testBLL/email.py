__author__ = 'Administrator'
from testDAL import email

def send_mail(memail):
    email.send_mail(memail)
def read_email(memail):
    email.read_email(memail)

