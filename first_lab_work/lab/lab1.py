import xml.etree.ElementTree as ET
import argparse
import math
import csv  

def parse_file(file_path):
    """Определяет тип файла и парсит его соответствующим образом."""
    if file_path.endswith('.xml'):
        return parse_xml(file_path)
    elif file_path.endswith('.csv'):
        return parse_csv(file_path)
    else:
        raise ValueError("Unsupported file type. Please provide a .xml or .csv file.")
    
def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    parameters = {
        'n0': int(root.find('n0').text),
        'h': int(root.find('h').text),
        'nk': int(root.find('nk').text),
        'a': float(root.find('a').text),
        'b': float(root.find('b').text),
        'c': float(root.find('c').text)
    }
    
    return parameters

def parse_csv(file_path):
    parameters = {}
    with open(file_path, mode='r') as csvfile:
        reader = csv.DictReader(csvfile) #возвращает объект reader, который построчно итерирует csvfile
        for row in reader:
            parameters['n0'] = int(row['n0'])
            parameters['h'] = int(row['h'])
            parameters['nk'] = int(row['nk'])
            parameters['a'] = float(row['a'])
            parameters['b'] = float(row['b'])
            parameters['c'] = float(row['c'])
    
    return parameters

def function(x, a, b, c):
    return a * (math.sin(x))**2 + b * math.cos(x) + c

def main():
    #Создаем экземпляр ArgumentParser, который будет обрабатывать аргументы командной строки
    parser = argparse.ArgumentParser(description='обработка cmd')

    #add_argument добавляет новый аргумент, который можно передать программе при запуске
    parser.add_argument('--config', type=str) 
    #--config — это имя аргумента, - type=str указывает, что ожидается строка (путь к файлу конфигурации)
    
    #выполняем парсинг аргументов. После объект args будет содержать значения всех аргументов, которые были переданы программе
    args = parser.parse_args()

    if args.config:
        parameters = parse_file(args.config)
    else:
        # Запрашиваем параметры у пользователя
        parameters = {}
        parameters['n0'] = int(input("Введите n0: "))
        parameters['h'] = int(input("Введите h: "))
        parameters['nk'] = int(input("Введите nk: "))
        parameters['a'] = float(input("Введите a: "))
        parameters['b'] = float(input("Введите b: "))
        parameters['c'] = float(input("Введите c: "))

    
   # Извлекаем параметры
    n0 = parameters['n0']
    h = parameters['h']
    nk = parameters['nk']
    a = parameters['a']
    b = parameters['b']
    c = parameters['c']

    results = []
    # Вычисляем значения функции
    for x in range(n0, nk + 1, h):
        y = function(x, a, b, c)
        results.append((x, y))

    with open('results.txt', 'w') as f:
        for x, y in results:
            f.write(f"x: {x}, y: {y}\n")


if __name__ == '__main__':
    main()
