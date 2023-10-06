import random
import time

def BubbleSort(arr):
  step = 1
  for i in range(len(arr)):
    for j in range(len(arr)-i-1):
      if arr[j] >= arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
      print(f'Step {step} :')
      print(arr)
      print('')
      step += 1

def SelectionSort(arr):
  for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
      if arr[min_index] >= arr[j]:
        min_index = j
    print(arr)
    arr[i], arr[min_index] = arr[min_index], arr[i]

start_time = time.time()

lst = []
for i in range(101):
  lst.append(random.randint(-100,100))
print(lst)
# BubbleSort(lst)
# SelectionSort(lst)

print("Process finished --- %s seconds ---" % (time.time() - start_time))