n = int(input())
a = list(map(int, input().split()))

first_neg_index = None
for i in range(n):
    if a[i] < 0:
        first_neg_index = i
        break

last_non_neg_index = None
for i in range(n-1, -1, -1):
    if a[i] >= 0:
        last_non_neg_index = i
        break

if first_neg_index is not None and last_non_neg_index is not None:
    a[first_neg_index], a[last_non_neg_index] = a[last_non_neg_index], a[first_neg_index]

print(' '.join(map(str, a)))