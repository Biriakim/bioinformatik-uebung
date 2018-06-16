def MedianString(dna,k):                                             
    distance=float("inf")                                            #distance enstpricht lokaler Speicher (Vaiable)
    for i in range(0,4**k):                                          #für alle 4^k k-mere durchgehen und vergleichen, wobei
                                                                     #nur aktuelles Pattern gespeichert wird
        pattern=NumberToPattern(i,k)
        if distance > DistanceBetweenPatternAndStrings(pattern,dna): #geprüft, ob gespeicherte Distanz besser bzw. kleiner ist als distance
            distance=DistanceBetweenPatternAndStrings(pattern,dna)   #ist die Distanz kleiner, wird die neue Distanz gespeichert
            Median=pattern                                           
    return Median


def NumberToPattern(i,k):
    if k==1:
        return NumberToSymbol(i)
    prefixindex=int(i)//4
    r=int(i)%4
    symbol=NumberToSymbol(r)
    PrefixPattern=NumberToPattern(prefixindex, k-1)
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

def DistanceBetweenPatternAndStrings(pattern,dna):
    k=len(pattern)                                #k entspricht Länge von Pattern
    distance=0                                    #lokale Variable, auf 0 gesetzt
    for string in dna:                            #alle strings durchgehen, alle allignments durchgehen,
                                                  #Minimum der Hamming-Distanz gespeichert in hammingdistance
        hammingdistance=float("inf")              #hammingdistance auf unendlich oder zumindest größer als ermittelte
                                                  #Hamming-Distanz, damit die korrekte Hamming-Distanz wiedergegeben
                                                  #werden kann
        for i in range(0,len(string)-k+1):        #alle k-mere un string durchgehen
            a=string[i:i+k]
            if hammingdistance > HammingDistance(pattern,a):  #wenn aktuelle Hammingd-Distanz kleiner als gespeicherte
                                                              #Hamming-Distanz
                hammingdistance=HammingDistance(pattern,a)    #wird neue Hamming-Distanz (optimales Ergebnis für
                                                              #aktuellen String gemerkt
        distance = distance + hammingdistance                 #zur Variable distance wird hammingdistance addiert
    return distance


def HammingDistance(pattern,a):
    distance = 0                #mit einer Distanz von 0 beginnen und ab da zählen
    L=len(pattern)              #loop über die Indices des Strings
    for i in range(L):
        if pattern[i] != a[i]: 
            distance += 1       #plus 1 zur distance, wenn pattern und a nicht identisch sind
    return distance             #zurückgeben des finalen Counts der Unterschiede
    

