import hashlib

secret = 'ckczppom'

result = 1
found = False

n = 5

while not found:
    res = hashlib.md5((secret+str(result)).encode()).hexdigest()
    if res[:n] == '0'*n:
        found = True
    else:
        result += 1

print(f'Result: {result}')