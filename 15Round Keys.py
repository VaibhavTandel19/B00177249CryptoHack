# Round Keys lab
#we are having 2 matrices state and round key and we are doing XOR between their elements 
# then we are converting it in to bytes to get the answer#

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    out = []
    for i in range(len(s)):
        for j in range(len(s[i])):
            out.append(s[i][j] ^ k[i][j])
    return out

def matrix2bytes(matrix):
    out = []
    for r in matrix:
        out.append(r.to_bytes(2,byteorder='little').decode())
    return ''.join(out)

print(matrix2bytes(add_round_key(state, round_key)))