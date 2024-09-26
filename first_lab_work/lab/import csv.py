import csv

# Данные для записи в CSV файл
data = [
    {'n0': 1, 'h': 2, 'nk': 3, 'a': 4.1, 'b': 5.2, 'c': 6.3}
]

# Имя файла
filename = 'config.csv'

# Запись данных в CSV файл
with open(filename, mode='w', newline='') as csvfile:
    fieldnames = ['n0', 'h', 'nk', 'a', 'b', 'c']  # Заголовки столбцов
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # Записываем заголовки
    for row in data:
        writer.writerow(row)  # Записываем строки данных

print(f"CSV файл '{filename}' успешно создан.")
