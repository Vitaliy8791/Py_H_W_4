from string import punctuation, ascii_letters, digits, whitespace
from hw_4.hw_4_1 import clear_word

enter_char = []
filt1 = punctuation + digits + whitespace
filt2 = punctuation + digits + '\t\n\r\x0b\x0c'
ascii_lettersflt = ascii_letters + " "


def bad_char(text):  # функция проверяет текст на символы не из английского алфавита
    text = text.lower()
    enter_list = list(text)
    for i in range(0, len(enter_list)):
        if enter_list[i] in filt2:  # пропускаем специальные символы и символы пунктуации
            continue
        if enter_list[i] in ascii_lettersflt:
            enter_char.append(enter_list[i])  # добавляем в список отобранных символов
    new_str = ("".join(str(x) for x in enter_char))
    new_str = new_str.split(" ")
    new_str.sort()
    while new_str[0] == "":
        new_str.remove("")
    return new_str


if __name__ == "__main__":
    text = """Clear_word - Функция по filterstr очистке слова от символов не из - filterstr"""
    print("\nИсходный текст: ", text)
    print("-----------------------------------")
try:
    enter_list = clear_word(text, filt1)  # вызываем функцию clear_word
    print("В тексте только специальные, английские символы и символы пунктуации!")

except ValueError:  # выводим результат поиска
    print("В тексте найдены символы не из английскго алфавита!")
    bad_list = set(bad_char(text))
    print("Очищенный текст: ", bad_list)
