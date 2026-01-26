alphabet = [-1] * 26
word = input()

for i, w in enumerate(word):
    if (alphabet[ord(w) - ord('a')] == -1):
        alphabet[ord(w) - ord('a')] = i

print(" ".join(map(str, alphabet)))