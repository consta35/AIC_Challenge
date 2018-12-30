
n = input()
def Brackets(n):
    lefts =0
    rights = 0
    lbracks = ['[','(', '{']
    rbracks = [']',')','}']
    ans = ""
    bracks = ""
    total = ""
    for i in n:
        if i in lbracks or i in rbracks:
            bracks +=i
    for i in n:
        if i in lbracks:
            lefts += 1
        if i in rbracks:
            rights += 1
    if rights == lefts:
        ans = 'Y' 
    else:
        ans = 'N'
    total = ''.join(map(str, ans)) + ' ' + ''.join(map(str, bracks))
    return total


print (Brackets(n))