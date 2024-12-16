# Structure of AES lab
# first we are converting bytes to matrix and than matrix to bytes then 
# we are converting matrix into 2 bytes and then decoding it in string to get answer #

def bytes2matrix(text):
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    out = []
    for r in matrix:
        for c in r:
            out.append(c.to_bytes(2,byteorder='little').decode())
    return ''.join(out)

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix))