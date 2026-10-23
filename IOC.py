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
        
    #Now we want to added the total count together
    totalSum = sum(number for letter, number in totalAmount)
    
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
    iocCalculation = sum (frequencyCount * (frequencyCount - 1) / (totalSum * (totalSum - 1)))
    print(iocCalculation)

#Generates the columns to represent the key length (can be changed with whatever key length is defined)
def table():
    #Stuff

#Will decrypt the plain text
    
if __name__ == "__main__":
    iocFormula()
    table()