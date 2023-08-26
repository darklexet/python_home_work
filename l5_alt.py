phonebook = {}

def show_menu():
    print("[1] Поиск контакта")
    print("[2] Добавление контакта")
    print("[3] Изменение контакта")
    print("[4] Удаление контакта")
    print("[5] Вывод всех контактов")
    print("[0] Выход")

def search_contact():
    name = input("Введите имя контакта: ")
    if name in phonebook:
        print("Фамилия:", phonebook[name][0])
        print("Имя:", phonebook[name][1])
        print("Отчество:", phonebook[name][2])
        print("Телефон:", phonebook[name][3])
    else:
        print("Контакт не найден")

def add_contact():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    number = input("Введите номер телефона: ")
    phonebook[name] = (surname, name, patronymic, number)
    print("Контакт добавлен")

def update_contact():
    name = input("Введите имя контакта для изменения: ")
    if name in phonebook:
        print("Введите новые данные для контакта:")
        surname = input("Фамилия: ")
        name = input("Имя: ")
        patronymic = input("Отчество: ")
        number = input("Номер телефона: ")
        phonebook[name] = (surname, name, patronymic, number)
        print("Контакт изменен")
    else:
        print("Контакт не найден")

def delete_contact():
    name = input("Введите имя контакта для удаления: ")
    if name in phonebook:
        del phonebook[name]
        print("Контакт удален")
    else:
        print("Контакт не найден")

def print_contacts():
    for name in phonebook:
        print("Фамилия:", phonebook[name][0])
        print("Имя:", phonebook[name][1])
        print("Отчество:", phonebook[name][2])
        print("Телефон:", phonebook[name][3])
        print()

while True:
    show_menu()
    choice = input("Выберите опцию: ")

    if choice == "1":
        search_contact()
    elif choice == "2":
        add_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print_contacts()
    elif choice == "0":
        break
    else:
        print("Неверный ввод")