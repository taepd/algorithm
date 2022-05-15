s = '2014.07.15'
date = s.split('.')

for i, c in enumerate(date[::-1]):
    print(c, end='-') if i != len(date)-1 else print(c)