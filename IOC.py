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
    
if __name__ == "__main__":
    iocFormula()