import numpy as np

ar = np.array([[1, 2, 3], [4, 5, 6]])
ar2 = np.array([[10, 23, 11], [22, 50, 42]])


def Replace(m, n, ar):

    for i in range(len(ar)):
        for j in range(len(ar[i])):
            if i and j == m-1 and n-1:
                ar[i][j] = int(input('Enter The Value to be Replaceed: '))
    return ar


def trasverse(ar):
    '''Iterating The Each Value of the Array'''
    for i in range(len(ar)):
        for j in range(len(ar[i])):  # <-- With Logic
            print(ar[i][j])

            # OR
            
    print('\n')
    for i in ar.flat:    # <-- With Numpy arrays Properties
      print(i)  

def append_atEnd(ar, ar2,):
    ar = np.append(ar, ar2, axis=int(
        input('Axis Where to Insert The Other Array{0 for row,1 for column}: ')))
    return ar


def insert_atSpecificIndex(arod):
    '''Insert a Value at a specific index without PoppingAny exsiting Value of array ,
    Values Got shift after the value to right {Only one dimensional}'''
    t = int(input('Enter The Index where you want to insert the Value: '))-1
    for i in range(len(arod)):
        if i == t:
            arod = np.insert(
                arod, t, [int(input('Enter the Value to add in Array: '))])
            break
    return arod


def sorting(ar):
    '''Sorts the array of Integers Values'''
    res = np.sort(ar)
    return res


def search(ar):
    '''Search the array of Integers Values'''
    vts = int(input("Enter the Value to search in the array: "))
    rows, cols = np.where(ar == vts)
    return rows, cols


if __name__ == '__main__':

    trasverse(ar2)  # trasversing the array

    res = ar.flatten()  # flatten the array to One dimensional

    print(res, "\n")

    print(sorting(ar2))

    print(f'Value U wanted To search is Found At Index: [][{search(ar2)}]',)

    # insert the value at specific index of the array {Only one dimensional}
    print(insert_atSpecificIndex(res))
