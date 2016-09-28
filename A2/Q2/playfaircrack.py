import math;
import random;
from keymanipulation import *;
import ngram_score as ns
import sys;

TEMP = 20;
STEP = 0.2;
COUNT = 10000;
RAND_MAX = 0x7fff;
bestKey = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
print "math.exp(-45.17) : ", math.exp(-45.17);
fitness = ns.ngram_score('english_quadgrams.txt');
print fitness.score('HELLOWORLD')
## using simulated annealing algorithm
def playfairCrack(cipherText, length, Key):
    
    maxKey = Key;
    plainText = decrption(cipherText, length, maxKey);
    maxscore =  fitness.score(plainText);
    bestscore = maxscore;
    
    T = TEMP;
    count = 0;
    while T >= 0:
        count = 0;
        while count < COUNT:
            newKey = changeKey(maxKey);
            ## print "newKey: ", newKey;
            plainText = decrption(cipherText, length, newKey);
            score = fitness.score(plainText);
            dF = score - maxscore;
            if dF >=0:
                maxscore = score;
                maxKey = newKey; ## is maxKey pointing to newKey?
            elif T > 0:
                prob = math.exp(dF/ T);
                if prob > 1.0*random.randint(0,RAND_MAX)/RAND_MAX:
                    maxscore = score;
                    maxKey = newKey;                   
                
            ## update the best key and score    
            if maxscore > bestscore:
                bestscore = maxscore;
                global bestKey;
                bestKey = maxKey;
            
            count = count+1;

        T -= STEP;
    
    return bestscore, bestKey;

def changeKey(oldKey):
    i = random.randint(0, RAND_MAX) % 50;
    newKey = '';
    if i == 0:
        newKey = swap2rows(oldKey);
    elif i == 1:
        newKey = swap2cols(oldKey);
    elif i == 2:
        newKey = reverse(oldKey);
    elif i == 3:
        newKey = rowsupdown(oldKey);
    elif i == 4:
        newKey = colsleftright(oldKey);
    else:
        newKey = exchange2letters(oldKey);
    
    return newKey;


def decrption(cipherText, length, key):
    result = '';

    i = 0;
    while i < length:
        a = cipherText[i];
        b= cipherText[i+1];
        a_ind = key.find(a); ## find the index of first occurance of a in key
        b_ind = key.find(b);
        a_row = a_ind / 5;
        b_row = b_ind / 5;
        a_col = a_ind % 5;
        b_col = b_ind % 5;
        if a_row == b_row:
            if a_col == 0:
                result += key[a_ind + 4];
                result += key[b_ind - 1];
            elif b_col == 0:
                result += key[a_ind - 1];
                result += key[b_ind + 4];
            else:
                result += key[a_ind - 1];
                result += key[b_ind - 1];					
        elif a_col == b_col:
            if a_row == 0:
                result += key[a_ind + 20];
                result += key[b_ind - 5];		
            elif b_row == 0:
                result += key[a_ind - 5];
                result += key[b_ind + 20];
            else:
                result += key[a_ind - 5];
                result += key[b_ind - 5];
        else:
            result += key[5 * a_row + b_col];
            result += key[5 * b_row + a_col];
        i += 2;
        
    return result;

def main():
    print('good start!')
    filename = 'ciphertext.txt'
    ##filename = 'example.txt'
    maxscore = -99e99
    key = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
    cipherText = '';
    with open(filename) as txt:
        while True:
            c = txt.read(1)
            cipherText += c;
            if not c:
                ## print "End of file"
                break
            ## print "Read a character:", c
    txt.close()
    print "cipherText: ", cipherText;
    plainText= '';
    ## the main while loop for cracking playfair cipher
    random.seed();
    i = 0;
    while True:
        i = i+1;
        score, maxKey = playfairCrack(cipherText, len(cipherText), key);
        if score > maxscore:
            maxscore = score;
            key = maxKey;
            print "current max: ", maxscore;
            print "iteration: ",i;
            print "key : ", maxKey;
            plainText = decrption(cipherText, len(cipherText), key);
            print "plainText: ", plainText;
        print "iteration : ",i;
        
# program entry point
###############################################################################
if __name__ == "__main__":
    sys.exit(main())

