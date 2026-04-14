def get_bad_char_table(pattern):
    """Формирует таблицу последних вхождений каждого символа для правила плохого символа."""
    bad_char = {}
    for i in range(len(pattern)):
        bad_char[pattern[i]] = i
    return bad_char

def bms_search(text, pattern):
    """Выполняет поиск образца в тексте по алгоритму Бойера-Мура."""
    m = len(pattern)
    n = len(text)
    if m == 0: return []

    bad_char = get_bad_char_table(pattern)
    occurrences = []
    shift = 0

    while shift <= (n - m):
        j = m - 1

        # Сравниваем образец с текстом справа налево
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        if j < 0:
            # Образец найден полностью
            occurrences.append(shift)
            # Сдвигаем образец, чтобы найти следующее вхождение
            if shift + m < n:
                shift += m - bad_char.get(text[shift + m], -1)
            else:
                shift += 1
        else:
            # Произошло несовпадение, применяем правило плохого символа
            char_in_text = text[shift + j]
            bad_char_shift = j - bad_char.get(char_in_text, -1)
            shift += max(1, bad_char_shift)

    return occurrences

if __name__ == "__main__":
    text_to_search = "HERE IS A SIMPLE EXAMPLE"
    pattern_to_find = "EXAMPLE"

    print(f"Текст:   {text_to_search}")
    print(f"Образец: {pattern_to_find}")
    print("-" * 30)

    results = bms_search(text_to_search, pattern_to_find)

    if results:
        print(f"Найдено совпадений: {len(results)}")
        for pos in results:
            print(f"Позиция начала вхождения: {pos}")
            # Наглядная визуализация
            print(text_to_search)
            print(" " * pos + "^" * len(pattern_to_find))
    else:
        print("Совпадений не обнаружено.")
