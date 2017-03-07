def optbubblesort(array):
    size = len(array)
    for i in range (0, size):
        swapped = False
        for current in range(0, size-1):
            if array[current] > array[current+1]:
                temp = array[current]
                array[current] = array [current+1]
                array[current+1] = temp
                swapped = True
        if swapped == False:
            continue
    return array

def bubblesort(array):
    size = len(array)
    for i in range (0, size):
        for current in range(0, size-1):
            if array[current] > array[current+1]:
                temp = array[current]
                array[current] = array [current+1]
                array[current+1] = temp
    return array

def insertion(array):
    size = len(array)
    for j in range(0,size):
        # i = j
        while j>0 and array[j-1]>array[j]:
            temp = array[j]
            array[j] = array[j-1]
            array[j-1] = temp
            j-=1
    return array

def selection_sort(array):
    size = len(array)
    for j in range(0, size-1):
        min = j
        for i in range(j+1, size):
            if array[min] > array[i]:
                min = i
        temp=array[min]
        array[min] = array[j]
        array[j] = temp
    return array



array = [1,2,4,5,6,3,5,6,71,2,4,5,6,3,5,6,71,2,4,5,6,3,5,6,71,2,4,5,6,3,5,6,71,2,4,5,6,3,5,6,7]

print(bubblesort(array))
print(insertion(array))
print(optbubblesort(array))
print(selection_sort(array))
