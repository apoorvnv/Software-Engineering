# Program to Send OTP via Mail
import random
import smtplib  # Python module to send E-mail

def send_otp():
    server = smtplib.SMTP('smtp.gmail.com',587)  #to create gmail server, "587" is port of gmail
    server.starttls()                              # tls security
    server.login('apoorvnv@gmail.com',password='xxxx xxxx xxxx xxxx)
    #n=int(input("Enter value of number of digits to generate OTP: "))  # length of OTP
    otp=''.join([str(random.randint(0,9))for i in range(4)])  # func. call of no. of digits
    msg='Hello, your otp is '+str(otp)
    vr=msg
    # server.sendmail('apoorvnv@gmail.com','ashwindg2020@gmail.com',msg)
    rc=str(input("Enter receiver's mail: "))
    server.sendmail('apoorvnv@gmail.com',str(rc),msg)
    server.quit()
    print(otp)
    return otp

def verify_otp(w):
    temp = input("Enter received OTP: ")
    if(str(w)==temp):
        print("Verified..!!!")
    else:
        print("Not Verified")

w = send_otp()
verify_otp(w)


# import smtplib  #SEND MAIL FROM SENDER TO RECEIVER
# import random
# server = smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
# server.login('apoorvnv@gmail.com',password='suua ormr pojn hxrm')
# otp=''.join([str(random.randint(0,9))for i in range(4)])
# msg='Hello, your otp is '+str(otp)
# server.sendmail('apoorvnv@gmail.com','mihirjawale2412@gmail.com',msg)
# server.quit()
# print(otp)
