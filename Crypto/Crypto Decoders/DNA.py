 #!/usr/bin/env python

codon=["AAA","AAC","AAG","AAT","ACA","ACC","ACG","ACT","AGA","AGC","AGG","AGT","ATA","ATC","ATG","ATT","CAA","CAC","CAG","CAT","CCA","CCC","CCG","CCT","CGA","CGC","CGG","CGT","CTA","CTC","CTG","CTT","GAA","GAC","GAG","GAT","GCA","GCC","GCG","GCT","GGA","GGC","GGG","GGT","GTA","GTC","GTG","GTT","TAA","TAC","TAG","TAT","TCA","TCC","TCG","TCT","TGA","TGC","TGG","TGT","TTA","TTC","TTG","TTT"]
trans=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"," "," "]


string = 'GATCCGGCGCGCACTCTAACACCCGCACTGTCTACCTCTAACTACGTCTTCCTATCCAGCGCGCCCGCTTCCGCGCGATCAATACTGCTTCCTAACAATAGATCTTGCGTACACTACTTC'

print(len(codon))
print(len(trans))
for i in range( 0, len(string), 3 ):
    piece =  string[i:i+3]
    for j in range(0,len(codon)):
        if((piece == codon[j])):
            print(trans[j],end="")  

