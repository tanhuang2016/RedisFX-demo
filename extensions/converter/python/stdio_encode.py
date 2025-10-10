import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# 配置密钥和IV（与解密脚本保持一致）
key = b"1234567890123456"  # 16字节AES密钥
iv = b"1234567890123456"   # 16字节IV

# 从stdin读取明文数据
plaintext = sys.stdin.buffer.read()

# PKCS7填充
padding_length = 16 - (len(plaintext) % 16)
plaintext += bytes([padding_length] * padding_length)

# AES加密
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher.encryptor()
encrypted = encryptor.update(plaintext) + encryptor.finalize()

# 通过stdout输出加密结果
sys.stdout.buffer.write(encrypted)
sys.stdout.flush()
