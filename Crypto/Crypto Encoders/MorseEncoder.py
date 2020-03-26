#Morse encoder

Plaintext = str.upper(str(input("Introduzca el texto a codificar: ")))
alphabet=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-.-","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-.--","--.."]
num=["-----",".----","..---","...--","....-",".....","-....","--...","---..","----."]

for i in range (0,len(Plaintext)):
    
    if((ord(Plaintext[i]) >= 65 )):    
        index =(ord(Plaintext[i])-65)
        print (alphabet[index], end="")
        print ("/", end="")
    else:
        if((ord(Plaintext[i]) >= 48 )&(ord(Plaintext[i]) < 58)):
            index =(ord(Plaintext[i])-48)
            print (num[index], end="")
            print ("/", end="")
        else: 
            print("/", end="") 
print("/")
