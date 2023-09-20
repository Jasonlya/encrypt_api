# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/20 22:56
@Auth ： liangya
@File ：mock_test2.py
"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests
import base64
import json

# 加密前的数据
data_to_encrypt = {
    "num1": 42,
    "num2": 23
}

# 将数据转换为 JSON 格式的字符串
json_data = json.dumps(data_to_encrypt)

# 加密数据
def encrypt_data(data):
    # 密钥（key）需要是16字节长
    key = b"your_secret_key6"
    cipher_suite = AES.new(key, AES.MODE_ECB)
    # 使用 AES 加密并进行填充
    encrypted_data = cipher_suite.encrypt(pad(data.encode(), AES.block_size))
    # 将加密数据进行 Base64 编码
    return base64.b64encode(encrypted_data).decode('utf-8')

# 加密 JSON 数据
encrypted_data = encrypt_data(json_data)

# 构建请求头
headers = {'Content-Type': 'application/json'}

# 构建请求体
payload = {
    'data': encrypted_data
}

# 发送 POST 请求到服务器
url = 'http://192.168.0.102:5000/api/add'
response = requests.post(url, headers=headers, json=payload)
print(response.text)

# 检查响应
# if response.status_code == 200:
#     decrypted_data = response.json()
#     print(f"加密前的数据: {data_to_encrypt}")
#     print(f"解密后的数据: {decrypted_data}")
# else:
#     print(f"请求失败，状态码: {response.status_code}")
