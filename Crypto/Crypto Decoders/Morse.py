#Morse decoder

dots=[".","+","*","'",",","0","‚","‘","’","°","´","·","¸","º","i","I","a","A","e","E","u","U"]
dash=["-","1","_","~","¯","¹","o","O"]
separator = [ " ", "/" , "\\" ]
plaintext=str(input("Introduzca el mensaje a decodificar: "))
todecode=""
char = ""
   
for i in range(0,len(plaintext)):
    for j in range(0,len(dots)):
        if(plaintext[i] == dots[j]):
            todecode += "."
    for j in range(0,len(dash)):
        if(plaintext[i] == dash[j]):
            todecode += "-"
    for j in range(0,len(separator)):
        if(plaintext[i] == separator[j]):
            todecode += "/"
todecode += "/" 
alphabet=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-.-","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-.--","--.."]
num=["-----",".----","..---","...--","....-",".....","-....","--...","---..","----."]

for i in range(0,len(todecode)):
    if((todecode[i]== ".")|(todecode[i] == "-")):
        char += todecode[i]
    else:
        for j in range(0,len(alphabet)):
            if(alphabet[j] == char):
                char = ""
                print(chr(65+j), end="")
        for j in range(0,len(num)):
            if(num[j] == char):
                char=""
                print(chr(48+j), end="")
print("")
