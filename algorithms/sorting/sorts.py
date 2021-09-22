import logging
import sys
from copy import deepcopy

log = logging.basicConfig(level=logging.INFO)
    
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            if arr[i]>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i]>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i-1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = temp
    return arr

def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
            
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1

def heapify(arr, n, i):
    # i is nothing but root element
    largest = i 
    l = 2*i+1
    r = 2*i+2
    if l<n and arr[l]>arr[largest]:
        largest = l
    if r<n and arr[r]>arr[largest]:
        largest = r
    if largest!=i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n=len(arr)
    for i in range(int(n/2-1), -1, -1):
        heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def partition(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]
    while start<end:
        while arr[start]<=pivot and start<end:
            start+=1

        while arr[end]>pivot:
            end-=1
        
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    return end

def quick_sort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        quick_sort(arr, start, p-1)
        quick_sort(arr, p+1, end)


    
