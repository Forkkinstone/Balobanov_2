def knapsack(capacity, weights, values, n):
    # Создаем таблицу (n+1) строк и (capacity+1) столбцов
    # Заполняем нулями
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Идем по каждой вещи
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # Если вес текущей вещи меньше или равен текущему лимиту веса w
            if weights[i-1] <= w:
                # Выбираем максимум: 
                # 1. Мы берем вещь (её цена + цена остатка места в рюкзаке из предыдущей строки)
                # 2. Мы не берем вещь (просто берем значение из предыдущей строки)
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                # Вещь слишком тяжелая, просто копируем результат без неё
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

# Данные для теста
values = [60, 100, 120]  # Ценность вещей
weights = [10, 20, 30]   # Вес вещей
capacity = 50            # Макс. грузоподъемность рюкзака
n = len(values)

result = knapsack(capacity, weights, values, n)
print(f"Максимальная ценность в рюкзаке: {result}")
