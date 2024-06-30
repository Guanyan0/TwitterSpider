import nltk
import spacy

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# nltk.download('vader_lexicon')  # 第一次需安装

nlp = spacy.load("en_core_web_sm-3.0.0/en_core_web_sm/en_core_web_sm-3.0.0")
sid = SentimentIntensityAnalyzer()
from utils.Check_keywords import contains_keywords

def get_subject_sentiment(sentence):
    keywords_1 = ['Trump', 'Republican', 'Republicans']
    keywords_2 = ['Biden', 'democrat', 'democratic']
    substrings_1 = ['Trump', 'Republican', 'Republicans']
    substrings_2 = ['Biden', 'democrat', 'democratic']
    doc = nlp(sentence)
    scores = []

    for token in doc:
        # 判断token是否为主语
        if token.dep_ == "nsubj":
            # 提取包含主语的子句
            root = token.head
            clause = " ".join([tok.text for tok in root.subtree])
            # 进行情感分析
            sentiment_score = sid.polarity_scores(clause)
            # 存储主语和情感倾向compound
            if contains_keywords(keywords_1,substrings_1,token.text):
                scores.append(('r',token.text, sentiment_score['compound']))
            if contains_keywords(keywords_2,substrings_2,token.text):
                scores.append(('d',token.text, sentiment_score['compound']))
        if token.dep_ == "nsubjpass":
            root = token.head
            clause = " ".join([tok.text for tok in root.subtree])
            # 进行情感分析
            sentiment_score = sid.polarity_scores(clause)
            # 存储主语和情感倾向compound
            if contains_keywords(keywords_1, substrings_1, token.text):
                scores.append(('r', token.text, sentiment_score['compound']))
            if contains_keywords(keywords_2, substrings_2, token.text):
                scores.append(('d', token.text, sentiment_score['compound']))
    return scores


# 示例句子
# sentence = "the dog was loved by man"
# # The quick brown fox jumps over the lazy dog. The dog seems sad
#
# # 获取主语和情感倾向compound
# scores = get_subject_sentiment(sentence)
#
# # 打印结果
# for subject, compound in scores:
#     print(f"主语: {subject}, 情感倾向compound: {compound}")