def compute_lps(pattern):
    """Вычисляет префикс-функцию (массив LPS) для заданного образца."""
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    """Находит все вхождения образца в текст с использованием алгоритма КМП."""
    m = len(pattern)
    n = len(text)
    if m == 0:
        return []

    lps = compute_lps(pattern)
    occurrences = []
    i = 0
    j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            occurrences.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return occurrences

if __name__ == "__main__":
    # Тестовые данные
    sample_text = "ABABDABACDABABCABAB"
    sample_pattern = "ABABCABAB"

    print(f"Текст для поиска: {sample_text}")
    print(f"Искомый образец:  {sample_pattern}")
    print("-" * 30)

    # Запуск поиска
    indices = kmp_search(sample_text, sample_pattern)

    if indices:
        print(f"Найдено вхождений: {len(indices)}")
        for idx in indices:
            print(f"Образец найден на позиции: {idx}")
            # Визуализация места вхождения
            print(sample_text)
            print(" " * idx + "^" * len(sample_pattern))
    else:
        print("Вхождений не найдено.")
