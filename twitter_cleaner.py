import nltk
import re
import pandas
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('omw-1.4')

tweets_df  = pandas.read_csv('out/tweets.csv')
sw_eng = []
with open('stopwords_eng.txt') as f:
    sw_eng = f.read().splitlines()
sw_bm = []
with open('stopwords_bm.txt') as f:
    sw_bm = f.read().splitlines()

def remove_pattern(text, pattern_regex):
    r = re.findall(pattern_regex, text)
    for i in r:
        text = re.sub(i, '', text)
    return text

tweets_df['tidy_tweets'] = np.vectorize(remove_pattern)(tweets_df['tweet'], "@[\w]*: | *RT*")

cleaned_tweets = []

for index, row in tweets_df.iterrows():
    # Here we are filtering out all the words that contains link
    words_without_links = [word for word in row.tidy_tweets.split()        if 'http' not in word]
    cleaned_tweets.append(' '.join(words_without_links))

tweets_df['tidy_tweets'] = cleaned_tweets

tweets_df.drop_duplicates(subset=['tidy_tweets'], keep='last', inplace=True)
tweets_df['absolute_tidy_tweets'] = tweets_df['tidy_tweets'].str.replace("[^a-zA-Z# ]", "")

stopwords_eng = set(stopwords.words('english'))
stopwords_id = set(stopwords.words('indonesian'))
cleaned_tweets = []

for index, row in tweets_df.iterrows():
    # filerting out all the stopwords 
    data = [s.lower() for s in row.absolute_tidy_tweets.split()]
    data = [word for word in data if not word in stopwords_eng]
    data = [word for word in data if not word in stopwords_id]
    data = [word for word in data if not word in sw_eng]
    data = [word for word in data if not word in sw_bm]
    # finally creating tweets list of tuples containing stopwords(list) and sentimentType 
    cleaned_tweets.append(' '.join(data))

tweets_df['absolute_tidy_tweets'] = cleaned_tweets

## Tokenization
#tokenized_tweet = tweets_df['absolute_tidy_tweets'].apply(lambda x: x.split())
#
## Finding Lemma for each word
#word_lemmatizer = WordNetLemmatizer()
#tokenized_tweet = tokenized_tweet.apply(lambda x: [word_lemmatizer.lemmatize(i) for i in x])
##joining words into sentences (from where they came from)
#for i, tokens in enumerate(tokenized_tweet):
#    tokenized_tweet[i] = ' '.join(tokens)
#    tweets_df['absolute_tidy_tweets'] = tokenized_tweet

df_final = tweets_df['absolute_tidy_tweets']
df_final.to_csv('out/tweets_cleaned.csv', index=False)
