
print('\n-------------------task 5/1--------------')
file_abs = "C:/Users/stavr/Downloads/Семинар 5. Погружение в Python. Итераторы и генераторы.pdf"

def path_name(name):
    full_file_name = file_abs.split('/')[-1:][0]
    full_path = file_abs.split(full_file_name)[0]
    exten_file = full_file_name.split('.')[-1:][0]
    return (full_path, full_file_name, exten_file)

res_out = path_name(file_abs)
print(res_out)

# -------------------task 5/2--------------

print('\n-------------------task 5/2--------------')
list_1 = ['var1', 200, '12.25%']
list_2 = ['var2', 300, '13.25%']
list_3 = ['var3', 400, '14.25%']

def gen_premiya_one_str(name1, name2, name3):
    res_gen = ({i[0]: i[1] * float(i[2].split('%')[0])} for i in iter([name1, name2, name3]))
    yield res_gen

for i in gen_premiya_one_str(list_1, list_2, list_3):
    print(*i)


# -------------------task 5/3--------------

print('\n-------------------task 5/3--------------')


def fibon(n):
    ' первые два числа равны 0 и 1, а каждое последующее число равно сумме двух предыдущих чисел'
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

print(list(fibon(10)))

# fibon(5)