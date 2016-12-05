__author__ = 'shikun'
from testDAL import email

def send_mail(memail):
    email.send_mail(memail)
def read_email(memail):
   return email.read_email(memail)

