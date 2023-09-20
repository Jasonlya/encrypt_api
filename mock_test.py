from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests
import json
import base64

# 密钥（key）需要是16字节长
key = b"your_secret_key6"

# 创建一个AES加密器
cipher_suite = AES.new(key, AES.MODE_ECB)

data={"num1": "1", "num2": "1"}
# encrypt_data = cipher_suite.encrypt(pad(json.dumps(data).encode(), AES.block_size))
# 定义加密的 JSON 字符串
encrypt_data = cipher_suite.encrypt(pad(json.dumps(data).encode(), AES.block_size))
# print(encrypt_data)
#requests.post方法中的data参数需要是一个字典、元组或字节流。加密的字节流需要转化成base64编码进行请求
encoded_data = base64.b64encode(encrypt_data).decode()
# print(encoded_data)
# # 解密 JSON 字符串
# decipher_suite = AES.new(key, AES.MODE_ECB)
# decrypt_data = unpad(decipher_suite.decrypt(encrypt_data), AES.block_size)

# # 将解密后的 JSON 字符串转换为 Python 对象
# data = json.loads(decrypt_data.decode())
# print(data)

# 发送请求并打印响应结果
response = requests.post('http://192.168.0.102:5000/api/add', headers={'Content-Type': 'application/json'}, json=json.dumps({"data": encoded_data}))
print(response.status_code)