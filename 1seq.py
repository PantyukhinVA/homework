result_list = []

count_list_elements = input('Введите количество элементов: ')

for i in range(int(count_list_elements)):
    result_list.append(int(input(f'Введите {i + 1} элемент: ')))

result_list.sort()

print(result_list)
