class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        str_product = f'{self.name}, {self.weight}, {self.category}'
        return str_product


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

        file = open(self.__file_name, 'a')
        file.close()

    def get_products(self):  # возвращает длинную строку
        file = open(self.__file_name, 'r')
        result = file.read()
        file.close()
        return result

    def add(self, *products: Product):
        lines = self.get_products().splitlines()
        existing_products = []
        for line in lines:  # 'Potato', 50.0, 'Vagetables'
            product = line.split(', ')[0]
            existing_products.append(product)

        for prod in products:
            if prod.name not in existing_products:
                file = open(self.__file_name, 'a')
                file.write(str(prod) + '\n')
                file.close()
            else:
                print(f'Продукт {prod.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

s1 = Shop()
s1.add()