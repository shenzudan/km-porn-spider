from Crypto.Cipher import AES
#self
import constant as const

AES_SECRET_KEY = const.AES_KEY  # 此处16|24|32个字符

IV = const.AES_IV

# padding算法
BS = len(AES_SECRET_KEY)
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]


class AES_ENCRYPT(object):
    def __init__(self):
        self.key = AES_SECRET_KEY
        self.mode = AES.MODE_CBC

    # 加密函数
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, IV)
        # v = pad(text).encode("UTF-8")
        v = pad(text).encode("UTF-8")
        self.ciphertext = cryptor.encrypt(v)
        # AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题，使用base64编码
        bs = self.ciphertext
        return ''.join(['%02X ' % b for b in bs]).replace(' ', '')

    # 解密函数
    def decrypt(self, text):
        decode = bytes.fromhex(text)
        cryptor = AES.new(self.key, self.mode, IV)
        plain_text = cryptor.decrypt(decode)
        msg = plain_text
        padding_len = msg[len(msg) - 1]

        return msg[0:-padding_len].decode("UTF-8")
