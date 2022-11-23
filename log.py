from info import phonebook


def read_contact():
    with open('Phonebook.csv', 'r', encoding='utf-8') as f:
        return f.read()


def writing_csv(phonebook):
    file = 'phonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'Фамилия: {phonebook[0]}; Имя: {phonebook[1]}; Номер телефона: {phonebook[2]}; Описание: {phonebook[3]}\n')


def writing_txt(phonebook):
    file = 'phonebook.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'Фамилия: {phonebook[0]}; Имя: {phonebook[1]}; Номер телефона: {phonebook[2]}; Описание: {phonebook[3]}\n')
