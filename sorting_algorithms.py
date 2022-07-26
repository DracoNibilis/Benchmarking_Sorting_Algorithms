# Algorithms - measuring the running time
# Author: Magdalena Malik
# CTA Project 

# import needed modules
import numpy as np # count mean values
import time # count time of runs
import random # generate an array of random values
import pandas as pd # create table of data
import matplotlib.pyplot as plt # plot data

# *** Bubble Sort ***
def bubble_sort(arr):
    # check the last element of array
    indexing_length = len(arr) - 1
    # set false to continue checking
    sorted = False
    while not sorted:
        sorted = True
        # Loop through arra to compare elements
        for i in range(0, indexing_length):
            # check condition is first element is bigger then following
            if arr[i] > arr[i+1]:
                sorted = False
                # Swap elements after comparison
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
    
# *** Quick Sort Algorithm ***
def quick_sort(arr):
    lenght = len(arr)
    # Set lenght of the set
    if lenght < 1:
        return arr
    else:
        # Pick pivot
        pivot = arr.pop()
    # create subbarays / left and right / 
    items_greater = []
    items_lower = []
    # Loop through array 
    for item in arr:
        # fill subbarays with data
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)     
    # return recursive call to reapeat steps 
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

# *** Bucket Sort Algorithm ***
def bucket_sort(array):
    
    largest = max(array)
    length = len(array)
    size = largest/length
    # Create Buckets
    buckets = [[] for i in range(length)]
    # Looping through array  
    for i in range(length):
        index = int(array[i]/size)
        # Fill buckets 
        if index != length:
            buckets[index].append(array[i])
        else:
            buckets[length - 1].append(array[i])
    # Sorting Individual Buckets  
    for i in range(len(array)):
        buckets[i] = sorted(buckets[i])
    # Flattening the Array
    result = []
    for i in range(length):
        result = result + buckets[i]        
    return result

# *** Insertion Sort Algorithm ***
def insertion_sort(array):
    # Set the lentght of array 
    index_lenght = range(1, len(array))
    # Loop through array
    for i in index_lenght:
        # Set the key value 
        value_to_sort = array[i]
        # Move values which are greater than a key 
        while array[i-1] > value_to_sort and i>0:
            # Swap values
            array[i], array[i-1] = array[i-1], array[i]
            # Decrement value i 
            i = i-1
    return array    

# *** Selection Sort Algorithm ***
def selection_sort(array):
    # Set index lenght 
    index_length = range(0, len(array)- 1)
    # Loop through array 
    for i in index_length:
        # Set minimum value 
        min_value = i
        # Loop through rest of the set
        for j in range(i+1, len(array)):
            # Check value if smaller then minimum 
            if array[j] < array[min_value]:
                # Swap the value with minimum 
                min_value = j
        # Check other values 
        if min_value != i:
            # Swap values
            array[min_value], array[i] = array[i], array[min_value]
    return array
     
# Array for input sizes
size_array = [120, 240,500,  800, 1200 ,2400,  4800, 12000]

# time array 
time_array = []

# generate random array
def random_array(n):
    rand_array = []
    for i in range(0,n,1):
        rand_array.append(random.randint(0,100))
    return rand_array

# generate time array for bubble sort
def bubble_timing(gen_array):
    time_array= []
    x = 10
    while x != 0:
        # time check
        start_time = time.time()
        # call sorting function
        arr_sorted = bubble_sort(gen_array)
        end_time = time.time()
        #end time check
        time_elapsed = end_time - start_time
        # list of times 
        time_array.append(time_elapsed)
        # decrease value to get 10 runs
        x-=1
    return time_array
        
# create and fill array of mean times for n trials 
bubble_mean_array = []
for i in size_array:
    gen_array = random_array(i)
    new_array = bubble_timing(gen_array)
    mean_of_times = round(np.mean(new_array),3)
    bubble_mean_array.append(mean_of_times)
    
