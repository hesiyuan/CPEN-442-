import subprocess
import sys
import os
import pycrc
import keymanipulation
import string
import random
import thread

retval = os.getcwd();

print retval;

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



def call_routine(string):
    sys.argv = ['pycrc.py','--model','crc-32','--check-string',string]
    crc = pycrc.main();
    return crc;


def hacker(threadName, start):
    #print call_routine("T2W704SG90")
    #print call_routine("9IBQU5B5AN")
    print "starting", threadName;
    print "start", start;
    #crc1 = 2417756558;
    count = start;
    hashtable = {};
    while True:
        string = id_generator();
        crc = call_routine(string);
        if crc in hashtable:
            print "found, ",hashtable[crc];
            break;
        hashtable[crc] = string;
        count += 1;
        if count % 1000 ==0:
            print count," ", crc;
    print "done"
    print "string: ", string;

try:
    thread.start_new_thread(hacker, ("Hacker-1",0));
except:
    print "Error"

while True:
    pass


