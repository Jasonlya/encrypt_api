from flask import Flask, request, jsonify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import json

app = Flask(__name__)

# 密钥（key）需要是16字节长
key = b"your_secret_key6"

# 创建一个AES加密器
cipher_suite = AES.new(key, AES.MODE_ECB)

# # 创建一个AES解密器
# decipher_suite = AES.new(key,AES.MODE_ECB)

@app.route('/api/add', methods=['POST'])
def add_numbers():
    encrypt_data = request.data
    print(encrypt_data)
    # base = base64.b64encode(encrypt_data).decode('utf-8')
    # print(base)
    decipher_suite = AES.new(key, AES.MODE_ECB)
    decrypt_data = unpad(decipher_suite.decrypt(encrypt_data), AES.block_size)
    # print(decrypt_data)
    data = json.loads(decrypt_data.decode())
    # print(data)
    # data2 = json.dumps(data)
    # print(data['num1'])
    # print(data2)
    #加密
    # num1 = cipher_suite.encrypt(pad(data['num1'].encode(), AES.block_size))
    # num2 = cipher_suite.encrypt(pad(data['num2'].encode(), AES.block_size))
    #解密
    # num1 = cipher_suite.decrypt(data['num1'].encode())
    # num1 = unpad(cipher_suite.decrypt(base64.b64decode(data['num1'])), AES.block_size)
    # #num1 解密后为二进制数据，需要转换
    # num1 = int(num1.decode('utf-8'), 2)
    # num2 = cipher_suite.decrypt(data['num2'].encode())
    # num2 = unpad(cipher_suite.decrypt(base64.b64decode(data['num2'])), AES.block_size)
    # # num1 解密后为二进制数据，需要转换
    # num2 = int(num2.decode('utf-8'), 2)
    result = data['num1']+data['num2']

    response = {'data':{'num': {'num1':data['num1'],'num2':data['num2']},'result':result}}
    return jsonify(response)
###大啊啊

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    plaintext = data['plaintext']
    ciphertext = cipher_suite.encrypt(pad(plaintext.encode(), AES.block_size))
    response = {'ciphertext': base64.b64encode(ciphertext).decode()}
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
