# Python String Practice Questions

# 1. Indexing and Slicing
#    Given the string s = "PythonPractice", what are the outputs of:
#    - s[1]
#    - s[-3:]
#    - s[2:7]

s = "PythonPractice"
print(s[1])      # Output: 'y'
print(s[:])
print(s[-3:])    # Output: 'ice'
print(s[2:7])    # Output: 'thonP'
print(s[::-1])


# 2. Reverse a String
#    Write a one-liner to reverse the string "developer" using slicing

# print('developer'[::-1])  # Output: 'repoleved'
# print(''.join(reversed('developer')))    # Output: 'repoleved'

li = ['d', 'e', 'v', 'e', 'l', 'o', 'p', 'e', 'r']
# Output: ['r', 'e', 'p', 'o', 'l', 'e', 'v', 'e', 'd']
# print(list(reversed(li)))

# 3. Count Vowels
#    Write a function that counts the number of vowels in a given string.


def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(2 for char in s if char in vowels)
    return count


print(count_vowels("Ashish"))


def count_vowels1(s):
    vowels = "aeiouAEIOU"
    count = 0
    for car in s:
        if car in vowels:
            count += 1
    return count


print(count_vowels1("Sareshma"))


# 4. Check for Palindrome
#    Write a function to check if a given string is a palindrome. Ignore spaces and capitalization.

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


print(is_palindrome("pa  ap"))


def is_pal(str):
    str = str.replace(" ", "").upper()
    str1 = str[::-1]
    return str1 == str


print(is_pal("race car"))  # Output: True


# 5. Clean and Format String
#    Given text = "   hello world! welcome to Python.   ", write code to:
#    - Remove leading/trailing spaces
#    - Capitalize each word
#    - Replace the word "Python" with "Programming"

text = "   hello world! welcome to Python.   "
text = text.rstrip()  # Remove trailing spaces
text = text.lstrip()  # Remove leading spaces
text = text.strip()  # Remove leading/trailing spaces
# print(text)
# print(text.capitalize())  # capitalize first letter of the string
# print(text.title())  # Capitalize each word
# Replace "Python" with "Programming"
# print(text.replace("Python", "Programming"))  # replace word in string


# 6. Find Longest Word
#    Write a function that takes a sentence and returns the longest word in it.

def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest


# print(longest_word(string))  # Output: ''


def longest_word1(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if "-" in word:
            word = word.replace("-", "")
        if len(word) > len(longest):
            longest = word
    return longest


string = "The quick-brown fox jumps over the lazy dog"
print(longest_word1(string))  # Output: 'quickbrown'

# 7. String Operators
#    Given s1 = "Py" and s2 = "thon", what are the results of:
#    - s1 + s2
#    - s1 * 3
#    - "y" in s1

s1 = "Py"
s2 = "thon"

print(s1 + s2)  # Output: 'Python'
print(s1 * 3)  # Output: 'PyPyPy'
print("y" in s2)  # Output: False
print("y" in s1)  # Output: True


# 8. Remove Duplicate Characters
#    Write a function that removes all duplicate characters from a string but keeps the first occurrence.

def remove_duplicates(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)
    # return ''.join()


print(remove_duplicates("programming"))  # Output: 'progamin'


# 9. Check for Anagram
#    Write a function that returns True if two strings are anagrams of each other.

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)


print(are_anagrams("listen", "silent"))  # Output: True

# str = "ashish"
# print(sorted(str))

# 10. Word Frequency Counter
#     Write a function that takes a sentence and returns a dictionary of word frequencies.


def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


# Output: {'this': 3, 'is': 2, 'a': 2, 'test.': 1, 'only': 1}
# word_ferquency("This is a test. This test is only a test.")
dic = {
    'a': 2,
    'is': 2,

}
dic.append.get('c', "ashsih")
print(dic)  # Output: 'ashsih'
# print(dic['a'])
# dic[a] = 2
# dic[0] = 2
