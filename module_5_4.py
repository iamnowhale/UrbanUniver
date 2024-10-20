class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
          house_name = args[0]
          cls.houses_history.append(house_name)
          return super().__new__(cls)

    def __init__(self, name: str, number_of_floors: int):
          self.name = name
          self.number_of_floors = number_of_floors

    def __len__(self):
          return self.number_of_floors

    def __str__(self) -> str:
          return f'Название: {self.name}, кол-во этажей {self.number_of_floors}'

    def __eq__(self, other):
          if isinstance(other, House):
                return self.number_of_floors == other.number_of_floors
          return NotImplemented

    def __lt__(self, other):
          if isinstance(other, House):
                return self.number_of_floors < other.number_of_floors
          return NotImplemented

    def __le__(self, other):
          if isinstance(other, House):
                return self.number_of_floors <= other.number_of_floors
          return NotImplemented

    def __gt__(self, other):
          if isinstance(other, House):
                return self.number_of_floors > other.number_of_floors
          return NotImplemented

    def __ge__(self, other):
          if isinstance(other, House):
                return self.number_of_floors >= other.number_of_floors
          return NotImplemented

    def __ne__(self, other):
          if isinstance(other, House):
                return self.number_of_floors != other.number_of_floors
          return NotImplemented

    def __add__(self, other):
        if isinstance(other, House):
            return House(self.name, self.number_of_floors + other.number_of_floors)
        if isinstance(other, int):
            return House(self.name, self.number_of_floors + other)

        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i + 1)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)
