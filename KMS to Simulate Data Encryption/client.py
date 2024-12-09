#!/usr/bin/python
#coding:utf-8
import sys
import requests
import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkkms.request.v20160120.DecryptRequest import DecryptRequest
from Crypto.Cipher import AES
from Crypto import Random
import base64
import os
from dotenv import load_dotenv

# Specify the absolute path to the .env file
load_dotenv('/root/config/.env')

accesskeyid = os.getenv('ACCESS_KEY_ID')
accesssecret = os.getenv('SECRET_ACCESS_KEY')
regionid = "me-east-1"

def aes256pad(s):
    #return s + (32 - len(s) % 32) * chr(32 - len(s) % 32)
    pad_len = 32 - (len(s) % 32)
    padding = bytes([pad_len] * pad_len)  # Ensure padding is in bytes
    return s + padding

def send(ciphertext, cipherdatakey):
    url = "http://47.91.120.127/sendEncryptedData" #replace with your ip public
    payload = {'ciphertext': ciphertext, 'cipherdatakey': cipherdatakey}
    headers = {}
    response = requests.post(url, headers=headers, data=payload)
    print(response.text)

if __name__ == "__main__":
    content = sys.argv[1].encode('utf-8')
    #content = sys.argv[1]
    cipherdatakey = sys.argv[2]

    clt = AcsClient(accesskeyid, accesssecret, regionid)
    decrequest = DecryptRequest()
    decrequest.set_CiphertextBlob(cipherdatakey)
    decrequest.set_accept_format("json")
    decrequest.set_protocol_type("https")

    decresp = clt.do_action_with_exception(decrequest)
    plaintext = json.loads(decresp)
    datakey = base64.b64decode(plaintext["Plaintext"])

    iv = Random.new().read(AES.block_size)
    cipher = AES.new(datakey, AES.MODE_CBC, iv)
    filedata = aes256pad(content)
    cipherfile = base64.b64encode(iv + cipher.encrypt(filedata))
    print("Encrypt text = ",cipherfile) 
    send(str(cipherfile, encoding="utf-8"), cipherdatakey)
    