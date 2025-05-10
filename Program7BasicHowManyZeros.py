#Program 7 Basic: How Many Zeros
#Owen O'Neil
#3/21/24

from time import time 
#start Chat.gpt Aproach
#slower
#use numbers rather than converting them to a string
def count_zeros(n):
    count = 0
    for i in range(1, n + 1):#numbers from 1 to input number
        num = i
        while num > 0: #number has to be grater than zero for loop to run 
            if num % 10 == 0: #if the remainder of individual num is zero/ dividend is completely devisible,A.K.A num=0, it adds 1 to count 
                count += 1
            num //= 10 #strips right most digit and runs it throught if statement again  
    return count #returns the total count of zeros encountered 

number = int(input("Enter a number: "))
start=time()
zeros_count = count_zeros(number)#number = n 
print(f"The number of zeros from 1 to {number} is: {zeros_count}")
#end Chat.gpt Aproach
end=time()
print("The process took {} seconds".format(end-start))



from time import time
#Start My Aproach
#uses string to find zero instead of number
#faster
def countzeros(given_number):
    count=0
    for i in range(1,given_number + 1):# the +1 includes the given number
        count += str(i).count('0')#converts wach number to a string and reads wach one
                            # if it contains a 0 it will add one to the counter
    print("There are {} zeros from 1 to {}".format(count,given_number))
given_number=int(input("Enter a Positive Number: "))
start=time()        
countzeros(given_number)#call subroutine
end=time()
print("The process took {} seconds".format(end-start))
#end My Aproach     

#My approach is faster becuase it is quicker to read through every number as a string and count how many times a zero is shown rather than having to do devide each number and determine if it is a zero or not
#for smaller inputs it doesnt matter as much and is very hard to tell becuase it is done so quick