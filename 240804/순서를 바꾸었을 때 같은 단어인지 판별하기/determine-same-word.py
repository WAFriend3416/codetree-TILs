li1 = sorted(list(input()))
li2 = sorted(list(input()))

if len(li1) != len(li2):
    print("No")
else:
    if li1 == li2:
        print("Yes")
    else:
        print("No")