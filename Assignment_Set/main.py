'''

SET – Coding Questions
1. Write a program to find the union, intersection, difference, and symmetric difference of two sets.
2. Remove common elements from two sets.
3. Write a program to check whether one set is a subset of another.
4. Iterate over a set and print only elements greater than a given number.
5. Given a list with duplicate values, convert it into a set and back to a list with unique elements.

'''


def basic_set_ops(a, b):
    union_m = a.union(b)
    inter_m = a.intersection(b)
    diff_m = a.difference(b)
    symdiff_m = a.symmetric_difference(b)
    return union_m, inter_m, diff_m, symdiff_m


def remove_common(a, b):
    common = a.intersection(b)
    a_without_common = a - common
    b_without_common = b - common
    return a_without_common, b_without_common



def is_subset(small, big):
    return small <= big


def print_greater_than(s, k):
    for x in s:
        if x > k:
            print(x)


def unique_list(lst):
    unique_set = set(lst)
    unique_list_result = list(unique_set)
    return unique_list_result



def main():
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}


    u_m, i_m, d_m, sd_m = basic_set_ops(A, B)
    print("A:", A)
    print("B:", B)

    print("Union :", u_m)
    print("Intersection :", i_m)
    print("Difference :", d_m)
    print("SymDiff :", sd_m)
    print("------" * 3)

    a_nc, b_nc = remove_common(A, B)
    print("A without common:", a_nc)
    print("B without common:", b_nc)
    print("------" * 3)

    small = {3, 4}
    big = {2, 3, 4, 5}
    print("Is", small, "subset of", big, "?", is_subset(small, big))
    print("Is {7} subset of", big, "?", is_subset({7}, big))
    print("------" * 3)

    S = {10, 3, 7, 15, 1}
    print("Elements in", S, "greater than 6:")
    print_greater_than(S, 6)
    print("------" * 3)

    lst = [1, 2, 2, 3, 1, 4, 4, 5]
    print("Original list:", lst)
    print("Unique :", unique_list(lst))

main()