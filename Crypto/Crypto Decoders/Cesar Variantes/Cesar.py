#Python 3
#Cesar Decoder non ascii table

plaintext = input ("Introduce el mensaje a desee desencriptar: ")
key = int(input("Introduce el desplazamiento: ")) % 26
decoded = "" 


for i in range (0,len(plaintext)):
    if(((ord(plaintext[i]) >= 65) & (ord(plaintext[i]) <= 90))|( (ord(plaintext[i]) >= 97) & (ord(plaintext[i]) <= 122))):
        if(((ord(plaintext[i]) - key) < 65 & ord(plaintext[i]) <= 90)| ((ord(plaintext[i]) - key) <= 97  & ord(plaintext[i]) >= 97)): 
           decoded += chr(ord(plaintext[i]) +( 26 - key) ) 
        else:
           decoded += chr(ord(plaintext[i]) - key)
    else:
        decoded += chr(ord(plaintext[i]))
print(decoded)
