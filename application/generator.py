from random_username.generate import generate_username

def generate():
    quantity = input("Введите количество необходимых имён пользователей: ")
    print(generate_username(int(quantity)))

