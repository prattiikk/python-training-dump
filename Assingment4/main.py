'''
TUPLE – Coding Questions
1. Write a program to find the maximum and minimum elements in a tuple.
2. Convert a list of tuples into a dictionary.
3. Count the occurrence of an element in a tuple without using built-in methods.
4. Create a tuple with mutable elements and modify the mutable data inside it.
5. Write a program to swap two tuples.
'''

def maxNmin(t):
    min_val = t[0]
    max_val = t[0]

    for x in t:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x

    return min_val, max_val


def list_of_tuples_to_dict(pairs):
    d = {}
    for key, value in pairs:
        d[key] = value
    return d



def count_occurrence(t, target):
    cnt = 0
    for x in t:
        if x == target:
            cnt += 1
    return cnt



def modify_mutable_in_tuple():
    t = ([1, 2, 3], "hello", [10, 20])

    t[0][1] = 99       # changes 2 -> 99
    t[2].append(30)    # [10, 20, 30]
    return t


def swap_tuples(a, b):
    temp = a
    a = b
    b = temp
    return a, b


def main():

    t1 = (5, 2, 9, 1, 7)
    mn, mx = maxNmin(t1)
    print("Tuple:", t1)
    print("Min:", mn)
    print("Max:", mx)
    print("------" * 3)

    pairs = [("Aman", 91), ("Bhakti", 70), ("Chetan", 81)]
    d = list_of_tuples_to_dict(pairs)
    print("Pairs:", pairs)
    print("Dictionary:", d)
    print("------" * 3)

    t2 = (1, 2, 3, 2, 2, 4, 2)
    target = 2
    cnt = count_occurrence(t2, target)
    print("Tuple:", t2)
    print("Count of", target, ":", cnt)
    print("------" * 3)

    modified = modify_mutable_in_tuple()
    print("Modified tuple with mutable elements:", modified)
    print("------" * 3)

    a = (10, 20)
    b = (30, 40, 50)
    print("Before swap:", "a =", a, ", b =", b)
    a, b = swap_tuples(a, b)
    print("After  swap:", "a =", a, ", b =", b)

main()