## read in data from input file
data = []
with open("input001.txt") as f:
    for line in f:
        data.append(line)

datac = []
for i in data:
     datac.append(i.strip())

hash_id = []
for i in datac:
    hash_id.append(abs(hash(i)))

def encode(num):
    ans = []    
    characters ="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
    base = len(characters)
    ret = []
    val = []
    while num > 0 and len(ret)<6:
        val = num % base
        ret.append(characters[val])
        num = num // base
    ans += "http://sprng.brd/",''.join(set(ret[::-1]))
    return ''.join(ans)

for i in hash_id:
    print(encode(i))