class House:

    # __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
    def __len__(self):
        return self.number_of_floors


    # __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


    def __init__(self, name, number_of_floors):

        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):

        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            print('-'.join([str(num) for num in range(1, new_floor+1)]))


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
