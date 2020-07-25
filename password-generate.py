import string
import random
import os
import sntplib
def password_generator():
    s1=string.ascii_uppercase
    s2=string.ascii_lowercase
    s3=string.digits
    s4=string.punctuation

    pass_len=int(input("please enter your password lenght  "))
    #to save your password with your account name or email or first name or mobile number
    # to do later it
    username=input('where you want to set password or username ')

    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    # print(s)
    random.shuffle(s)
    gen_pass=(''.join(s[0:pass_len]))
    
    save_password(username,gen_pass)
    print(gen_pass)


def save_password(passwords,usernames):
    file=open('pass.txt',mode="a+")
    s=dict()
    s[usernames]=passwords
    file.write(str(s)+'\n')
    file.close()


password_generator()