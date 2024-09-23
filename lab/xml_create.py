import xml.etree.ElementTree as ET

def write_to_xml(file_path, n0, h, nk, a, b, c):
    # Создаем корневой элемент
    root = ET.Element("data")

    # Добавляем элементы с данными
    ET.SubElement(root, "n0").text = str(n0)
    ET.SubElement(root, "h").text = str(h)
    ET.SubElement(root, "nk").text = str(nk)
    ET.SubElement(root, "a").text = str(a)
    ET.SubElement(root, "b").text = str(b)
    ET.SubElement(root, "c").text = str(c)

    # Создаем дерево и записываем его в файл
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

# Пример использования функции
write_to_xml("data.xml", n0=1, h=2.5, nk=3.0, a=4.1, b=5.2, c=6.3)
