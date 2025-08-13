def find_vowels (text):
    count=0
    for ch in text:
        if ch.lower() in "aeiou":
            yield ch
            count+=1
    return count

gen=find_vowels ("Hello World")
it=iter(gen)
while True:
    try:
        vowel=next(it)
        print("Vowel found:", vowel)
    except StopIteration as e:
        print("Total Vowels:",e.value)
        break