word = "banana"
freq = {word[i]:word.count(word[i]) for i in range(len(word))}
print(freq)