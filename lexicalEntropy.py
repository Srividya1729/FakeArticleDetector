import preprocessData as pd
import numpy as np
from nltk.stem import PorterStemmer
from nltk.tokenize import  word_tokenize
from nltk.stem import WordNetLemmatizer


def calculateEntropy(article_tokens):
    typeDict = dict()
    for token in article_tokens:
        if typeDict.get(token, None) is None:
            typeDict[token] = 1
        else:
            typeDict[token] += 1


    sum = 0
    N = len(article_tokens)
    for key in typeDict.keys():
        p = typeDict[key]/float(N)
        sum += p * np.log2(p)

    return -sum

def main():

    train_data = pd.preprocessData('trainingSet.dat', 'trainingSetLabels.dat')
    ps = PorterStemmer()
    wordnet_lemmatizer = WordNetLemmatizer()
    entropy = []
    for article in train_data:
        article_tokens = []
        for sentence in article.allSentences:
            word_tokens = word_tokenize(sentence.string.upper())
            # word_tokens = [wordnet_lemmatizer.lemmatize(w).upper() for w in word_tokens]
            article_tokens.extend(word_tokens)

        entropy.append(calculateEntropy(article_tokens))

    return entropy









if __name__ == '__main__':
    main()