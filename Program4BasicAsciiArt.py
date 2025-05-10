#Owen O'Neil
#02/22/24
#Program 4 Basic: Ascii Art

def translate():
    f=open('ascii1-data.txt','r')# opens file
    s=""
    for line in f:
        line=line.rstrip("\n")#gets rid of right space
        if (len(line)>0):    
            elements = line.split()#seperates the inputs
            if elements[1]=="..":
                s+=(int(elements[0])*" ")#first input times space
            else:
               s+=(int(elements[0])*elements[1])#first input times second input
        else:
            print(s)
            s=""
    f.close()

translate()
