#Annotation:
print("Speaker’s Name: Greta Thunberg")
print("Date of Talk: November 2018")
print("Title of the Talk: The disarming case to act right now on climate change")
print("Length of the Talk: 11:02")
print("Source: https://www.ted.com/talks/greta_thunberg_the_disarming_case_to_act_right_now_on_climate_change#t-259530")


import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import re


#Reading the Text:
text= open('text.txt', encoding='utf-8').read()
print("the length of the speech before cleaning:", len(text))
print('\n')

#Cleaning the Text (the Talk/ Speeches):

#1- convert the Text to lower case:

lower_case= text.lower()
#print(lower_case)

# 2- Remove the timer:

def timer_eliminator(text):
    text = re.sub(r"[0-9][0-9]:[0-9][0-9]", '', text)
    return text
#print("Removing time:\n")
no_timer_text = timer_eliminator(lower_case)
#print(no_timer_text)

# 3- Remove words in Brackets:

def brackets_eliminator(text):
    text = re.sub(r"[(]applause[)]", '', text)
    text = re.sub(r"[(]laughter[)]", '', text)
    return text

#print("Removing brackets:\n")
#print(brackets_eliminator(no_timer_text))
no_brackets_text = brackets_eliminator(no_timer_text)


# 4- Remove Punctuation:

cleaned_text= no_brackets_text.translate(str.maketrans('','',string.punctuation))
#print("cleaned text:\n")
#print(cleaned_text)
#print("the length of the text without punctuation:", len(cleaned_text))
#print('\n')

# 5- Remove spaces and lines breaks:

def space_eliminator(text):
    text= re.sub('\n+', ' ', text)
    text= re.sub(' +', ' ', text)

    return text

#print("Removing Speces:\n")
#print(space_eliminator(cleaned_text))
#print('\n')
#print("the length of the text without spaces:", len(space_eliminator(cleaned_text)))


# 6- Tokenization:

tokenized_text= word_tokenize(cleaned_text)
#print('\n')
#print("Tokenized Text:", tokenized_text)

# 7- Remove stop words:

stop_words= stopwords.words('english')
#print('\n')
#print("Stop Words:\n")
#print(stop_words)


text_without_stopwords= []
for word in tokenized_text:
    if word not in stop_words:
        text_without_stopwords.append(word)

#print('\n')
#print("Text without stop words:\n")
#print(text_without_stopwords)
#print("The length of the Text without stop words:", len(text_without_stopwords))

# THE READY TO GO TEXT:
#print("The Final version of the text:", text_without_stopwords)
#print("The Final version of the text:", len(text_without_stopwords))
final_text= text_without_stopwords

# Build the Sentiment analyser:

# 1- Reading the texts:

positve_list = word_tokenize(open('positive-words.txt', encoding='utf-8').read())

negative_list = word_tokenize(open('negative-words.txt', encoding='utf-8').read())

# 2- Building the function:

def sentiment_analyser(final_text):
    positive = 0
    negative = 0

    for word in final_text:
        if word in positve_list:
            positive = positive +1
        if word in negative_list:
            negative = negative +1

    if (positive > negative):
        print()
        #print("Text is positiv")
    elif (negative > positive):
        print()
        #print("Text is negative")
    else:
        print()
        #print("Text is neutral")

    #print("positive words number: ", positive)
    #print("negative words number: ", negative)

sentiment_analyser(final_text)

