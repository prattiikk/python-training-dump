'''
LIST – Coding Questions
1. Write a program to remove duplicate elements from a list without using set.
2. Given a list of numbers, create a new list containing only even numbers using list comprehension.
3. Write a program to find the second largest element in a list.
4. Create a nested list and calculate the sum of each inner list.
5. Demonstrate shallow copy and deep copy of a list with mutable elements.
'''



def remove_duplicates(lst):
    unq = []
    for n in lst:
        if n not in unq:
            unq.append(n)
    return unq

def keep_even(lst):
    return [x for x in lst if x % 2 == 0]

def sec_largest(lst):
    largest = None
    second = None
    for n in lst:
        if largest is None or n > largest:
            second = largest
            largest = n
        elif n < largest and ( (second is None) or n > second ):
            second = n
    return second

def inner_list_sum(lst):
    sum = []
    for inner_list in lst:
        x = 0
        for n in inner_list:
            x += n
        sum.append(x)
    return sum


import copy

def demonstrate_copies():
    original = [[1, 2], [3, 4]]
    shallow = original[:]
    deep = copy.deepcopy(original)

    # Modify inner list in the original
    original[0][0] = 99

    print("Original:", original)     # [[99, 2], [3, 4]]
    print("Shallow:", shallow)       # [[99, 2], [3, 4]]  -> affected
    print("Deep   :", deep)          # [[1, 2], [3, 4]]   -> not affected







def main():

    data = [1, 3, 2, 3, 1, 4, 2, 5, 5]
    print("Original:", data)
    print("Without duplicates:", remove_duplicates(data))
    print("------" * 3)


    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    print("Evens (list comprehension):", keep_even(nums))
    print("------" * 3)

    a = [10, 5, 20, 8, 20, 3]
    print("Second largest:", sec_largest(a))
    print("------" * 3)

    nested = [[1, 2, 3], [10, 0], [5, 5, 5], []]
    print("Nested:", nested)
    print("Sum of each inner list:", inner_list_sum(nested))
    print("------" * 3)

    demonstrate_copies()


main()