from string import punctuation, whitespace

fltterstr = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# создаём строку из специальных, английских символов и символов пунктуации
fltterstr1 = fltterstr + punctuation + whitespace

try:
    def clear_word(enter_string, filt):
        enter_num = []
        enter_char = []
        enter_list = list(enter_string)  # преобразовываем текст в список символов текста
        for i in range(0, len(enter_list)):
            if enter_list[i] in filt:  # если символ в строке из специальных, английских символов и символов пунктуации
                continue               # пропускаем его
            else:
                enter_char.append(enter_list[i])  # добавляем в список отобранных символов
                enter_num.append(i)  # запоменаем его порядковый номер
        rez_list = [enter_char, enter_num]  # создаём список кортежей из символов и порядковых номеров
        return rez_list


    if __name__ == "__main__":
        text = """clear_word - Функция по очистке слова от символов не из - filterstr"""
        enter_tupl = clear_word(text, fltterstr1)  # вызываем функцию clear_word
        char, num = enter_tupl  # разбиваем список кортежей на список символов и список порядковых номеров
        if char[0] is not None:  # если был хоть искомый символ вызываем ошибку
            raise ValueError

except IndexError:  # ошибка если небыло нужных символов
    print("В тексте только специальные, английские символы и символы пунктуации!")
except ValueError:  # выводим результат поиска
    print("В тексте найдены символы не из английскго алфавита!\n")
    print("| {:^3}  | {:^5} |".format("СИМВОЛ", "НОМЕР ПОЗИЦИИ"))
    print("|_________|_______________|")
    for i in range(0, len(char)):
        print("| {:6}  | {:>13} |".format(char[i], num[i]))
