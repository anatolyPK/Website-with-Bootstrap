word = input()

buff = []
for symb in word:
    if symb in 'eyuioa':
        buff.append(symb)

for ind in range(len(word)):
    if word[ind] in 'eyuioa':
        word = word[:ind] + buff.pop() + word[ind+1:]

print(word)