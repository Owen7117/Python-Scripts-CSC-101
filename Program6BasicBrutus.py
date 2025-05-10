#Owen O'Neil
#Program 6 Basic: Brutus
#3/14/24

from time import time
def cipher():
    f=open('ciphertexts.txt','r')#file holding text
    r=open('words.txt','r')#file holding common words
    dictionary=[]
    for word in r:
        word = word.strip('\n')#gets rid of space after word 
        word = word.upper() #makes every charagter uppercase
        dictionary.append(word)
            
    for line in f:#loop that reads file line by line 
        line=line.strip('\n')#get rid of space at end
        message=''
        message=message+line
        letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num=0
        print("Chiphertext: {}".format(message))
        for translated in range(len(letters)-1):#if inclued the 26th letter it will translate the same thing as the first 
            translated=''
            num+=1
            for character in message: 
                index = letters.find(character)
                if index>=0:#must fall in index from 0 and up
                    index -= num#takes the letter back by num to match correct original leter
                    if index > 25:#goes back to A if it passes Z
                        index= index-25
                    translated += letters[index]
                else:
                    translated += character#prints characters that arent letters
            
            count = 0
            for word in translated.split():#splits words in the final correct translation 
                if (word in dictionary):
                    count += 1#increases count of correct words 
            if count > len(translated.split())*0.4:# if count is grater than 40% of the ciphered sentence it is correct
                print("Shift = {}: {}".format(num,translated))               
                       
    f.close()#close file
start= time()
cipher()#call subroutine
end=time()
print('The process took {} seconds.'.format(end-start))

