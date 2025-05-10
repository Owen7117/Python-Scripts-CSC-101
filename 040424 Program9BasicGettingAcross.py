#Program 9 Basic: Getting Across
#Owen O'Neil
#04/06/24


def GetAcross(index, line):
    #end of string
    if index == len(line) - 1:#if end of string return 1 
        return 1
    #if you are on a mouontain
    if line[index] == '^':#if on mountain or not enough space to jumpp
        return 0 #cant work 
    comboCounter = 0
    if line[index]== "-":
        comboCounter += GetAcross(index + 1, line)#if current index is "-" move 1 index to the right, once finished add to combo counter
    if line[index]== "-" and index < len(line) - 2:
        comboCounter += GetAcross(index + 2, line)#if current index is "-" and the next 2 are "-" move 2 index to the right. = jump, once finished add to combo counter
    return comboCounter 
    

f=open('paths.txt','r')#open paths file 
for line in f:#read file 
    line= line.strip('\n') #delete spaces after each line
    GetAcross(0, line)#call subroutine
    print("Path: : {}".format(line))
    print("Number of possible ways across: {}".format(GetAcross(0,line)))
f.close()#close paths file 