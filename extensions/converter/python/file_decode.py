import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# 配置密钥和IV（根据实际加密参数修改）
key = b"1234567890123456"  # 16字节AES密钥
iv = b"1234567890123456"   # 16字节IV
# 输入输出路径需要和自定义编解码器中的配置保持一致，且输入固定为redis-fx.input 输出固定为redis-fx.output
io_dir = r'E:\test\decode'
with open(os.path.join(io_dir, 'redis-fx.input'), "rb") as f:
    # 从文件读取二进制数据
    data = f.read()

# AES解密
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
decryptor = cipher.decryptor()
decrypted = decryptor.update(data) + decryptor.finalize()

# 将二进制数据写入文件
with open(os.path.join(io_dir, 'redis-fx.output'), "wb") as f:
    f.write(decrypted)



