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
    

