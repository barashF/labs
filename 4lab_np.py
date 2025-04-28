import numpy as np

# 1. Создание случайной матрицы 10x10 с числами от 0 до 100
matrix = np.random.uniform(0, 100, size=(10, 10))
print("Матрица:\n", matrix)

# 2. Среднее значение всех элементов
mean_value = np.mean(matrix)
print("\nСреднее значение:", mean_value)

# 3. Минимальное и максимальное значения
min_value = np.min(matrix)
max_value = np.max(matrix)
print("Минимум:", min_value, "Максимум:", max_value)

# 4. Транспонирование матрицы
transposed_matrix = matrix.T
print("\nТранспонированная матрица:\n", transposed_matrix)

# 5. Сумма элементов на главной диагонали
diagonal_sum = np.trace(matrix)
print("\nСумма главной диагонали:", diagonal_sum)

# 6. Нормализация матрицы
normalized_matrix = matrix / max_value
print("\nНормализованная матрица:\n", normalized_matrix)

# 7. Переворот строк матрицы
flipped_matrix = matrix[::-1]
print("\nПеревернутая матрица:\n", flipped_matrix)