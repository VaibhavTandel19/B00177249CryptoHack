#we are directly sending encrypt a flag using AES and we get cipher text
# then we are sending another request to decrypt ciphertext which we got which gives us a hex and 
# then we can convert it into plaintext

import requests

url = "https://aes.cryptohack.org/block_cipher_starter/"
ciphertext = requests.get(url + "encrypt_flag/").json()["ciphertext"]
plaintext_hex = requests.get(url + "decrypt/" + ciphertext ).json().get("plaintext")

print(bytes.fromhex(plaintext_hex).decode())