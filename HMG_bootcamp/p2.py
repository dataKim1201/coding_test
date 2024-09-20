# 복호화

import sys
input = sys.stdin.readline
cmd = input().split()
# ord() - 97
def encoding(key):
    return list(map(lambda x: ord(x) -97,key))
def decoding(key):
    return ''.join(map(lambda x: chr(x + 97),key))
def encrypt(cmd):
    c, s_key, rotate, message = cmd
    encoded_s_key = encoding(s_key)
    encoded_message = encoding(message)
    encoded_m = list(map(lambda x,y: (x + y)%26, encoded_s_key, encoded_message))
    
    if abs(eval(rotate)) == 0:
        return encoded_m
    elif abs(eval(rotate)) == 1:
        return encoded_m[1:] + [encoded_m[0]]
    else:
        r = eval(rotate)
        return encoded_m[r:] + encoded_m[:r]
    
def decrypt(cmd):
    c, s_key, rotate, message = cmd
    # 역순으로 진행
    decoded_message = encoding(message)
    encoded_s_key = encoding(s_key)
    r = eval(rotate)
    if abs(eval(rotate)) == 0:
        encoded_m = list(map(lambda x,y: (y-x)%26, encoded_s_key, decoded_message))
        return encoded_m
    elif abs(eval(rotate)) == 1:
        DM = decoded_message[1:] + [decoded_message[0]]
    if r < 0:
        DM = decoded_message[-r:] + decoded_message[:-r]
    else:
        DM = decoded_message[-r:] + decoded_message[:-r]
    encoded_m = list(map(lambda x,y: (y-x)%26, encoded_s_key, DM))
    return encoded_m
    
# cmd = 'encrypt secretword 1 helloworld'.split()
if cmd[0] == 'encrypt':
    print(decoding(encrypt(cmd)))
else:
    print(decoding(decrypt(cmd)))

# cmd = 'decrypt secretword 1 incspkfcgz'.split()
# if cmd[0] == 'encrypt':
#     print(decoding(encrypt(cmd)))
# else:
#     print(decoding(decrypt(cmd)))