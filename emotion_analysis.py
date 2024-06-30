# nltk.download('stopwords')
import pandas as pd
import re
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

election_data=pd.read_excel("result/US Presidential Election2000.xlsx")
text_series = election_data['content']
date_series = election_data['createdb']
# print(text)
# text = "This is an example sentence to demonstrate stopword removal."
filtered_tokens=[]
filtered_texts =[]
for text in text_series:

    text=re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\$\$,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)

    tokens = text.split()  # 分词
    tokens = [token.lower() for token in tokens]
    tokens = [token for token in tokens if token.isalpha()]
    filtered_texts.append(text)
    filtered_tokens.append([word for word in tokens if word.lower() not in stop_words])

# print(text_series[0])
# print(filtered_tokens[0])
scores=[]
from Get_subject_sentiment import get_subject_sentiment

for sentence in filtered_texts:
    sentiment_scores = get_subject_sentiment(sentence)
    # print(sentiment_scores)
    scores.append(sentiment_scores)

data = {'date': date_series, 'sentiment': scores}
df = pd.DataFrame(data)
df.to_excel('result/scores_data.xlsx',index_label='rowno')



