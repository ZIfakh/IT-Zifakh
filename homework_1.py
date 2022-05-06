import random

class Human:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def introduce_human(self):
        print(f"Имя: {self.name}. Фамилия: {self.surname}. Возраст: {self.age}.")

    def __repr__(self):
        return f"{self.name} {self.surname} {self.age}"

    def takeaqueae(self, queue_obj):
        return Queue.static_add_person(queue_obj, self)


class Queue:

    def __init__(self):
        self.list = []

    @staticmethod
    def static_add_person(queue_obj, person):
        return queue_obj.add_item(person)

    def add_item(self, person):
        self.list.append(person)

    def dell_list(self):
        if self.list == 0:
            return None
        return self.list.remove(self.list)

    def random_list(self, person):
        rnd = random.randrange(len(self.list))
        print(self.list[rnd])
        return self.list.insert(rnd + 1, person)


queue = Queue()

first_pers = Human('Чичик', 'Младший', 6)
second_pers = Human('Кадр', 'Старший', 66)
third_pers = Human('Штрих', 'Низший', 666)
four_pers = Human('Чипинкос', 'Высший', 25)

queue.add_item(first_pers)
queue.add_item(second_pers)
queue.add_item(third_pers)
queue.random_list(four_pers)
print(queue.list)