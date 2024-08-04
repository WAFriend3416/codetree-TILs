li_item = list(input().split())

li_words = []

for _ in range(int(li_item[0])):
    word = input()
    if word.startswith(li_item[2]):
        li_words.append(word)

li_words = sorted(li_words)

print(li_words[int(li_item[1])-1])