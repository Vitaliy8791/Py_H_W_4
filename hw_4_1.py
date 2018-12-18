from string import whitespace, punctuation, ascii_letters, digits

enter_num = []
enter_char = []
fltterstr = whitespace + punctuation + digits


def clear_word(enter_string, filt):  # функция проверяет текст на символы не из английского алфавита
    enter_char = []
    enter_list = list(enter_string)  # преобразовываем текст в список символов текста
    for i in range(0, len(enter_list)):
        if enter_list[i] in filt:  # если символ в строке из специальных символов и символов пунктуации пропускаем его
            continue
        if enter_list[i] not in ascii_letters:  # если символ в строке не из английского алфавита вызываем исключение
            raise ValueError
        enter_char.append(enter_list[i])

    return enter_char


def bad_char(text):  # функция проверяет текст на символы не из английского алфавита
    enter_list = list(text)
    for i in range(0, len(enter_list)):
        if enter_list[i] in fltterstr:  # пропускаем специальные символы и символы пунктуации
            continue
        if enter_list[i] not in ascii_letters:
            enter_char.append(enter_list[i])  # добавляем в список отобранных символов
            enter_num.append(i)  # запоменаем его порядковый номер
    return enter_char, enter_num


if __name__ == "__main__":
    text = """clear_word - Функция по очистке слова от символов не из - filterstr"""
try:
    enter_list = clear_word(text, fltterstr)  # вызываем функцию clear_word
    print("В тексте только специальные, английские символы и символы пунктуации!")




except ValueError:  # выводим результат поиска
    print("В тексте найдены символы не из английскго алфавита!\n")
    bad_list, bad_num = bad_char(text)
    print(bad_list)
    print(bad_num)
    print("В тексте найдены символы не из английскго алфавита!\n")
    print("| {:^3}  | {:^5} |".format("СИМВОЛ", "НОМЕР ПОЗИЦИИ"))
    print("|_________|_______________|")
    for i in range(0, len(bad_list)):
        print("| {:6}  | {:>13} |".format(bad_list[i], bad_num[i]))
