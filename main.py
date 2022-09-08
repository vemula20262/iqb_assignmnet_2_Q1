
sequence = "SGFRKMAFPSGKVEGCMVQVTCGTTTLNGLWLDDTVYCPRHVICTAEDMLNPNYEDLLIRKSNHSFLVQAGNVQLRVIGHSMQNCLLRLKVDTSNPKTPKYKFVRIQPGQTFSVLACYNGSPSGVYQCAMRPNHTIKGSFLNGSCGSVGF"
length = len(sequence)
ex_helix = {'E': 1.53,
            'A': 1.45,
            'L': 1.34,
            'H': 1.24,
            'M': 1.20,
            'Q': 1.17,
            'W': 1.14,
            'V': 1.14,
            'F': 1.12,
            'K': 1.07,
            'I': 1.00,
            'D': 0.98,
            'T': 0.82,
            'S': 0.79,
            'R': 0.79,
            'C': 0.77,
            'N': 0.73,
            'Y': 0.61,
            'P': 0.59,
            'G': 0.53}
ex_beta = {'M': 1.67,
           'V': 1.65,
           'I': 1.60,
           'C': 1.30,
           'Y': 1.29,
           'F': 1.28,
           'Q': 1.23,
           'L': 1.22,
           'T': 1.20,
           'W': 1.19,
           'A': 0.97,
           'R': 0.90,
           'G': 0.81,
           'D': 0.80,
           'K': 0.74,
           'S': 0.72,
           'H': 0.71,
           'N': 0.65,
           'P': 0.62,
           'E': 0.26}
helix = ""
beta = ""
for i  in range(0,length):
    helix = "-"+helix

for i in range(0,length-5):
    count = 0
    for j in range(i,i+6):
        if ex_helix[sequence[j]] >= 1:
            count +=1
    if count>=4:
        helix = helix[0:i]+"HHHHHH"+helix[i+6:]
    while (i+6)<length:
        total = 0
        for k in range(i+3,i+7):
            total +=ex_helix[sequence[k]]
        if total >=4:
            helix = helix[:i+6]+"H"+helix[i+7:]
        else :
            break
    while i-1>=0:
        total = 0
        for k in range(i-1,i+3):
            total += ex_helix[sequence[k]]
        if total >=4:
            helix = helix[:i-1]+"H"+helix[i:]
        else :
            break
print (helix)





