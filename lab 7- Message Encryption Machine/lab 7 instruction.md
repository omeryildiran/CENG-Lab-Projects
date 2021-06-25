- In this lab, you are going to implement two separate functions named find_most_freq_char (40 points) and encrpyt_message (60 points):

#Function 1: find_most_freq_char(word)

word: A string that includes only alphabetical characters, e.g. "ilgili".

This function should return the most frequent character (e.g. "i" for the word "ilgili") in the word.

#Function 2: encrypt_message(message)

message: A string consisting of words separated by a space character, i.e. "word1 word2 word3 ... wordN".

This function should return a string that has the following properties:

1- For each word in message, you need to:

find the most frequent character (you can use the find_most_freq_char() function you implemented),
remove all occurrences of the most frequent character from the word.
2- You need to combine these modified words with the # character.

**Notes:**

The most frequent character (the character that occurs most in the word) should be calculated for each word.
There will be at least two unique characters in each word.
It is guaranteed that there will be only one character that has the maximum occurrence.
The inputs to both functions will always be lowercase alphabetical characters.
Warnings:

The order of characters in each word and the order of words in the string should be preserved. E.g., after removing character "a", "alaka" should become "lk" and not "kl".
Your function should receive its data via its parameters only. Your submitted solution must NOT use any input() function.
Your function should return its result. Your submitted solution must NOT print anything.