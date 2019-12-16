from cs50 import get_string
from sys import argv
from sys import exit
#test

def main():
    if (len(argv)==1):
        print(f"error! you forgot a comad line argument {argv[0]}")
        exit("1")
    if (len(argv)>=3):
        print("err0r! you gave to mey cammand line arguments!")
        exit("1")
    
    k= int(argv[1])
    plaintext = get_string("plaintext: ")
    print("ciphertext: ", end="")
    
    for i in plaintext:
        # lower case
#        if (ord(plaintext[i])>=97):
        
        if (ord(i)>=97):
            c = chr(((ord(i)+ k -97)%26)+97) 
        
        elif(int(ord(i))>=65):
             c = chr(((ord(i)+ k -65)%26)+65) 
        elif (i==" "):
            c=" "
             
        else:
            c=i;
        print(c, end="")
        
#print("")

    

if __name__ == "__main__":
    # execute only if run as a script
    main()
    print("")
    
