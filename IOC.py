#Contains the code that will calculate the IOC to prove that the length of m = 7 matches
from collections import Counter
    
#Now we need to format the count of each of the characters to match the m-substring creation
def iocFormula():
    
    #Count the frequnecies of each of the letters
    cipherText = "LAVHEBSJMDINFGXCLWTUUWARWBQWFTEHWUDDTCAAKKTXTSMYALMVHTAHJHKICFAFZKLEXATXIXYMFVLVGUDALRFJTTGKXNLOYOWLVVVQAFKVGEZLEHEXHEZGPVZEDOWARZEAFSGVASOSDXJIEZESBEWTDWSFGVOPMUMJENPKWKMMCQKVXJMGZWVBEEWMQLARXGUNWLLWEDKKHCICAFLKFPOHWJTTGEEKLHKLEUJVTKEAESJXJYLFDSPVRFAJUXDINFAKLFQEFAEXJYNMTDXKSRQUGOVVTTWUHEXEZLGYVPEOLJHEMCOGEFLRIOSLBFRSRJGFKLEFWUAESLAYQIISVUVWKVZEZAFKVWPAFKXKSAOGMKKSRPWJHIHUXQSNKLODARXUAADJSGKMSEMWWSCARWVXIELVMVZVJODWPTDTLQESGPGOYEMGZGAFAGGJWEDNAVVWNAOWGTVYBLUXIXAUFUHDQUZAUTKMOZKTRUIFMMDMNMTTLZXBIYZWUXJWADQLHUICDQHMKLEOGEFLRIOSLBFRSEGDXCCIZLZXYENPKGYKLEQFVNJIRFZALRTPXAWLSSTTOZXEXHQVSMRMSUFEHKMOZGNXIILQULKFRIOFWMNSRWKGKRXRQKLHEENQDWVKVOZAUWVZIOWAYKLEOGEFLRIOSLBFRSBJGOZHEDAKLVVVQVOBKLAISJKRRTEWWDZRGFZGLVGOYEMGZGAFAGGJXHQHJHMMDQJUTEROFHJHMMDQLZXUETMTWVRYSQALARWDQKAZEIDFZWMVGHZGDHXCSGUZMYETULUTEROFTWTTGEEKWWSCAZQLAZVDBSJMPAEPGFHKLAHWSGPWIXNWKSYLXWLLRRDFZWWZWCGKKBFRSIALAZRTTWWQVGUFANXSVAZUZTIISFADEFRGAAFZNLIXWLAVVETSKGFXYQLTXVRAPWUBJMOZOZXKLEDLGLVIKXWYBJPAFAGGNIMGKLPFVKIALATSNSJWLJMNPMKMICAOSVXDMCEHJBMECKYJHLTSMFVHKLEDKLHTVARLSGRTPDGSVYXHMLSWUVEEKWLRPLAXLAVQUXLAICICAEHXKMNSUGGTIRZKLARXHMNWUVINFZWYFGUEGXLFQUOZVXSETQTMMNICMFSECEGDWWMYETIWOBCPNQWVHEKOUFYAFREELSGUMNRGJFVHPGTDBTHENSLXRFOGLZHNFEELLHGVOFWUMCMBQJLRRRDEWUNIMTKAFUFXHAMJERASMFVHLVTQUZGFPOSQ"
    letterFreq = Counter(cipherText)
    totalAmount = []

    #Append that count to a totalAmount array
    for char, count in letterFreq.items():
        totalAmount.append((char, count))
    
    #Aftewards we can create a loop that can calculate the IOC
    testKeyLength = int(input("Please input the keylength: "))
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
    
    #Now bridge together with IOC calculation
    iocCalculation = 0.0
    for counts in frequencyCount:
        nLength = sum(counts.values())
        #Formula taken from slides
        top = sum(count * (count - 1) for count in counts.values())
        bottom = (nLength * (nLength - 1))
        iocCalculation += (top / bottom)
        
    iocAverage = iocCalculation / testKeyLength
    print(f"Calculated IOC is {iocAverage:.3f}")
    
if __name__ == "__main__":
    iocFormula()