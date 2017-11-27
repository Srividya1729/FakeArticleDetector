#Sentence Object - Add more attributes as required
import math

class sentenceObj(object):

    def __init__(self, string="", length=0):
        self.string = string
        self.length = length

#Article Object - Add more attributes as required
class articleObj(object):

    def __init__(self, numberOfSentences=0, label=-1, allSentences=[]):
        self.numberOfSentences = numberOfSentences
        self.label = label
        self.allSentences = allSentences

#Creats an Article
def createArticle(numberOfSentences, label, allSentences):

    article = articleObj(numberOfSentences, label, allSentences)
    return article

#Creats a Sentence
def createSentence(string, length):

    sent = sentenceObj(string, length)
    return sent

#Preprocess Data
def preprocessData(data, labels):

    Labels = []
    with open(labels) as f:
        lines = f.readlines()

        for l in lines:
            l = l.strip()
            Labels.append(int(l))

    f.close()

    trainSet = []
    with open(data) as f:
        lines = f.readlines()

        for l in lines:
            l = l.strip()
            trainSet.append(l)

    f.close()

    iteration = 0
    global num
    global k
    k = 0
    allArticles = []

    for l in trainSet:

        if l == "~~~~~":

            if (k != 0):
                allArticles.append(createArticle(num, Labels[iteration], allSentences))
                iteration = iteration + 1
            else:
                k = 1

            num = 0
            allSentences = []

        else:

            l = l.lstrip("<s>")
            l = l.lstrip()

            l = l.rstrip("</s>")
            l = l.rstrip()

            allSentences.append(createSentence(l,len(l)))

            num = num + 1

    allArticles.append(createArticle(num, Labels[iteration], allSentences))

    return allArticles

########## POS Tagging ##############
import nltk
def pos_feat(art,real,fake,N_real,N_fake):

    for sent in art.allSentences:

        text = nltk.word_tokenize(sent.string)
        #print text
        pos_tags = nltk.pos_tag(text)
    #    print pos_tags
        first = pos_tags[0][1]
        last = pos_tags[-1][1]
    #    print art.label

        if art.label == 0:
        #    print "Fake",first,last, art.label
            N_fake += sent.length
        #    if first not in fake:
        #        fake[first] = 1
        #    else:
        #        fake[first] += 1
            if last not in fake:
                fake[last] = 1
            else:
                fake[last] +=1
        else:
        #    print "Real",first,last, art.label
            N_real += sent.length
        #    if first not in real:
    
        #        real[first] = 1
        #    else:
        #        real[first] += 1
            if last not in real:
                real[last] = 1
            else:
                real[last] +=1


    return real,fake,N_real,N_fake

############ Parser #################
import pickle
from bllipparser import RerankingParser

def sent_struct(trainArticles):
    rrp = RerankingParser.fetch_and_load('WSJ-PTB3',verbose=True)
    fake_score = []
    real_score = []
    gram_scores = []
    score_work = []
    count = 0
    for article in trainArticles:
        count +=1
    
        sc = 0
        lc = 0
    #    print "~~~~~~~ Article ~~~~~~~~~~~"
        for sent in article.allSentences:
        #    print sent.string
            best_list = rrp.parse(sent.string)
            score = best_list[0].parser_score
            if article.label == 0:
                fake_score.append([sent.length,score])
            else:
                real_score.append([sent.length,score])
            sc += score*sent.length
            lc += sent.length
        #    sent_score.append(sc)
        #    print sent.length,score/float(sent.length),article.label
        
    #    print "Grammaticality score of ",article.label," article : ",sc/float(lc)
        print "Article ",count
        gram_scores.append(sc/float(lc))
        score_work.append([article.label,sc/float(lc)])

    #    print "--------------------------------"
    pickle_file = open('article_gram_score.pkl','wb')
    pickle.dump(gram_scores,pickle_file)
    pickle_file.close()
    pickle_file = open('score.pkl','wb')
    pickle.dump(score_work,pickle_file)
    pickle_file.close()
    




def main():

    print "Train"
    real = {}
    fake = {}
    N_real = N_fake = 0
    trainArticles = preprocessData("trainingSet.dat","trainingSetLabels.dat")
    sent_struct(trainArticles)
    print len(trainArticles), "Number of Articles"
#    for art in trainArticles:
        #print art.allSentences
#        real,fake,N_real,N_fake = pos_feat(art,real,fake,N_real,N_fake)
    #    for sent in art.allSentences:
    #        print sent.string
    #    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Dev"
#    print "Distribution for Fake Articles : "
#    for key,value in fake.items():
#        fake[key] = math.log(fake[key]/float(N_fake))
#        print key,fake[key]
#    print "-----------------------------------"
#    print "Distribution for Real Articles : "
#    for key,value in real.items():
#        real[key] = math.log(real[key]/float(N_real))
#        print key,real[key]

#    print "---------------------------------"
#    print "Distribution for Real Articles : ", N_real
#    print "Distribution for Fake Articles : ", N_fake
    testArticles = preprocessData("developmentSet.dat", "developmentSetLabels.dat")
    print len(testArticles), "Number of Articles"

if __name__ == "__main__":
    main()