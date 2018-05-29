def FrequencyArray(text, k):            #Funktion mit Parameter text und k
    array = []                          #leeres set
    for i in range(0, 4**k):
        array.append(0)                 #Hashwert für alle pattern in array 0
    for i in range(0,len(text)-k+1):
        pattern=text[i:i+k]
        num = PatternToNumber(pattern)
        array[num] = array[num] + 1     #setzten Counter für pattern an entsprechender Stelle im Array um 1 hoch
    return array

#Ausgabe ist frequency array der Länge 4^(k) eines strings, das i-te Element des Arrays enthält Häufigkeit, dass das
#i-te k-mer in text in lexikographischer Anordnung vorkommt

def PatternToNumber(pattern):
    if pattern == "":
        return 0
    symbol = pattern[-1]
    prefix = pattern[:-1]
    return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)

def SymbolToNumber(symbol):
    if symbol == "A":
        number = 0
    elif symbol == "C":
        number = 1
    elif symbol == "G":
        number = 2
    elif symbol == "T":
        number = 3
    return number


