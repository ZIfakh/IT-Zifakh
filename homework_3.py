import csv
from datetime import datetime


class User:

    def __init__(self, id, name, surname, age, phone):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone

    def get_dict_from_user(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'age': self.age,
            'phone': self.phone
        }

    def __repr__(self):
        return f' {self.id} {self.name} {self.surname} {self.age} {self.phone}'


class UserData:

    def __init__(self, file_path, columns):
        self.file_path = file_path
        self.columns = columns

    def clear(self):
        with open(self.file_path, 'w') as file:
            pass

    def add_user(self, user_obj):
        with open(self.file_path, 'a') as file:
            writer = csv.DictWriter(
                file, delimiter=';', fieldnames=self.columns)
            writer.writerow(user_obj.get_dict_from_user())

    def delete_user(self, user_id):
        users_list_csv = self.get_list_of_users()
        index = None
        for idx, user in enumerate(users_list_csv):
            if int(user['id']) == user_id:
                index = idx
        if index is not None:
            users_list_csv.pop(index)
            with open(self.file_path, 'w') as file:
                writer = csv.DictWriter(
                    file, delimiter=';', fieldnames=self.columns)
                writer.writerows(users_list_csv)
        else:
            raise Exception(f'cant find user with id {user_id}')

    def get_list_of_users(self):
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(
                file, delimiter=';', fieldnames=self.columns)
            return [line for line in reader]

    def get_user(self, user_id):
        with open(self.file_path, 'r') as file:
            user = None
            reader = csv.DictReader(
                file, delimiter=';', fieldnames=self.columns)

            for user_csv in reader:
                if int(user_csv['id']) == user_id:
                    user = user_csv

            return

    def send_message(self, user_1, user_2):
        with open('message_file.csv', 'a+') as file:
            send = user_1
            rec = user_2
            message = input("Сообщение:    ")
            user_information = (f'Отправитель {send}'
                                f' Получатель {rec}'
                                f' Сообщение {message}'
                                f' Время {datetime.now()}')
            record = csv.writer(file)
            record.writerow([user_information])

    def dell_messages(self):
        with open("message_file.csv", newline='') as input_file:
            with open("message_file.csv", "w", newline='') as out_file:
                writer = csv.writer(out_file)
                for row in csv.reader(input_file):
                    if any(row):
                        writer.writerow(row)

    def show_messages(self):
        with open("message_file.csv", "r") as message_file:
            reader = csv.reader(message_file)
            Name = set(row[2] for row in reader)
        with open("message_file.csv", "r") as message_file:
            reader = csv.reader(message_file)
            Text = set(row[0] for row in reader)
        return f'Сообщения: {Text}\nОтправители: {Name}'


data = UserData('users.csv', ['id', 'name', 'surname', 'age', 'phone'])

user = User(6, 'Чичик', 'Младший', 16, +7666666)
user2 = User(9, 'Чичик', 'Старший', 19, +799999)

data.add_user(user)
data.add_user(user2)

data.send_message(user, user2)
data.send_message(user2, user)