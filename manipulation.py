#the following command is to ask a user to enter a sentence
str_manip = input("what do you have with you ?") # user input : with me here is my bag

#the following command is to get the length of words the user input including spaces and punctuation marks
print(len(str_manip))

#the following command is to get the last letter from the user's input.[-1] is used because using negative indices is an easy way of starting the string from the back and -1 is the rightmost index 
last_letter = str_manip[-1]
print(last_letter)

#the following command will replace the last letter of the user's input with @
new_response = str_manip .replace("g", "@")
print(new_response)

#the following command will show the last three letters in reverse [-3:] will list the last three letters while [::-1] is the reverse command
last_3_letter_reverse = str_manip[-3:][::-1]
print(last_3_letter_reverse)

#the folowing command will display the five letter words which comprises of the first three letters and last two letters of the user's input
five_letter_words = str_manip[:3] + str_manip[-2:]
print(five_letter_words)
