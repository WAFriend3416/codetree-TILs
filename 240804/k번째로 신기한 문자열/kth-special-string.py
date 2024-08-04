li_item = list(input().split())

li_words = []

for _ in range(int(li_item[0])):
    word = input()
    if li_item[2] in word:
        li_words.append(word)

li_words

print(sorted(li_words)[int(li_item[1])-1])