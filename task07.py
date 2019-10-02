line = """We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be
 (Football Coach)
"""

l_line = line.split()

print("Слов в тексте:", len(line.split()))

a = ''
for i in range(len(l_line)):
    a1 = str(l_line[i]).strip(',')
    a2 = a1.strip('!')
    a1 = a2.strip('.')
    a2 = a1.strip('(')
    a1 = a2.strip(')')
    a = a + a1 + " "
a = a.strip()

print("Удаляю знаки препинания в списке слов:", a)
l = list(a.split())
l.sort(key=str.lower)
print("Вывожу слова в алфавитном порядке:", l)

d = {}
for i in l:
    d.setdefault(i.lower(), 0)
    d[i.lower()] = d[i.lower()] + 1

print(d)
