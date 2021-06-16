#Annotation:
print("Speaker’s Name: Greta Thunberg")
print("Date of Talk: November 2018")
print("Title of the Talk: The disarming case to act right now on climate change")
print("Length of the Talk: 11:02")
print("Source: https://www.ted.com/talks/greta_thunberg_the_disarming_case_to_act_right_now_on_climate_change#t-259530")


#Reading the Text:
text= open('text.txt', encoding='utf-8').read()
print("the length of the speech before cleaning:", len(text))


#Cleaning the Text (the Talk):

#1- convert the Text to lower case:
import string
lower_case= text.lower()
#print(lower_case)

# Remove the timer:
import re
def timer_eliminator(text):
    text = re.sub(r"[0-9][0-9]:[0-9][0-9]", '', text)
    return text
#print("Removing time:\n")
no_time_text = timer_eliminator(lower_case)
#print(no_time_text)

def brackets_eliminator(text):
    text = re.sub(r"[(]applause[)]", '', text)
    text = re.sub(r"[(]laughter[)]", '', text)
    return text

print("Removing brackets:\n")
#print(brackets_eliminator(no_time_text))

#Remove (applause)/ (Laughter):


#2- Remove Punctuation:
cleaned_text= lower_case.translate(str.maketrans('','',string.punctuation))
print(cleaned_text)
print("the length of the text without punctuation:", len(cleaned_text))

#3- Remove spaces and lines breaks:

def preprocess_text(text):
    text= re.sub('\n+', ' ', text)
    text= re.sub(' +', ' ', text)

    return text

print(preprocess_text(cleaned_text))
print(len(preprocess_text(cleaned_text)))


# Tokenization:
import nltk
from nltk.tokenize import word_tokenize
tokenized_text= word_tokenize(cleaned_text)
print(tokenized_text)

#remove stop words:
from nltk.corpus import wordnet
from nltk.corpus import stopwords
stop_words= stopwords.words('english')
print(stop_words)


text_without_stopwords= []
for word in tokenized_text:
    if word not in stop_words:
        text_without_stopwords.append(word)

print(text_without_stopwords)

print(len(text_without_stopwords))

positve_list = word_tokenize(open('positive-words.txt', encoding='utf-8').read())

negative_list = word_tokenize(open('negative-words.txt', encoding='utf-8').read())


def sentiment_analyzer(text):
    positive = 0
    negative = 0

    for word in text:
        if word in positve_list:
            positive = positive +1
        if word in negative_list:
            negative = negative +1

    if (positive > negative):
        print("Text is positiv")
    elif(negative > positive):
        print("Text is negative")
    else:
        print("Text is neutral")


    p_ratio = (int)(1000* positive/len(text))
    n_ratio = (int)(1000* negative/len(text))
    print("positive words ratio: ", p_ratio/1000)
    print("negative words ratio: ", n_ratio/1000)


sentiment_analyzer(text_without_stopwords)

