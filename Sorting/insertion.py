# insertion_sort
def insertion_sort(ar):
    for i in range(len(ar)):
        # key holds the current element that we are working with
        key = ar[i]
        # temp holds the current index of the key
        temp = i
        # while the current element is greater than 0 and the element before the current element is greater than 0 
        # swap the values of the current element with the one before it
        while(temp > 0 and ar[temp-1] > key):
            ar[temp] = ar[temp-1]
            temp -= 1
        ar[temp] = key
        

def display(ar):
    for i in range(len(ar)):
        print(ar[i])

myList = [8, 625, 100, 5, 1, 10, 20, 11, 100]

# Print the unsorted list
display(myList)

insertion_sort(myList)

display(myList)
