import hashlib

dict_file = open('dictionary.txt', 'r')
names_file = open('rawnames.txt', 'r')

dict = []
names = []

for d in dict_file:
    dict.append(d[:-1])
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

#hash = 'apple7Sam'
#hash = b'2,)\xf3\xefk\x05\xf5?p\x11\xc6\xea\xd85M'
hash = b"\xfd{eZ'~\x8df2@\x8a\xd7-\xc1\xfdCT"

for d in dict:
    for i in range(0, 9):
        for n in names:
            test = d + str(i) + n
            m = hashlib.md5()
            string = bytes(test, "UTF-8")
            m.update(string)
            #print(m.digest())
            if (m.digest() == hash):
                 print(test)
                 exit()
