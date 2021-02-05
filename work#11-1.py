# 1.함수 twoSumSorted(a, n)을 사용하여 중복 원소가 없는 정렬된 리스트에서
# 두 원소를 더한 합이 사용자로부터 입력 받은 목표값과 같은 것이 있으면,
# 두 원소가 각각 리스트의 몇 번째 원소인지 출력하는 프로그램을 작성하라.
def twoSumSorted(a, t):
    n = len(a)
    for i in range(0, n):
        j = n - 1
        while i < j:
            if a[i] + a[j] == t:
                print(i + 1, '번째와', j + 1, '번째 원소')
                j -= 1
            else:
                j -= 1
        i += 1


import random

k = int(input('리스트의 원소 개수 입력:'))
a = []
for i in range(k):
    a.append(random.randint(1, k * 2))
print('리스트:', a)
for i in range(len(a)):
    j = len(a) - 1
    while i < j:
        if a[i] == a[j]:
            a.pop(j)
            j -= 1
        else:
            j -= 1
    i += 1
print('중복이 제거된 리스트:', a)
t = int(input('목표값 입력:'))
print('두 수의 합이', t, '인 원소 쌍')
twoSumSorted(a, t)
