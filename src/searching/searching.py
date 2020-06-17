def linear_search(arr, target): # ==> 0(n)
    # Your code here
    print(arr, target)
    for i in arr:  #0(n)
        if i == target:
            print(i)
            return True
        
    print(False)
    return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    # get the first item
    low = 0
    # get the last item
    high = len(arr) - 1
    # while the first item is less than the last, do

    while low < high :
        middle = (low + high) // 2
        guess = arr[middle]

        if guess == target:
            print(guess, target)
            return guess
        elif target < guess:
           high = middle - 1
        elif target > guess:
            low = middle + 1

    print("Number not found")
    return -1  # not found


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
linear_search(arr, 5)
binary_search(arr, 5)
