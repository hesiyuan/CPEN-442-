import hashlib


### Simple patch program for question 4 #####
offset = 0x41F1FB

print "Enter your new password: "

password = str(raw_input())

hashValue = hashlib.sha1(password).digest()

try:
    myfile = open("19204130.program2.exe", "r+b") ## open in binary mode

    offset = myfile.read().find("\x28\x7D\x74\xA4\xB9\x7A\x21\x7F\x86\xE5\x13\x9A\xD1\x47\x81\x3C\x74\x7A\xE4\x4A")
    
    myfile.seek(offset)

    myfile.write(hashValue)

    myfile.close()
except:
    print "Error occurred"


