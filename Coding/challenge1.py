import hashlib
import sys

dict_file = open('dictionary.txt', 'r')
names_file = open('rawnames.txt', 'r')

dict = []
names = []

for d in dict_file:
    dict.append(d.lower()[:-1])
dict_file.close()

print("Loaded Dictionary...")

for n in names_file:
    name = str()
    index = 0
    while(n[index] != " "):
        name += n[index]
        index += 1
    names.append(name[:1] + name[1:].lower())
names_file.close()

print("Loaded Names...")

hash = b"\xfd{eZ'~\x8d\xf2@\x8a\xd7-\xc1\xfdCT"

print("Cracking...")

for d in dict:
    for i in range(0, 9):
        for n in names:
            test = d + str(i) + n
            m = hashlib.md5()
            m.update(bytes(test, "UTF-8"))
            if (m.digest() == hash):
                 print(test)
                 print("FOUND")
                 sys.exit(0)
print("NOT FOUND")
