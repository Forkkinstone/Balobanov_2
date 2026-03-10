def compute_transition_table(pattern, alphabet):
    """Строит таблицу переходов конечного автомата."""
    m = len(pattern)
    # Инициализируем таблицу нулями
    table = [{c: 0 for c in alphabet} for _ in range(m + 1)]

    for q in range(m + 1):
        for c in alphabet:
            # k - следующее потенциальное состояние
            k = min(m, q + 1)
            # Строка, которую мы сейчас "прочитали"
            current_str = pattern[:q] + c

            # Ищем наибольший префикс образца, который является суффиксом current_str
            while k > 0 and not current_str.endswith(pattern[:k]):
                k -= 1
            table[q][c] = k

    return table


def fsm_string_search(text, pattern, alphabet):
    """Выполняет поиск образца в тексте с помощью автомата."""
    m = len(pattern)
    n = len(text)
    if m == 0:
        return []

    # Этап 1: Препроцессинг
    table = compute_transition_table(pattern, alphabet)

    # Этап 2: Поиск
    q = 0  # Начальное состояние (совпало 0 символов)
    occurrences = []

    for i in range(n):
        # Переходим в новое состояние по текущему символу текста
        q = table[q].get(text[i], 0)

        # Если достигли финального состояния, фиксируем индекс
        if q == m:
            # Вычисляем начальный индекс найденной подстроки
            occurrences.append(i - m + 1)

    return occurrences


# --- Тестирование ---
alphabet = "ab"
text = "ababaabaab"
pattern = "abaab"
result = fsm_string_search(text, pattern, alphabet)
print(f"Образец найден на индексах: {result}")
