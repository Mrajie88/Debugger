def BubbleSort(array):
    if(type(array)!= list):
        return
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if(array[j] < array[j+1]):  # fault here
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

#if __name__ == '__main__':
#    print(BubbleSort([2,2,1,3,4,5,6,1,1,1]))