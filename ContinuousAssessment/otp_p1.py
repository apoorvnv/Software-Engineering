# SEND MAIL FROM SENDER TO RECEIVER MAIL

import random
import smtplib  #number of digits of OTP

def get_email():
    n=int(input("Enter value of number of digits to generate OTP: "))
def GENERATE_OTP():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('apoorvnv@gmail.com',password='xxxx xxxx xxxx xxxx')
    otp=''.join([str(random.randint(0,9))for i in range(n)])
    msg='Hello, your otp is '+str(otp)
    server.sendmail('apoorvnv@gmail.com','anyscientist2002@gmail.com',msg)
    # server.sendmail('apoorvnv@gmail.com','ashwindg2020@gmail.com',msg)
    # server.sendmail('apoorvnv@gmail.com', 'hardikachaudhari02@gmail.com', msg)
    server.quit()
    print(otp)
get_email()
GENERATE_OTP()

''' MAKE FOLLOWING CHANGES IN CODE'''
# 1.minimum 2 function (done)
# 2.variables length (done)
# 3.Try to avoid HARDCODING
# mail this code at -->> " awk@dbatu.ac.in " <<--
