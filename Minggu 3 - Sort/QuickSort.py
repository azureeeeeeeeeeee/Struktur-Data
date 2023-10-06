import random

def QuickSort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[0]
  left = [x for x in arr[1:] if x < pivot]
  right = [x for x in arr[1:] if x > pivot]

  left = QuickSort(left)
  right = QuickSort(right)

  return left+[pivot]+right

def ShellSort(arr):
  n = len(arr)
  gap = n // 2
  while gap > 0:
    for i in range(gap, n):
      sem = arr[i]
      j = i
      while j >= gap and sem < arr[j-gap]:
        arr[j] = arr[j-gap]
        j -= gap
      arr[j] = sem
    gap //= 2
  return arr

lst = [i for i in range(10)]
random.shuffle(lst)

# print('List sebelum di Quick Sort :')
print(lst)
print()
# print('\nList seteleah di Quick Sort:')
print(ShellSort(lst))