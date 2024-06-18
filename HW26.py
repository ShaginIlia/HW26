def add_everything_up(a, b):
    c = a + b


try:
    print(add_everything_up(2, 'два'))
    print(add_everything_up(234.45, 10))
except TypeError as exc:
    print('2два')
    print(float(234.45) + float(10))
else:
    print('Всё сходиться')
