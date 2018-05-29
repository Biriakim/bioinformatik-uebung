def NumberToPattern(index,k):
    if k==1:                           
        return NumberToSymbol(index)   #wenn pattern nur 1 lang, dann entspricht das einfach der zugewiesenen nummer
    prefixindex=int(index)//4          #durch teilen Index durch 4 wird prefixindex erhalten
    r=int(index)%4                     #r entspricht Rest beim Teilen, 4 ist dabei die Basis
                                       #teilt index durch 4 und gibt den Rest r zurück
    symbol=NumberToSymbol(r)           #Rest entspricht Symbol in Liste
    PrefixPattern=NumberToPattern(prefixindex, k-1)  #PrefixPattern entspricht pattern vom Prefixindex(Quotient), ohne
                                                     #des letzten Nukleotids (k-mer minus dem letzten Element) + symbol ist
                                                     #das letzte Nukleotid
    return PrefixPattern + symbol               


def NumberToSymbol(r):                 #den einzelnen Nummern (0 - 3) die Base des DNA-Strangs zuordnen
    if r == 0:
        return "A"
    elif r == 1:
        return "C"
    elif r == 2:
        return "G"
    else:
        return "T"
