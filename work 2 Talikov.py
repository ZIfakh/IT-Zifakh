import csv


class Sim:
    def __init__(self, name, age, height, sex):
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height

    def eat_smthg(self, product_name, count):
        WriteFile("answer.csv").add_meal(self.name, product_name, count)


class WriteFile:
    def __init__(self, file_path, columns = ["Персонаж", "Что скушал", "Количество"]):
        self.file_path = file_path
        self.columns = columns

    def add_meal(self, userName, productName, count):
        with open(self.file_path, 'a') as file:
            writer = csv.DictWriter(
                file, delimiter=';', fieldnames=self.columns)
            writer.writerow({"Персонаж" : userName, "Что скушал" : productName, "Количество" : count})

    def get_list_of_meals(self):
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(
                file, delimiter=';', fieldnames=self.columns)
            return [line for line in reader]

Alex = Sim("Alex", 21, 185, "male")
Alex.eat_smthg("Гречка", 1)
Alex.eat_smthg("Яблоко", 2)
Alex.eat_smthg("Шоколадка", 1)

print(WriteFile("answer.csv").get_list_of_meals())