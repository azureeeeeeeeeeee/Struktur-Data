import random
import time

def BubbleSort(arr):
  print('----- Bubble Sort -----')
  step = 1
  for i in range(len(arr)):
    swapped = False
    for j in range(len(arr)-i-1):
      if arr[j] >= arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = True
      print(f'Step {step} :')
      print(arr)
      print('')
      step += 1
    if swapped == True:
      continue
    else:
      break

def SelectionSort(arr):
  print('----- Selection Sort -----')
  step = 1
  for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
      if arr[min_index] >= arr[j]:
        min_index = j
      print(f'Step {step} :')
      print(arr)
      print('')
      step += 1
    arr[i], arr[min_index] = arr[min_index], arr[i]

def InsertionSort(arr):
  print('----- Insertion Sort -----')
  # step = 1
  for i in range(1, len(arr)):
    min = arr[i]
    j = i - 1
    while j >= 0 and min < arr[j]:
      arr[j+1] = arr[j]
      j -= 1
      arr[j+1] = min
    # print(f'Step {step} :')
    # print(arr)
    # print('')
    # step += 1
  return arr

# def BogoSort(arr):
#     step = 1
#     n = 0 
    
#     while n < len(arr) - 1:
#         if is_sorted(arr, n):
#             n += 1
#         else:
#             random.shuffle(arr[n:])
#             print(f'Step {step} :')
#             print(arr)
#             print('')
#             step += 1


# def QuickSort(arr):
#   pivot = arr[0]
#   less = [x for x in arr[1:] if x <= pivot]
#   more = [x for x in arr[1:] if x > pivot]
#   sorted_less = QuickSort(less)
#   sorted_more = QuickSort(more)
#   sorted_arr = sorted_less + [pivot]+ sorted_more
#   return sorted_arr

# def is_sorted(arr, n):
#     for i in range(n, len(arr) - 1):
#         if arr[i] > arr[i + 1]:
#             return False
#     return True
    
# arr = [i for i in range(1, 11)]
# random.shuffle(arr)
arr = [1, 2, 3, 4, 5, 8, 7, 6, 9, 10]

print('List sebelum di sort : ')
print(arr)
print()

start_time = time.time()

# BogoSort(arr)
BubbleSort(arr)
# SelectionSort(arr)
# InsertionSort(arr)
# print(QuickestSort(arr))
# print(QuickSort(arr))

# sorted_arr = InsertionSort(arr)
# print('List setelah disorting : ')
# print(sorted_arr)

# print("--- %s seconds ---" % (time.time() - start_time))
