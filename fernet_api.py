from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import base64

app = Flask(__name__)

"""
    Fernet加密是一个对称加密算法，这意味着加密和解密使用的是同一把密钥
"""
# 密钥（key）和初始化向量（iv）需要是16字节长
key = b"your_secret_key"
iv = b"your_secret_iv123"
cipher_suite = Fernet(base64.urlsafe_b64encode(key + iv))

@app.route('/api/add', methods=['POST'])
def add_numbers():
    # 解密请求数据
    data = request.get_json()
    num1 = cipher_suite.decrypt(data['num1'].encode()).decode()
    num2 = cipher_suite.decrypt(data['num2'].encode()).decode()

    result = num1 + num2

    # 加密响应数据
    # response = {'result': cipher_suite.encrypt(result.encode()).decode()}
    #不加密响应数据
    response = {'result':{'data': result}}
    return jsonify(response)

#生成加密的字段
@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    plaintext = data['plaintext']
    ciphertext = cipher_suite.encrypt(plaintext.encode())
    response = {'ciphertext': ciphertext.decode()}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)