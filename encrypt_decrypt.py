from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

class encrypt_decrypt:

    def __init__(self, file):
        self.file = file
        self.ciphertext = ""
        self.decrypted_data = ""

    def en(self):
        key = get_random_bytes(16)  
        iv = get_random_bytes(16)   

        cipher = AES.new(key, AES.MODE_CBC, iv)

        data = self.file.encode('utf-8')

        padded_data = pad(data, AES.block_size)

        self.ciphertext = cipher.encrypt(padded_data)

        cipher_dec = AES.new(key, AES.MODE_CBC, iv)
        decrypted_padded_data = cipher_dec.decrypt(self.ciphertext)

        self.decrypted_data = unpad(decrypted_padded_data, AES.block_size)

    def de(self):
        return self.decrypted_data.decode('utf-8')
    
    def output_encrypt(self):
        return self.ciphertext

