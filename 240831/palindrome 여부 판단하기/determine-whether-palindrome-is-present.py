STR = list(input())

STR_R = ""
for i in STR:
    STR_R = i + STR_R

STR = "".join(STR)
if STR == STR_R:
    print('YES')
else:
    print('No')