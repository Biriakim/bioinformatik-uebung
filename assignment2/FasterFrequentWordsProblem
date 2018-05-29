def FasterFrequentWords(text,k):
    FrequentPatterns = []                           #Ausgabeliste, leeres set
    FrequencyArray=[]                               
    FrequencyArray = ComputingFrequencies(text,k)                      
    maxCount = max(FrequencyArray)                        
    for i in range(0, 4**k):                        #** steht für den Exponenten
        if FrequencyArray[i]==maxCount:             #finden der Indizes, bei denen pattern maximal im FrequencyArray vorkommt    
            pattern = NumberToPattern(i,k)          #index (i) wird durch 4 geteilt, der Rest
                                                    #entspricht dem letzten Nukleotid; jeder nachfolgende Quotient wird geteilt und der Rest, der einem
                                                    #weiteren vorangehenden Nukleotid entspricht, gemerkt, bis Quotient 0 ist
            FrequentPatterns.append(pattern)        #Hashwert des patterns wird in FrequentPatterns eingespeichert 
    FrequentPatterns=list(set(FrequentPatterns))    #Dublikate entfernen
    return FrequentPatterns                       


def ComputingFrequencies(text,k):
    FrequencyArray=[]                               #FrequentArray als leeres set
    for i in range(0, 4**k):                        #Schleife, initiieren Array mit 0en, ohne -1 da der letzte Wert in der Schleife nicht mitzählt
        FrequencyArray.append(0)                    #Hashwert am Anfang für alle pattern 0
    for i in range(0,len(text)-k):                  #Schleife duch text, len() Funktion für die Länge der Liste (alle items in der Liste)
        pattern=text[i:i+k]
        j=PatternToNumber(pattern)
        FrequencyArray[j] += 1                      #setzten Counter für pattern an entsprechender Stelle im Array um 1 hoch
    return FrequencyArray


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


def NumberToPattern(i,k):
    if k==1:
        return NumberToSymbol(i)
    prefixindex=i//4
    r=i%4
    symbol=NumberToSymbol(r)
    PrefixPattern=NumberToPattern(prefixindex, k - 1)
    return PrefixPattern + symbol


def NumberToSymbol(r):
    if r == 0:
        return "A"
    elif r == 1:
        return "C"
    elif r == 2:
        return "G"
    else:
        return "T"

