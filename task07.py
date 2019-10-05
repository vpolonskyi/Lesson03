line = """We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be
 (Football Coach)
 Smile:-)
 bbe, bbe.
"""

print(line)

l_line = line.split()

print("Слов в тексте:", len(line.split()))

for i in l_line:
    a = str(l_line[l_line.index(i)])
    a = a.strip("-,!.():; ")
    l_line[l_line.index(i)] = a

print("Удаляю знаки препинания в списке слов:", l_line)

l_line.sort(key=str.lower)
print("Вывожу слова в алфавитном порядке:", l_line)

d = {}
for i in l_line:
    d.setdefault(i.lower(), 0)
    d[i.lower()] = d[i.lower()] + 1

print(d)
