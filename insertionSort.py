import random
import time
def InsertionSort(arr):
    langkah = 1
    for i in range (1,len(arr)):
        key = arr[i]
        j= i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = key
            print("Langkah ke ",langkah,": ", arr)
            langkah+=1

def InsertionSortbawah(arr):
    langkah = 1
    for i in range (1,len(arr)):
        key = arr[i]
        j= i-1
        while j>=0 and key > arr[j]:
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = key
            print("Langkah ke ",langkah,": ", arr)
            langkah+=1

def masukkanData():

    print("1. Insertion Sort Kecil-Besar \n2. Insertion Sort Besar-Kecil\n3.Keluar")
    pilih = int(input("Masukkan Pilihan: "))
    if pilih == 3:
        quit()
    elif pilih == 1:
        x = int(input("Masukkan Banyak Data yang ingin di sort: "))
        arr = []
        for i in range (x):
            arr.append(i)
        random.shuffle(arr)
        InsertionSort(arr)
        masukkanData()
    elif pilih == 2:
        x = int(input("Masukkan Banyak Data yang ingin di sort"))
        arr = []
        for i in range (x):
            arr.append(i)
        random.shuffle(arr)
        InsertionSortbawah(arr)
        masukkanData()
    else:
        print("great")




masukkanData()
