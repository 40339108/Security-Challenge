import hashlib

dict_file = open('dictionary.txt', 'r')

dict = []

for d in dict_file:
    dict.append(d[:-1])
dict_file.close()

print("Loaded Dictionary...")

g = "αβγδεζηθικλμνξοπρςστυφχψωï"
a = "abcdefghijklmnopqrstuvwxyz"
g_letters = []
alphabet = []

for i in range(0, 26):
    g_letters.append(g[i])
    alphabet.append(a[i])

# hash = 'αppL77e'
# m = hashlib.md5()
# m.update(bytes(hash, 'UTF-8'))
# print(m.digest())
# exit()
#hash = b'\x90E\xfbf\xc4n*\xa8\x19\xa2\xb9\xb6!#\x94\xdc'
hash = b'\xa8\x8e\x89X\tJ\x80\xd0i)\xe1\xce\xd1O\xff\x9c'

for d in dict:
    temp = list(d)
    for i in range(0, len(temp)):
        word_i = list()
        word_i += temp
        if(word_i[i] in alphabet):
            word_i[i] = word_i[i].upper()
            for j in range(0, len(temp)):
                word_j = list()
                word_j += word_i
                if(word_j[j] in alphabet):
                    word_j[j] = g_letters[alphabet.index(word_j[j])]
                    for k in range(0, len(temp) + 1):
                        word_k = list()
                        word_k += word_j
                        for l in range(0, 10):
                            word_l = list()
                            word_l += word_k
                            word_l.insert(k, str(l))
                            word_l.insert(k, str(l))
                            word_l = "".join(word_l)
                            print(word_l)
                            m = hashlib.md5()
                            m.update(bytes(word_l, 'UTF-8'))
                            if(m.digest() == hash or word_l == 'appL77e'):
                                print(word_l)
                                print("FOUND")
                                exit()

print("NOT FOUND")
