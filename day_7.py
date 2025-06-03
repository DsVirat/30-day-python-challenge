# 🎯 Challenge
# - Count word frequencies in a text file

# # Approach 1 : without using the Counter Module 
#  ----------------------------------------------------------
# # Open the file 'my_file.txt' in read mode and read its entire content into the variable 'text'
# with open('my_file.txt','r') as f:
#     text = f.read()

# # Convert all characters in 'text' to lowercase for uniformity and split the text into individual words stored in the list 'words'
# words = text.lower().split()

# # Convert the list 'words' to a set to extract unique words only
# unique_words = set(words)

# # Print each unique word along with its count of occurrences in the original list
# print("Word:Count")
# for uni_word in unique_words:
#     print(f'{uni_word}:{words.count(uni_word)}')

# ----------------------------------------------------------

# Approach 2: Using the Counter Module

from collections import Counter

# Open the file 'my_file.txt' in read mode and read its entire content into the variable 'text'
with open('my_file.txt','r') as f:
    text = f.read()

# Convert all characters in 'text' to lowercase for uniformity and split the text into individual words stored in the list 'words'
words = text.lower().split()

# Counter returns a dictionary in which keys are words and values are their counts
words_count = Counter(words)

#Print each unique word along with its count of occurrences in the original file
print("Word:Count")
for word,count in words_count.items():
    print(f'{word}:{count}')
