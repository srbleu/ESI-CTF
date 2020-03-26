#Cesar Decoder ascii
#Non tested 
plaintext = input ("Introduce el mensaje a desee desencriptar: ")
key = int(input("Introduce el desplazamiento: "))
decoded = "" 
key %= 127

for i in range (0,len(plaintext)):
    print(ord(plaintext[i]))
    if(ord(plaintext[i]) < key):
        decoded += chr(ord(plaintext[i])+ (127 - key) )
    else:
        decoded += chr(ord(plaintext[i]) - key)
print(decoded)
