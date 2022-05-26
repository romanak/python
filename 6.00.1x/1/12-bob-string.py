s = 'azcbobobegghaklbob'
count = 0
for i in range(len(s)-2):
    if 'bob' == s[i:i+3]:
        count += 1
print('Number of times bob occurs is:', count)