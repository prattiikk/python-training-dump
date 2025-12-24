'''
STRING – Coding Questions
1. Write a program to count the number of vowels, consonants, digits, and special characters in a given string.
2. Given a string, reverse each word individually without changing the word order.
3. Check whether a given string is a palindrome using indexing and slicing.
4. Write a program to find the frequency of each character in a string.
5. Demonstrate string immutability by attempting to modify a character and handling the error.
'''

def count(string):
    vowels = 0
    consonants = 0
    digits = 0
    special = 0

    vowel_set = "aeiouAEIOU"

    for ch in string:
        if ch in vowel_set:
            vowels += 1
        elif ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            consonants += 1
        elif '0' <= ch <= '9':
            digits += 1
        else:
            special += 1

    return vowels, consonants, digits, special



def reverse_each_word(string):
    words = string.split()
    new_string = ""
    for w in words:
        new_string += w[::-1]
        new_string += " "
    return new_string.strip()


def is_palindrome(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


def frequency(string):
    freq = {}
    for ch in string:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq


def demonstrate_immutability(s):
    try:
        s[0] = 'X'
    except TypeError as e:
        return str(e)
    return "No error (unexpected)"


def main():
    s = "Hello World 123! hello"

    v, c, d, sp = count(s)
    print("String:", s)
    print("Vowels:", v)
    print("Consonants:", c)
    print("Digits:", d)
    print("Specials:", sp)
    print("------" * 3)

    rev_words = reverse_each_word(s)
    print("Reverse each word:", rev_words)
    print("------" * 3)

    p1 = "madam"
    p2 = "hello"
    print(p1, "is palindrome?", is_palindrome(p1))
    print(p2, "is palindrome?", is_palindrome(p2))
    print("------" * 3)

    freq_map = frequency(s)
    print("Frequency map:")
    for ch in (freq_map.keys()):
        print(ch, "->", freq_map[ch])
    print("------" * 3)

    err_msg = demonstrate_immutability(s)
    print("Immutability error message:", err_msg)


main()
