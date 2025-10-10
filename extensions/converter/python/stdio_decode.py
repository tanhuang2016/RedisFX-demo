import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# 配置密钥和IV（根据实际加密参数修改）
key = b"1234567890123456"  # 16字节AES密钥
iv = b"1234567890123456"   # 16字节IV

# 直接从stdin读取二进制数据
data = sys.stdin.buffer.read()

# AES解密
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
decryptor = cipher.decryptor()
decrypted = decryptor.update(data) + decryptor.finalize()

# 直接通过stdout输出二进制结果
sys.stdout.buffer.write(decrypted)
sys.stdout.flush()
