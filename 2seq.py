dict_sep = {0: ',',
            1: '.',
            2: '/'}

in_values = input("Введите последовательность чисел, через разделитель (. или , или /)")

#Удаляем все лишние пробелы в строке
in_values = in_values.replace(' ', '')

#Проверим, что в строке только один из разрешенных разделителей
check = [in_values.count('.') > 0, in_values.count(',') > 0, in_values.count('/') > 0]

if check.count(True) > 1 or check.count(True) == 0:
    print('Возможно использовать только один из разделителей: (. или , или /)')
else:
    print(','.join( in_values.split(dict_sep[check.index(True)])))

