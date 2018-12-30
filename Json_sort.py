
import sys, json;
data = json.load(sys.stdin)

output1 = []

for i in data['report']:
    for j in i['subject']:
        output1.append(j['code'] + ' ' + j["grade"] + ' ' + i['enrollment'] + ' ' + i['name'])
        

output1 = sorted(output1)

str1 = '\n'.join(output1)

print(str1)