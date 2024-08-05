class User:
    def __init__(self,user_id="codetree",user_level="10"):
        self.user_id = user_id
        self.user_level = user_level

User1 = User()

user_id , user_level = map(str,input().split())

User2 = User(user_id,user_level)


print(f'user {User1.user_id} lv {User1.user_level}')
print(f'user {User2.user_id} lv {User2.user_level}')