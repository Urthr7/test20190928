def nabeatsu(num):
    for i in num:
        if i % 3 == 0:
            num[i] = 'アホ'
        elif i in 3:
            num[i] = 'アホ'
    return num

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

result = nabeatsu(num)

print(result)