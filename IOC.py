#Contains the code that will calculate the IOC to prove that the length of m = 7 matches
from collections import Counter
    
#Now we need to format the count of each of the characters to match the m-substring creation
def iocFormula():
    
    #Count the frequnecies of each of the letters
    cipherText = "LAVHEBSJMDINFGXCLWTUUWARWBQWFTEHWUDDTCAAKKTXTSMYALMVHTAHJHKICFAFZKLEXATXIXYMFVLVGUDALRFJTTGKXNLOYOWLVVVQAFKVGEZLEHEXHEZGPVZEDOWARZEAFSGVASOSDXJIEZESBEWTDWSFGVOPMUMJENPKWKMMCQKVXJMGZWVBEEWMQLARXGUNWLLWEDKKHCICAFLKFPOHWJTTGEEKLHKLEUJVTKEAESJXJYLFDSPVRFAJUXDINFAKLFQEFAEXJYNMTDXKSRQUGOVVTTWUHEXEZLGYVPEOLJHEMCOGEFLRIOSLBFRSRJGFKLEFWUAESLAYQIISVUVWKVZEZAFKVWPAFKXKSAOGMKKSRPWJHIHUXQSNKLODARXUAADJSGKMSEMWWSCARWVXIELVMVZVJODWPTDTLQESGPGOYEMGZGAFAGGJWEDNAVVWNAOWGTVYBLUXIXAUFUHDQUZAUTKMOZKTRUIFMMDMNMTTLZXBIYZWUXJWADQLHUICDQHMKLEOGEFLRIOSLBFRSEGDXCCIZLZXYENPKGYKLEQFVNJIRFZALRTPXAWLSSTTOZXEXHQVSMRMSUFEHKMOZGNXIILQULKFRIOFWMNSRWKGKRXRQKLHEENQDWVKVOZAUWVZIOWAYKLEOGEFLRIOSLBFRSBJGOZHEDAKLVVVQVOBKLAISJKRRTEWWDZRGFZGLVGOYEMGZGAFAGGJXHQHJHMMDQJUTEROFHJHMMDQLZXUETMTWVRYSQALARWDQKAZEIDFZWMVGHZGDHXCSGUZMYETULUTEROFTWTTGEEKWWSCAZQLAZVDBSJMPAEPGFHKLAHWSGPWIXNWKSYLXWLLRRDFZWWZWCGKKBFRSIALAZRTTWWQVGUFANXSVAZUZTIISFADEFRGAAFZNLIXWLAVVETSKGFXYQLTXVRAPWUBJMOZOZXKLEDLGLVIKXWYBJPAFAGGNIMGKLPFVKIALATSNSJWLJMNPMKMICAOSVXDMCEHJBMECKYJHLTSMFVHKLEDKLHTVARLSGRTPDGSVYXHMLSWUVEEKWLRPLAXLAVQUXLAICICAEHXKMNSUGGTIRZKLARXHMNWUVINFZWYFGUEGXLFQUOZVXSETQTMMNICMFSECEGDWWMYETIWOBCPNQWVHEKOUFYAFREELSGUMNRGJFVHPGTDBTHENSLXRFOGLZHNFEELLHGVOFWUMCMBQJLRRRDEWUNIMTKAFUFXHAMJERASMFVHLVTQUZGFPOSQ"
    for testKeyLength in [6, 7, 8]:
        print(f" Testing Key Length (m) = {testKeyLength}")
        ysubStrings = [""] * testKeyLength #Divdes the text based on key length
    
        #Now we can loop through and calculate each of the substrings and its
        #frequency count
        for i, char in enumerate(cipherText):
            stringIndex = i % testKeyLength
            ysubStrings[stringIndex] += char
    
        frequencyCount = []    
        for freq in ysubStrings:
            charCounts = Counter(freq)
            frequencyCount.append(charCounts)
    
        #Now bridge together with IOC calculation of each substring
        iocSub = 0.0
        for index, counts in enumerate(frequencyCount):
            nLength = sum(counts.values())
            
            top = sum(count * (count - 1) for count in counts.values())
            bottom = (nLength * (nLength - 1))
            #Formula taken from slides to calculate substring ioc
            
            iocValue = (top / bottom)
            iocSub += iocValue
            print(f"  y{index + 1} IOC = {iocValue:.4f}")
            
        #Displays overall ioc calculation for entire sequence at key length    
        iocAverage = iocSub / testKeyLength
        print(f"Calculated IOC is {iocAverage:.3f} for m = {testKeyLength}")

