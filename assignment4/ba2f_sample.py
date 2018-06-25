import random

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

def NumberToSymbol(r):
    if r == 0:
        return "A"
    elif r == 1:
        return "C"
    elif r == 2:
        return "G"
    else:
        return "T"


def profileProbable(text, k, profile): #mit Profile wird jeweils das beste Motif aus der jeweiligen Sequenz gesucht
    maxprob = 0
    kmer = text[0:k]
    for i in range(0, len(text) - k +1):
        prob =1
        pattern =text[i:i+k]
        for j in range(k):
            l = SymbolToNumber(pattern[j])
            prob *= profile [l][j] #profile[l][j] Wahrscheinlichkeit für Base an Stelle Index
                                   #Multiplikation der einzelnen Wahrscheinlichkeiten für k-mer
        if prob > maxprob:         #nur wenn Wahrscheinlichkeit k-mer höher/besser als vorhe
            maxprob =prob
            kmer = pattern
    return kmer   #Erstellen der ersten Consensus-Sequenz anhand der random
                  #ausgewählten k-mere


def profileForm(motifs):  
    k= len(motifs[0])  #Voraussetzung alle Motive gleich lang
    profile = [[1 for i in range(k)] for j in range(4)] #Erstellen der Profile-Matrix
    for index in motifs:
        for i in range(len(index)):
            j = SymbolToNumber(index[i])
            profile[j][i] +=1
    for index in profile:
        for i in range(len(index)):
            index[i] = index[i]/len(motifs)
    return profile


def consensus(profile):  #aus Profile wird Consensus-Sequenz erstellt
    str = ""
    for i in range(len(profile[0])): #für jede Position
        max = 0
        loc = 0
        for j in range(4):
            if profile[j][i] > max:
                loc = j
                max = profile[j][i]
        str+=NumberToSymbol(loc)
    return str  #consensus anhand der größten Wahrscheinlichkeit im Profile


def score(motifs):
    profile = profileForm(motifs)
    cons = consensus(profile)
    score = 0
    for index in motifs:
        for i in range(len(index)):
            if cons[i] != index[i]:
                score +=1
    return score


def randomMotifSearch(DNA, k, t): #nach den besten Motifs (zufällig) suchen
    bestMotifs = []
    motifs = []
    for index in range(t):
        random.seed()
        i= random.randint(0, len(DNA[index])-k) #zufällig wird die Startposition i gewählt
        motifs.append(DNA[index][i:i+k])
    bestMotifs = motifs.copy()
    count = 0
    while True:   #while schleife läuft solange, bis sich der score bzw. die Ausgabe nicht mehr verbessern
        profile = profileForm(motifs)
        for index in range(t):
            motifs[index] = profileProbable(DNA[index], k, profile)
        if score(motifs) < score(bestMotifs): #wenn der score der mMtifs, die aus Profile erstellt wurden,
                                              #kleiner ist als der score der bestMotifs (in erstem durchlauf die random kmere)
            bestMotifs = motifs.copy()        #neue Motifs als bestMotifs genommen und neues Profile erstellt
            count +=1
        else:
            print(count)
            return bestMotifs   #Ausgabe der Motive


