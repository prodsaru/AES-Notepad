from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

class encrypt_decrypt:

    def en(file):
        key = get_random_bytes(16)  
        iv = get_random_bytes(16)   
        Keybook().add(file, key, iv)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        data = file.encode('utf-8')
        padded_data = pad(data, AES.block_size)
        ciphertext = cipher.encrypt(padded_data)
        return ciphertext
    
    def de(ciphertext, filename):
        key_iv = Keybook().get(filename)
        key = key_iv[0]
        iv = key_iv[1]
        cipher_dec = AES.new(key, AES.MODE_CBC, iv)
        decrypted_padded_data = cipher_dec.decrypt(ciphertext)
        decrypted_data = unpad(decrypted_padded_data, AES.block_size)
        return decrypted_data.decode('utf-8')
