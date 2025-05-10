#Owen O'Neil
#Program 5 Basic: Ceasar
#3/11/24

from time import time
def cipher():
    f=open('ciphertexts.txt','r')#file holding text
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
            print("Shift = {}: {}".format(num,translated))
            
    f.close()#close file
start= time()
cipher()#call subroutine
end=time()
print('The process took {} seconds.'.format(end-start))
