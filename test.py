from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import json

# 密钥（key）需要是16字节长
key = b"your_secret_key6"

# 创建一个AES加密器
cipher_suite = AES.new(key, AES.MODE_ECB)

data={"num1": "1", "num2": "1"}
# encrypt_data = cipher_suite.encrypt(pad(json.dumps(data).encode(), AES.block_size))
encrypt_data = cipher_suite.encrypt(pad(json.dumps(data).encode(), AES.block_size))
print(encrypt_data)

#解密
decipher_suite = AES.new(key, AES.MODE_ECB)
decrypt_data = unpad(decipher_suite.decrypt(encrypt_data), AES.block_size)
print(decrypt_data)
data = json.loads(decrypt_data.decode())
print(data)
# data2 = json.dumps(data)
print(data['num1'])
# 加密
# num1 = cipher_suite.encrypt(pad(data['num1'].encode(), AES.block_size))
# num2 = cipher_suite.encrypt(pad(data['num2'].encode(), AES.block_size))