# Part 2
#Ciphertext used
CIPHER_TEXT = "LAVHEBSJMDINFGXCLWTUUWARWBQWFTEHWUDDTCAAKKTXTSMYALMVHTAHJHKICFAFZKLEXATXIXYMFVLVGUDALRFJTTGKXNLOYOWLVVVQAFKVGEZLEHEXHEZGPVZEDOWARZEAFSGVASOSDXJIEZESBEWTDWSFGVOPMUMJENPKWKMMCQKVXJMGZWVBEEWMQLARXGUNWLLWEDKKHCICAFLKFPOHWJTTGEEKLHKLEUJVTKEAESJXJYLFDSPVRFAJUXDINFAKLFQEFAEXJYNMTDXKSRQUGOVVTTWUHEXEZLGYVPEOLJHEMCOGEFLRIOSLBFRSRJGFKLEFWUAESLAYQIISVUVWKVZEZAFKVWPAFKXKSAOGMKKSRPWJHIHUXQSNKLODARXUAADJSGKMSEMWWSCARWVXIELVMVZVJODWPTDTLQESGPGOYEMGZGAFAGGJWEDNAVVWNAOWGTVYBLUXIXAUFUHDQUZAUTKMOZKTRUIFMMDMNMTTLZXBIYZWUXJWADQLHUICDQHMKLEOGEFLRIOSLBFRSEGDXCCIZLZXYENPKGYKLEQFVNJIRFZALRTPXAWLSSTTOZXEXHQVSMRMSUFEHKMOZGNXIILQULKFRIOFWMNSRWKGKRXRQKLHEENQDWVKVOZAUWVZIOWAYKLEOGEFLRIOSLBFRSBJGOZHEDAKLVVVQVOBKLAISJKRRTEWWDZRGFZGLVGOYEMGZGAFAGGJXHQHJHMMDQJUTEROFHJHMMDQLZXUETMTWVRYSQALARWDQKAZEIDFZWMVGHZGDHXCSGUZMYETULUTEROFTWTTGEEKWWSCAZQLAZVDBSJMPAEPGFHKLAHWSGPWIXNWKSYLXWLLRRDFZWWZWCGKKBFRSIALAZRTTWWQVGUFANXSVAZUZTIISFADEFRGAAFZNLIXWLAVVETSKGFXYQLTXVRAPWUBJMOZOZXKLEDLGLVIKXWYBJPAFAGGNIMGKLPFVKIALATSNSJWLJMNPMKMICAOSVXDMCEHJBMECKYJHLTSMFVHKLEDKLHTVARLSGRTPDGSVYXHMLSWUVEEKWLRPLAXLAVQUXLAICICAEHXKMNSUGGTIRZKLARXHMNWUVINFZWYFGUEGXLFQUOZVXSETQTMMNICMFSECEGDWWMYETIWOBCPNQWVHEKOUFYAFREELSGUMNRGJFVHPGTDBTHENSLXRFOGLZHNFEELLHGVOFWUMCMBQJLRRRDEWUNIMTKAFUFXHAMJERASMFVHLVTQUZGFPOSQ"

#Standard English letter frequencies p0..p25
ENGLISH_FREQ = [
    0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070,
    0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 0.060,
    0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001,
]
#keyword length (confirmed in part 1)
M = 7


#Split the ciphertext into m substrings y1, ..., ym where yi contains
#every mth letter of the ciphertext starting at position i
def splitIntoSubstrings(cipherText, m):
    return [cipherText[i::m] for i in range(m)]


#Build the frequency count f0..f25 (A..Z) for a substring.
def letterCounts(substring):
    counts = [0] * 26
    for ch in substring:
        counts[ord(ch) - ord('A')] += 1
    return counts


#vg is the frequency-count vector cyclically shifted g steps
#vg[j] = counts[(j + g) mod 26]
def shiftedVector(counts, g):
    return counts[g:] + counts[:g]


#Mg = p (dot) vg, normalized by the substring length N, for g = 0..25.
def computeMgValues(substring):
    counts = letterCounts(substring)
    n = len(substring)
    mgValues = []
    for g in range(26):
        vg = shiftedVector(counts, g)
        dot = sum(p * c for p, c in zip(ENGLISH_FREQ, vg)) / n
        mgValues.append(dot)
    return mgValues


#Prints the table with one column per substring (g = 0..25 as rows)
def printTable(allMgValues):
    header = "g".rjust(4) + "".join(f"y{i+1}".rjust(10) for i in range(len(allMgValues)))
    print(header)
    for g in range(26):
        row = str(g).rjust(4)
        for mgValues in allMgValues:
            row += f"{mgValues[g]:10.4f}"
        print(row)
    print()


#The shift that maximizes Mg in each column is our guess for ki
def findKeyShifts(allMgValues):
    return [mgValues.index(max(mgValues)) for mgValues in allMgValues]


#Converts the numeric key shifts into the keyword string
def shiftsToKeyword(shifts):
    return "".join(chr(k + ord('A')) for k in shifts)


#Quick raw decrypt, this will be used to confirm the key word
def decryptPreview(cipherText, shifts):
    m = len(shifts)
    plain = []
    for i, ch in enumerate(cipherText):
        k = shifts[i % m]
        p = (ord(ch) - ord('A') - k) % 26
        plain.append(chr(p + ord('A')))
    return "".join(plain)


#Runs the full Part 2 table + keyword recovery process
def table():
    substrings = splitIntoSubstrings(CIPHER_TEXT, M)

    allMgValues = [computeMgValues(s) for s in substrings]

    print(f"Table of Mg values (m = {M}):\n")
    printTable(allMgValues)

    shifts = findKeyShifts(allMgValues)
    keyword = shiftsToKeyword(shifts)

    print(f"Key shifts (k1..k{M}): {shifts}")
    print(f"Keyword: {keyword}")
    print()
    print("Decryption preview (first 120 letters):")
    print(decryptPreview(CIPHER_TEXT, shifts)[:120])


if __name__ == "__main__":
    iocFormula()
    table()