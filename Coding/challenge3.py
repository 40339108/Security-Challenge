import hashlib
import sys

l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

hash = b'\x04,#j\xc7U-Y;\xc70$\xc3\x1e\x0bf'

print("Cracking...")

for a in range(0, 26):
    print(l[a])
    for b in range(0, 26):
        print(l[b])
        for c in range(0, 26):
            for d in range(0, 26):
                for e in range(0, 26):
                    for f in range(0, 26):
                        for g in range(0, 26):
                            word = l[a] + l[b] + l[c] + l[d] + l[e] + l[f] + l[g]
                            word += l[g] + l[f] + l[e] + l[d] + l[c] + l[b] + l[a]
                            m = hashlib.md5()
                            m.update(bytes(word, 'UTF-8'))
                            if (m.digest() == hash):
                                print(word)
                                print("FOUND")
                                sys.exit(0)
print("NOT FOUND")
