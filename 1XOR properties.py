#This is Crypto hack lab XOR properties Lab 
#We used XOR properties like  which is mentioned in the exercies 
#the first step was to find all the keys and their hex value as we wanted to find we need individual keys 
# so we can use xor to get original flag in its bytes form as it was mentioned.

key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key1_bytes = bytes.fromhex(key1)

key12 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key12_bytes = bytes.fromhex(key12)

#for i in key1_bytes:
    #for j in key12_bytes:

#key2 = hex(int(key1, 16) ^ int(key12, 16))
key23 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
key2 = "0x911404e13f94884eabbec925851240a52fa381ddb79700dd6d0d"

key3 = hex(int(key2, 16) ^ int(key23, 16))
#print(key3)

key3 = "0x504053b757eafd3d709d6339b140e03d98b9fe62b84add0332cc"
keyflag123 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

#flag = hex(int(key1, 16) ^ int(key2, 16) ^ int(key3, 16) )
flag = "0x679ce12554e557ada0e38f2e52f126e54240b2576c83c4196cd2"

#mainflag= hex(int(key1, 16) ^ int(key2, 16) ^ int(key3, 16) ^ int(keyflag123, 16) )

mainflag = "0x63727970746f7b7830725f69355f61737330633161743176337d"

print(bytes.fromhex(str(mainflag)[2:]))

#crypto{x0r_i5_ass0c1at1v3}'