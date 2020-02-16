"""
numbers = [15, 23, 4, 42, 8, 16]
numbers.sort()
print(numbers)
numbers.sort(reverse = True)
print(numbers)
"""

"""
letters = ["g", "a", "c", "b", "d", "e", "f"]
letters.sort()
print(letters)
"""

"""
words = ["peach", "ver3", "Python", "Pokemon", "ver2"]
words.sort()
print(words)
"""

"""
numbers = [15, 23, 4, 42, 8, 16]
#numbers_ascend = sorted(numbers)
#print(numbers_ascend)
#print(numbers)
#numbers_descend = sorted(numbers, reverse = True)
#print(numbers_descend)
#print(numbers)
numbers.reverse()
print(numbers)
"""

"""
import random
numbers = list(range(10))
random.shuffle(numbers)
print(numbers)
"""


words = ["chest", "wind", "holiday", "knight", "silence", "hot"]
#words.sort(key = len)
#print(words)
new_words = sorted(words, key = str.lower)
print(new_words)
