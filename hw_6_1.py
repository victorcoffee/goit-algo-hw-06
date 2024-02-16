# Модуль 6

import os, re

os.system("cls")


from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # реалізація класу
    name: Field


class Phone(Field):
    # реалізація класу
    phone: Field

    # Додати перевірку
    def __init__(self, value):
        super().__init__(value)

    # Перевірка під self. Переробити під str?
    def is_phone(self):
        pattern = r"\d{10}"
        match = re.search(pattern, str(self.phone))
        if match:
            return self.phone
        else:
            print(f"Некоректний номер")
            return


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу

    def add_phone(self, phone: Phone):
        self.phones.append(phone)
        return f"Номер {phone} додано {self.name.value}"

    def remove_phone(self, phone: Phone):
        # перевірку існування зробити корректно
        self.phones.remove(phone)

    # перевірку існування зробити корректно
    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        if self.phones[old_phone]:
            self.phones[old_phone] = new_phone
            return f"Номер {new_phone} оновлено для {self.name.value}"

    def find_phone(self, phone: Phone):
        if phone in self.phones:
            return f"{self.name}: {phone}"
        else:
            return f"Телефон {phone} не знайдено"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    # реалізація класу
    book = UserDict()

    def add_record(self, record: Record):
        self.data[record.name] = record.phones

    def find(self, name: Name):
        # перевірку існування зробити корректно
        # self.data.get(name)
        if name in self.data:
            return self.data[name]
        else:
            print(f"Контакт {name} відсутній")

            return

    def delete(self, name: Name):
        # перевірку існування зробити корректно
        if self.data[name]:
            del self.data[name]
            print(f"Контакт {self.data[name]} видалено")
        else:
            return f"Контакт {self.data[name]} відсутній"


def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")


if __name__ == "__main__":
    main()
