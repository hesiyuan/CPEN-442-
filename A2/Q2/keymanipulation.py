import random;
RAND_MAX = 0x7fff;
random.seed();
def exchange2letters(oldKey):
    key = list(oldKey);
    i = random.randint(0, RAND_MAX)% 25;
    j = random.randint(0, RAND_MAX)% 25;
    temp = key[i];
    key[i] = key[j];
    key[j] = temp;
    newKey = "".join(key);
    return newKey;
    
def swap2rows(oldKey):
    i = random.randint(0, RAND_MAX)%5;
    j = random.randint(0, RAND_MAX)%5;
    key = list(oldKey);
    k = 0;
    while k < 5:
        temp = key[i*5 + k];
        key[i*5 + k] = key[j*5 + k];
        key[j*5 + k] = temp;
        k = k+1;

    newKey = "".join(key);
    return newKey;

def swap2cols(oldKey):
    i = random.randint(0, RAND_MAX)%5;
    j = random.randint(0, RAND_MAX)%5;
    key = list(oldKey);
    k = 0;
    while k < 5:
        temp = key[k*5 + i];
        key[k*5 + i] = key[k*5 + j];
        key[k*5 + j] = temp;
        k = k+1;

    newKey = "".join(key);
    return newKey;

def reverse(oldKey):
    key = list(oldKey);
    newKey = list(oldKey);
    k = 0;
    while k<25:
        newKey[k] = key[24-k];
        k = k + 1;
    reverse = "".join(newKey) 

    return reverse;

def rowsupdown(oldKey):
    key = list(oldKey);
    newKey = list(oldKey);
    k = 0;
    while k<5:
        j = 0;
        while j<5:
            newKey[k*5 + j] = key[(4-k)*5 + j];
            j = j+1;
        k = k + 1;
    updown = "".join(newKey) 
    return updown;

def colsleftright(oldKey):
    key = list(oldKey);
    newKey = list(oldKey);
    k = 0;
    while k<5:
        j = 0;
        while j<5:
            newKey[j + k*5] = key[(4-j) + k*5];
            j = j+1;
        k = k + 1;
    updown = "".join(newKey)
    return updown;