# generate time array for quick sort
def quick_timing(gen_array):
    time_array= []
    x = 10
    while x != 0:
        # time check
        start_time = time.time()
        # call sorting function
        arr_sorted = quick_sort(gen_array)
        end_time = time.time()
        # end time check
        time_elapsed = end_time - start_time
        # list of times
        time_array.append(time_elapsed)
        # decrease value to get 10 runs
        x-=1
    return time_array
        
# create and fill array of mean times for n trials 
quick_mean_array = []
for i in size_array:
    gen_array = random_array(i)
    new_array = quick_timing(gen_array)
    mean_of_times = round(np.mean(new_array),3)
    quick_mean_array.append(mean_of_times)
    
# generate time array for bucket sort
def bucket_timing(gen_array):
    time_array= []
    x = 10
    while x != 0:
        # time check
        start_time = time.time()
        # call sorting function
        arr_sorted = bucket_sort(gen_array)
        end_time = time.time()
        # end time
        time_elapsed = end_time - start_time
        # list of times
        time_array.append(time_elapsed)
        # decrease value to get 10 runs
        x-=1
    return time_array
        
# create bucket sort mean times array
bucket_mean_array = []
for i in size_array:
    gen_array = random_array(i)
    new_array = bucket_timing(gen_array)
    mean_of_times = round(np.mean(new_array),3)
    bucket_mean_array.append(mean_of_times)

# generate times array for insertion sort
def insertion_timing(gen_array):
    time_array= []
    x = 10
    while x != 0:
        # time check
        start_time = time.time()
        # call sorting function
        arr_sorted = insertion_sort(gen_array)
        end_time = time.time()
        time_elapsed = end_time - start_time
        time_array.append(time_elapsed)
        #print("time elapsed", time_elapsed)
        x-=1
    return time_array
        
# create and fill array of mean times for n trials 
insertion_mean_array = []
for i in size_array:
    gen_array = random_array(i)
    new_array = insertion_timing(gen_array)
    mean_of_times = round(np.mean(new_array),3)
    insertion_mean_array.append(mean_of_times)

# generate times array for selection sort       
def selection_timing(gen_array):
    time_array= []
    x = 10
    while x != 0:
        
        # time check
        start_time = time.time()
        # call sorting function
        arr_sorted = selection_sort(gen_array)
        end_time = time.time()
        # end time check
        time_elapsed = end_time - start_time
        # list of times
        time_array.append(time_elapsed)
        # decrease value to get 10 runs
        x-=1
    return time_array
        
# create and fill array of mean times for n trials 
selection_mean_array = []
for i in size_array:
    gen_array = random_array(i)
    new_array = selection_timing(gen_array)
    mean_of_times = round(np.mean(new_array),3)
    selection_mean_array.append(mean_of_times)
 
# array to generate table with all data
# array of times
table_array = [bubble_mean_array, quick_mean_array, bucket_mean_array, insertion_mean_array, selection_mean_array]

# array of names of algorithms
sort_alg = [ "Bubble Sort", "Quick Sort", "Bucket Sort", "Insertion Sort", "Selection Sort" ]

# create table by Pandas 
df = pd.DataFrame(table_array, columns = ["120", "240", "500", "800", "1200", "2400", "4800", "12000"], index =[ "Bubble Sort", "Quick Sort", "Bucket Sort", "Insertion Sort", "Selection Sort" ] )
# display table in prompt
print("=== TABLE OF TIMES (mean per 10 runs) ===")
print(df)

# plotting data 
# create seperate plots for each type of sorting algorithm
# labeled accordingly
plt.plot(size_array, bubble_mean_array, label="Bubble Sort")
plt.plot(size_array, quick_mean_array,  label="Quick Sort")
plt.plot(size_array, bucket_mean_array, label="Bucket Sort")
plt.plot(size_array, insertion_mean_array, label="Insertion Sort")
plt.plot(size_array, selection_mean_array,  label="Selection Sort")
# Set x and y labels ( input size and running time )
plt.xlabel("input size n")
plt.ylabel("running time")
# Set legend
plt.legend()
# Save plot to file
plt.savefig("time_plot.png")
# Show plot
plt.show()
