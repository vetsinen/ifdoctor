# результаты проверки можно сохранять в переменные

c = 5 < 4
print(c)

p = "python" > "java"
print(p)
if p:
    print("python is the best")

if "python" > "java":
    print("python is the best")

print(type(p))  # переменная будет иметь так называемый boolean-тип

# сравнение "python" > "java" не подразумевает, что язык python лучше языка Java
# в этом примере лишь производиться сравнение двух строк по значениям их кодов
