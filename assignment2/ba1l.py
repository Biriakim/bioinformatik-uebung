def PatternToNumber(pattern):
    if pattern == "":
        return 0             #leeres pattern hat Nummer 0
    symbol = pattern[-1]     #symbol entpricht dem letzten Nukleotid
    prefix = pattern[:-1]    #prefix ist alls vor dem letzten Nukleotid (Länge k - 1)
    return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)
#geben passende Nummer für letztes Symbol aus und rufen Funktion noch einem rekursiv auf für Buchstaben davor
#den müssen wir noch mit 4 multiplizieren, da jedes k-mer eines DNA-Strangs, wenn das letztes Symbol entfernt
#wird, 4mal vorkommt
#Ausgabe ist der Index in der lexikographischen Anordnung des k-mers

def SymbolToNumber(symbol): #den einzelnen Basen des DNA-Strangs Nummern zuordnen
    if symbol == "A":
        number = 0
    elif symbol == "C":
        number = 1
    elif symbol == "G":
        number = 2
    elif symbol == "T":
        number = 3
    return number
