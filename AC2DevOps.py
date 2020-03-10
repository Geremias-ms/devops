def ehprimo(primo):
    for i in range(2, primo+1):
        if i != primo:
            i = primo % i
            if i == 0:
                return False
                break
        else:
            return True
            break
cont = 1
num = 2
while cont < 100:
    if ehprimo(num) == True:
        print(num)
        cont += 1
    num = num + 1
    



