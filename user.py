from info import phonebook
from log import read_contact, writing_csv, writing_txt

def first_step():
    print('Выберите:\n 1.Добавить новый контакт\n 2.Вывести телефонную книгу')
    mode = int(input())
    if mode == 1:
        a = phonebook()
        writing_txt(a)
        writing_csv(a)
    elif mode ==2:
        print(read_contact())
    else:
        print('Введено неверное значение')