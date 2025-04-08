data = b'hello word!'

# 通过函数的方式，不管怎么转换都行，不用去记是decode还是encode
data = str(data, encoding='utf-8')
print(data)

data = bytes(data, encoding='utf-8')
print(data)