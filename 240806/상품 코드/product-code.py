class Product:
    def __init__(self,name="codetree",code=50):
        self.name = name
        self.code = code

pd1 = Product()
asdf,asdd = map(str,input().split())
pd2 = Product(asdf,asdd)

print("product",pd1.code,"is",pd1.name)
print("product",pd2.code,"is",pd2.name)