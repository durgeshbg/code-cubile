twttr = input('Input: ')
output = ''

for c in twttr:
    if c.lower() in ['a','e','i','o','u']:
        continue
    else:
        output += c

print(f'Output: {output}')