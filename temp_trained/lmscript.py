import os
import preprocessData as pd
import numpy as np
import re


def main():
    trainArticles = pd.preprocessData("../trainingSet.dat", "../trainingSetLabels.dat")
    four_grams = []
    perplexity = []
    for article in trainArticles:
        fp = open('red.txt', 'w')
        len_article = 0
        for sentence in article.allSentences:
            len_article += sentence.length
            fp.write(sentence.string)
            fp.write('\n')
        fp.close()
        os.system('echo "perplexity -text red.txt" | ./evallm -binary a.binlm > dummy.txt')
        op = open('dummy.txt')
        lines = op.readlines()
        items = re.split(',', lines[2])
        per = float(items[0].split('=')[1].strip())
        perplexity.append(per)
        items = lines[4].strip().split('=')

        fourG = int(items[1].strip().split(' ')[0])
        fourG = float(fourG)/len_article
        os.system('echo "perplexity -text red.txt" | ./evallm -binary a.binlm')
        four_grams.append(fourG)


    print 'bla'




if __name__ == '__main__':
    main()
