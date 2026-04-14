def rk_search(text, pattern, d=256, q=101):
    """Выполняет поиск образца в тексте алгоритмом Рабина — Карпа."""
    m = len(pattern)
    n = len(text)
    if m == 0 or m > n:
        return []

    h = pow(d, m - 1) % q
    p = 0  # Хеш образца
    t = 0  # Хеш текущего окна текста
    occurrences = []

    # Предварительное вычисление хеша
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        # Если хеши совпали, проверяем символы поштучно (защита от коллизий)
        if p == t:
            if text[i:i+m] == pattern:
                occurrences.append(i)

        # Вычисляем хеш для следующего окна
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            # В Python результат % может быть отрицательным, правим это:
            if t < 0:
                t = t + q

    return occurrences

if __name__ == "__main__":
    text_data = "GEEKS FOR GEEKS"
    pattern_data = "GEEKS"
    
    # Параметры d и q можно оставить по умолчанию
    print(f"Текст:   '{text_data}'")
    print(f"Искомое: '{pattern_data}'")
    print("-" * 35)

    found_indices = rk_search(text_data, pattern_data)

    if found_indices:
        print(f"Результат: Найдено {len(found_indices)} вхождений.")
        for pos in found_indices:
            print(f"-> Индекс: {pos}")
            print(text_data)
            print(" " * pos + "^" * len(pattern_data))
    else:
        print("Ничего не найдено.")
