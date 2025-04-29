import numpy as np

matrix = np.random.uniform(0, 100, size=(10, 10))
print("Матрица:\n", matrix)

mean_value = np.mean(matrix)
print("\nСреднее значение:", mean_value)

min_value = np.min(matrix)
max_value = np.max(matrix)
print("Минимум:", min_value, "Максимум:", max_value)

transposed_matrix = matrix.T
print("\nТранспонированная матрица:\n", transposed_matrix)

diagonal_sum = np.trace(matrix)
print("\nСумма главной диагонали:", diagonal_sum)

normalized_matrix = matrix / max_value
print("\nНормализованная матрица:\n", normalized_matrix)

flipped_matrix = matrix[::-1]
print("\nПеревернутая матрица:\n", flipped_matrix)