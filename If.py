a = input('Введіть число, яке буде оброблено: ')
a = int(a)
a = a // 2 + 7
print("А тепер вгадай число ")
c = input()
c = int(c)

while c != a:
    if c > a:
        print('менше')
    else:
        print('більше')
    c = input()
    c = int(c)

print('молодець!')