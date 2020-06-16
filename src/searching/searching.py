def linear_search(arr, target): # ==> 0(n)
    # Your code here
    for i in arr: #0(n)
        if i == target:
            print(i)
            return i;
        print(False)
        return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    # get the first item
    low = 0
    # get the last item
    high = arr - 1
    # while the first item is less than the last, do
    while low < high:
        middle = (low + high) // 2
        guess = arr[middle]

    for i in range(len(arr) - 1, 0, -1):
        if guess == i:
            print(guess, i)
            return i
        else:
            print("Number not found")
            return "Number not found"

    return -1  # not found


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
linear_search(arr, 5)
