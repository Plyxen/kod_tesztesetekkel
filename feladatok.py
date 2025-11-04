def egyedi_betuk(szoveg:str=""):
    betuk = ""
    i = 0
    
    while i < len(szoveg):
        if szoveg[i].isalpha():
            betu = szoveg[i].lower()
            if betu not in betuk:
                betuk += betu
        i += 1
    
    betuk = "".join(sorted(betuk))
    eredmeny = []
    j = 0
    
    while j < len(betuk):
        szamlalas = 0
        k = 0
        while k < len(szoveg):
            if szoveg[k].isalpha() and szoveg[k].lower() == betuk[j]:
                szamlalas += 1
            k += 1
        eredmeny.append(betuk[j] + ":" + str(szamlalas))
        j += 1
    
    return eredmeny
