with open('data.txt','r') as fd:
    stri = str(fd.read())
    fd.close()
   
vowels = ["a", "e", "i", "o", "u", "y", "æ", "ø", "å"] 
def vowel_counter(strengs):

    strengs=strengs.lower()
    teller= 0
    for s in strengs:
        if s in vowels:
            teller += 1
    return teller

print(vowel_counter(stri))