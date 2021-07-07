# left shift rotate
def rotate(l, n):
    return l[n:] + l[:n]


# key generate
externalKey = open('pass.txt', 'r').read()
result = []

for i in range(len(externalKey)):
    bits = bin(ord(externalKey[i]))[2:]
    bits = '00000000'[len(bits):] + bits
    result.extend([int(b) for b in bits])

PC1 = [ 57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

PC2 = [ 14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

round = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

nresult = []
Key = []

for i in range(len(PC1)):
    nresult.append(result[PC1[i]-1])

C, D = nresult[:23], nresult[23:]

for i in range(len(round)):
    C, D = rotate(C, round[i]), rotate(D, round[i])
    Ki = C + D
    aur = []
    for j in range(len(PC2)):
        aur.append(Ki[PC2[j]-1])
    Key.append(aur)

for i in range(len(Key)):
    print("Key", i, " =", Key[i])