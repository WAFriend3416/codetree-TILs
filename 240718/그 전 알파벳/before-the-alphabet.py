#97 : a , 122: z
# ord(문자) : 아스키코드(숫자) 반환
# chr(숫자) : 문자 반환

n = input()

if ord(n) == 97:
    print('z')
else:
    print(chr(ord(n)-1))