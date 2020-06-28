
# O(n^2)
def selectionSorting(arr) :

    for i in range(len(arr)-1) :
        
        imin = i
        for j in range(i+1,len(arr)) :
            if arr[j] < arr[imin] :
                imin = j
        arr[i] , arr[imin] = arr[imin] , arr[i]

    return arr


# O(n^2)
def bubbleSorting(arr) :

    for i in range(1,len(arr)) :

        flag = 0
        for j in range(0,len(arr)-i) :
            if arr[j] > arr[j+1] :
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                flag = 1
        
        if not flag :
            break

    return arr 
    

# O(n^2)
def insertionSorting(arr) :
    
    for i in range(1,len(arr)) :
        
        value = arr[i]
        hole = i

        while hole > 0 and arr[hole-1] > value :
            arr[hole] = arr[hole-1]
            hole -= 1

        arr[hole] = value

    return arr



lst = [7,2,4,1,5,3]
#print(insertionSorting(lst))
#print(selectionSorting(lst))
print(bubbleSorting(lst))