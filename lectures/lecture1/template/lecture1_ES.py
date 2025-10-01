"""
Part 2, Lecture 1

Implement and test argmax() function that returns the location of a maximum.

Tasks
-----

1.  Implement a function argmax() that takes a sequence of numbers and returns 
    the index (position) the maximum element.

2.  Test the function with the following sequence of numbers:
    [2, 3, -1, 7, 4]

3.  Add error handling if an empty sequence is passed. Test the function with an 
    empty sequence.

4.  Use the notebook lecture1-benchmark.ipynb to benchmark your implementation 
    against NumPy's argmax().
"""
import numpy as np

def argmax(lst):

    N = len(lst)

    if N == 0:
        raise ValueError("The input list is empty.")
    
    value_max = - np.inf

    for i in range(N):
        value = lst[i]
        if value > value_max:
            imax = i
            value_max = value

    return imax



if __name__ == "__main__": #only execute this when you run this python file, and not if its used in other files
    #values = [2, 3, -1, 7, 4]
    values = []
    try: 
        i = argmax(values)
        print(f"The maximum value is at index: {i}")
    except ValueError:
        print("Caught an exception: The input list is empty.")

