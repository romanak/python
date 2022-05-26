s = 'azcbobobegghakl'
count = 0
for char in s:
    if char in 'aeiou':
        count += 1
print('Number of vowels:', count)