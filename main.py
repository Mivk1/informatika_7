import components.sellers.service as seller

add_el = "создать"
delete_el = "удалить"
get_el = "вывести все"
get_id = "вывести по id"
upd_id = "заменить"
user = input("Как изменить список: создать, удалить, вывести все, вывести по id, заменить  ")
if user.lower() == add_el.lower():
    print(seller.create_one({
        "name": "Анна Кузнецова",
        "hall_id": [
                1,
                2
            ],
        "contacts": {
            "email": "annakuznec@example.com",
            "phone": "+35793495"
            }}), " Вы добавили этот элемент")
elif user.lower() == delete_el.lower():
    print(seller.delete_one_by_id(3), " Вы удалили этот элемент")
elif user.lower() == get_el.lower():
    print(seller.get_all(), " Все элементы списка")
elif user.lower() == get_id.lower():
    q_id = input("Введите номер id: ")
    if q_id == 1:
        print(seller.get_one_by_id(1), " Элемент с 1 id")
    elif q_id == 2:
        print(seller.get_one_by_id(2), " Элемент с 2 id")
    elif q_id == 3:
        print(seller.get_one_by_id(3), " Элемент с 3 id")
    elif q_id == 4:
        print(seller.get_one_by_id(4), " Элемент с 4 id")
    else:
        print("Элемент с этим id не найден")
elif user.lower() == upd_id.lower():
    print(seller.update_one_by_id(4, {
        "name": "Петр Петрович",
        "contacts": {
            "email": "petr@example.com",
            "phone": "+1122334455"
        }}))
else:
    print("Пожалуйста, укажите пункт, который есть в меню!")
