with open('data.txt','r') as fd:
    stri = str(fd.read())
    fd.close()
    
def vowel_counter(stri):
    a = "a"
    A = "A"
    e = "e"
    E = "E"
    i = "i"
    I = "I"
    o = "o"
    O = "O"
    u = "u"
    U = "U"
    y = "y"
    Y = "Y"
    ae = "æ"
    AE = "Æ"
    oe = "ø"
    OE = "ø"
    aa = "å"
    AA = "Å"

    acount = 0
    ecount = 0
    icount = 0
    ocount = 0
    ucount = 0
    ycount = 0
    aecount= 0
    oecount = 0
    aacount = 0


    if A or a in stri :
        acount = acount + 1

    if E or e in stri :
        ecount = ecount + 1

    if I or i in stri :
        icount = icount + 1

    if o or O in stri :
        ocount = ocount + 1

    if u or U in stri :
        ucount = ucount + 1
        
    if y or Y in stri :
        ycount = ycount + 1
        
    if oe or OE in stri :
        oecount = oecount + 1
        
    if ae or AE in stri :
        aecount = aecount + 1

    if aa or AA in stri :
        aacount = aacount + 1


    vowel_count = acount + ecount + icount + ocount + ucount + ycount + oecount + aecount + aacount
    return vowel_count

print(vowel_counter(stri))