dna=['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG','TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
dna2=["ACTTATATCTAGAGTAAAGCCCTGATTCCATTGACGCGATCCCTACCTCCATCATACTCCACAGGTTCTTCAATAGAACATGGGGAAAACTGAGGTACACCAGGTCTAACGGAGATTTCTGGCACTAACTACCCAAAATCGAGTGATTGAACTGACTTATATCTAGAGT",
    "AAAGCCCTGATTCCATTGACGCGATCCCTACCTCCATCATACTCCACAGGTTCTTCAATAGAACATGGGGAAAACTGAGGTACACCAGGTCTAACGGAGATTTCTGGCACTAACTACCCAAAATCCTCTCGATCACCGACGAGTGATTGAACTGACTTATATCTAGAGT",
    "CACTCCCGTCCGTCTGACGCCAGGTGCTCTACCCCGCTGATTGTCTGGTACATAGCAGCCTATAGATCACCGATGCAGAAACACTTCGAGGCAGCCGATTTCGCTTATCACAACGTGACGGAATTTGATAAACCACGTACTCTAATACCGTCACGGGCCCATCAACGAA",
    "ACAAGAACTGGTGGGGAGACTATGACACTCTAGCGGTCGCATAAGGGCCGGAAACCAGGACAAATCGATAAGATGAAGCGGGGATATAAGCCTTATACTGCGACTGGTTCCTTATATTATTTAGCCCCGATTGATCACCGATTAAAATATTCTGCGGTTTTCGAGACGG",
    "TAACCACACCTAAAATTTTTCTTGGTGAGATGGACCCCCGCCGTAAATATCAGGATTAAATGTACGGATACCCATGACCCTCCAGTCATCTACCTTCCCGTGGTGGTCGCTCAGCCTTGTGCAGACCGAACTAGCACCTGTCACATACAATGTTGCCCGCATAGATCGT",
    "ATCCGACAGAGGCAGTGAATAAGGTTTCGTTTCCTCAGAGAGTAGAACTGCGTGTGACCTTGCCTTCACCGACATCCGTTTCCAATTGAGCTTTTCAGGACGTTTAGGTAACTGATTGTCATTGCAATTGTCCGGGGGATTTAGATGGCCGGGTACCTCTCGGACTATA",
    "CCTTGTTGCCACCGATTCGCGAGCAACATCGGAGTGCTCTGATTCACGGCGATGCTCCACGAAGAGGACCGCGGCACGACACGCCCTGTACCTACGTTTCTGGATATCCTCCGGCGAGTTAATAGAGCAATACGACCTGGTCGTCGAGATCGTGTATCTAGCCCTACCT",
    "ATAGGTTAACGAATCAGGAGAGTTAATTTTACCTAGCTAGAGCGGACGGTGCCTGGCTGTATTCGCGTTTGACTTTCGGGCTCGCTGATAACTTGTGATCACCTTTTACGCTTACTGGATCCAACGATGGATCAAAGTTGAGAATTTCTGTGCCTTGGGTGTGAGCTGT",
    "CTGACGAAAGGACGGGCGGTGTACTTAGTTTGGGGTAAAATAGTTGGTATAATTCTGTGCGACAGACATTTGGTCAGGCCATACTGCCATATCGTGATGTAACTATCCACACTACGTCATAGGCCCTTGTGATCAATTAAACGTTCCTCATGCCAGGCTATCTGTTTAA",
    "GGCTTCGCGTTTAAGGCTGGATTAAGTACTCCGCCTTGTGATCTGTGATCCTCCGACCTGTGATCAGCAAGATTGGAACCTAGGTAGGCGGCGGGTCTACGCTGGCCCACAATCGTGAGTCCCCCACTCCGTAGGTTGTGGAATTTATAGACCCGCAAGGGGCACCACT",
    "AGGATGACACCCAGGATGAATCTGGATTAGGAACACCAACCCGACATATTTGTTACCGCTGCAGCATTTCGCTCTTGGACGCGTAACCCGAGATCCGTCTCGCGATCGTCACGGATCGGGATTATGCAGGCAATACCTTGTGATCACTCCGCGCTTGGTTTTGCTAGCG",
    "ACATCTCTAGTCACTTTTATTGAGCAGGTGGGCGGATTCATGATCCGGCTCTGTCGTACGTCCAACCACGGTGACATGTTCGGAGCTGTCGCCGTGGAGCAGAGATACATCGGATCTATCAATTTTACTAAGAGCAACTAGCCACGACAAACTGTGATCACCGATTGGA",
    "AATTTGCGTATCTCTAGGACTCCCTCATACAAATCAAAGCTTGGATGGGTAAGATGCCGCAGCAGCAGGTATCTCATATTGGCTATTAAGAGCCAGGCCCTATGGCCTTAGTATCACCGATCAGACGTCGCATGAGCGGGCCCGTTGTCCTATCTCTTTAGCTGCCGCA",
    "GAAGTAAAGGGGTTCCACTGCGTAGAGCGTGCCCCTCTGGTGTGCCGTACTGTTATGGTGATACAGCTTCCTTATACCCCTCGTAAAGCGGCTAATGGTCCTAATGAATGCCCTTGTGAAATCCGAATCGCTTTACAATTGCGTTCGGCGGAATGCAGTCACCAGTGTT",
    "TACACTACGCGTTATTTACTTTTACTGAGTCCTTGTCGCCACCGAACGAGGATTGTTCATTGTATCCGGAGATTAGGAGTTCGCATCGCTGACACAGCCAGTTCGTAGCAAATACCGCTGGCCCTGGGCACTCCAGATCAGAACTACTAGCCCTAAACTCTATGACACA",
    "TTGGGTCTCGATCCCTCTATGTTAAGCTGTTCCGTGGAGAATCTCCTGGGTTTTATGATTTGAATGACGAGAATTGGGAAGTCGGGATGTTGTGATCACCGCCGTTCGCTTTCATAAATGAACCCCTTTTTTTCAGCAGACGGTGGCCTTTCCCTTTCATCATTATACA",
    "TTTCAAGTTACTACCGCCCTCTAGCGATAGAACTGAGGCAAATCATACACCGTGATCACCGACCCATGGAGTTTGACTCAGATTTACACTTTTAGGGGAACATGTTTGTCGGTCAGAGGTGTCAATTATTAGCAGATATCCCCCAACGCAGCGAGAGAGCACGGAGTGA",
    "GATCCATTACCCTACGATATGTATATAGCGCCCTAGTACGGCTTCTCCCTTGCAGACACGCAGGCGCTGTGCGCTATCGGCTTCCTCGGACATTCCTGGATATAAGTAACGGCGAACTGGCTATCACTACCGCCGCTCCTTAAGCCTTGGTTTCACCGACGATTGTCGT", 
    "TAGTAGATTATTACCTGTGGACCGTTAGCTTCAAGACCGAAACGTTGGTGATGCTACTTAAATGTCAAGAGTTGCGAAGTTGGGCGAAGCACATCCGTACTCCCAAGTGGACGATCGATAGATCCATGGAGTTTCCATCCATCTTAATCCGCCCTTTGCATCACCGACG",
    "TACAAGGCACAAACGAGACCTGATCGAACGGTGCACGGTCGAGGCAGCGAGATAAATGTACATTGAGAGCACCTTGTGATTTACGACCTGCATCGAAGGTTTCTTGGCACCCACCTGTCGTCCGCCAGGGCAGAGCCGACATTATATGACGCTGATGTACGAAGCCCCT"]

k = 8
t = 5
best = randomMotifSearch(dna, k, t)
min = score(best)
for index in range(1000):  #randomizedMotifSearch wird in diesem Falle 1000 mal angesprochen
    print(index)
    a = randomMotifSearch(dna, k, t)
    if score(a) < score(best):
        best = a
        min = score(a)  
print(min)
for index in best:
    print(index) 
