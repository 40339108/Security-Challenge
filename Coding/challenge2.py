import hashlib
import sys

hash = b'\xa8\x8e\x89X\tJ\x80\xd0i)\xe1\xce\xd1O\xff\x9c'
dict_file = open('dictionary.txt', 'r')
dict = []
for d in dict_file:
    dict.append(d.lower()[:-1])
dict_file.close()
print("Loaded Dictionary...")

g = "αβγδεζηθικλμνξοπρςστυφχψωï"
a = "abcdefghijklmnopqrstuvwxyz"
g_letters = []
alphabet = []
for i in range(0, 26):
    g_letters.append(g[i])
    alphabet.append(a[i])

print("Cracking...")
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
                            for n in range(0, 10):
                                word_n = list()
                                word_n += word_l
                                word_n.insert(k, str(n))
                                word_n = "".join(word_n)
                                m = hashlib.md5()
                                m.update(bytes(word_n, 'UTF-8'))
                                if(m.digest() == hash):
                                    print(word_l)
                                    print("FOUND")
                                    sys.exit(0)
print("NOT FOUND")