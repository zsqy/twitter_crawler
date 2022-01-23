import nltk
import pandas as pd

with open ("out/tweets_cleaned.csv", "r") as myfile:
    data=myfile.read().replace('\n', ' ')
    
    data = data.split(' ')
    data = [s.lower() for s in data]
    data = [s.replace('#', '') for s in data]

    fdist1 = nltk.FreqDist(data)
    pd.DataFrame(fdist1.most_common(20000), columns=['word', 'count']).to_csv('out/wordcount.csv', index=False)
