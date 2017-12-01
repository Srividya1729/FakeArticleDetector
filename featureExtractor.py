
def extractFourGram(gramscore_features, w2w_features, pos_ratio_features, word2vec_mean_features, trisix_ratio_features, trifive_ratio_features, triquad_ratio_features, pos_three_perp_features, pos_four_perp_features, entropy_features, three_grams_perp_features, five_grams_perp_features, four_grams_perp_features, stat_features, ratio1_features, ratio2_features):

    #lang model - ratio and features

    four_grams_perp = []
    four_grams = []

    five_grams_perp = []
    five_grams = []

    three_grams_perp = []
    three_grams = []


    trifive_ratio = []
    triquad_ratio = []
    trisix_ratio = []

    #V2/V1 ratio etc

    ratio1 = []
    ratio2 = []

    #lexical entropy feature

    entropy = []

    # pos lang model - ratio and features
    r1 = []
    r2 = []
    r3 = []

    pos_four_perp = []
    pos_three_perp = []

    # svd - inter word coherence features

    median = []
    maxx = []
    minn = []
    mean = []
    ratio = []

    # grammer features
    grammaticality = []
    grammar_score = []

    # statistical features

    stopwords = []
    ttr = []
    rare = []
    sentlen = []
    verb = []
    noun = []

    # word2vec - mean

    word2vec_mean = []

    # statistical features

    fp = open(stat_features)
    fp.readline()
    data = fp.readlines()
    for line in data:
        items = line.strip().split(',')

        ttr.append(float(items[2]))
        stopwords.append(float(items[3]))
        sentlen.append(float(items[4]))
        rare.append(float(items[9]))
        grammaticality.append(float(items[6]))
        verb.append(float(items[7]))
        noun.append(float(items[8]))

    #svd - inter word coherence features

    fp = open(w2w_features)
    data = fp.readlines()
    for line in data:
        items = line.strip().split(',')
        median.append(float(items[0]))
        maxx.append(float(items[1]))
        minn.append(float(items[2]))
        mean.append(float(items[3]))
        ratio.append(float(items[4]))

    fp.close()

    # grammer features

    fp = open(gramscore_features)
    data = fp.readlines()
    for line in data:
        items = line.strip().split(' ')
        grammar_score.append(float(items[0]))

    fp.close()

    #word2vec - mean

    fp = open(word2vec_mean_features)
    data = fp.readlines()
    for line in data:
        items = line.strip().split(' ')
        word2vec_mean.append(float(items[0]))

    fp.close()

    # lang model features - 3gram

    fp = open(three_grams_perp_features)
    data = fp.readlines()
    for line in data:
        items = line.strip().split(' ')
        three_grams_perp.append(float(items[0]))

    fp.close()

    # lang model features - 4gram

    fp = open(four_grams_perp_features)
    data = fp.readlines()
    for line in data:
        items = line.strip().split(',')
        four_grams_perp.append(float(items[0]))

    fp.close()

    # lang model features - 5gram

    fp = open(five_grams_perp_features)
    data = fp.readlines()
    for line in data:
        items = line.strip().split(' ')
        five_grams_perp.append(float(items[0]))

    fp.close()

    # lang model features - ratio

    fp = open(trifive_ratio_features)
    data = fp.readlines()
    for line in data:
        items = line.strip().split(' ')
        trifive_ratio.append(float(items[0]))

    fp.close()

    # lang model features - ratio

    fp = open(triquad_ratio_features)
    data = fp.readlines()
    for line in data:
        items = line.strip().split(' ')
        triquad_ratio.append(float(items[0]))

    fp.close()

    # lang model features - ratio

    fp = open(trisix_ratio_features)
    data = fp.readlines()
    for line in data:
        items = line.strip().split(' ')
        trisix_ratio.append(float(items[0]))

    fp.close()

    # V2/V1 ratio etc

    fp = open(ratio1_features)
    data = fp.readlines()
    for line in data:
        items = line.strip().split(',')
        ratio1.append(float(items[0]))

    fp.close()

    # V2/V1 ratio etc

    fp = open(ratio2_features)
    data = fp.readlines()
    for line in data:
        items = line.strip().split(',')
        ratio2.append(float(items[0]))

    fp.close()

    # lexical entropy feature

    fp = open(entropy_features)
    data = fp.readlines()
    for line in data:
        items = line.strip().split(' ')
        entropy.append(float(items[0]))

    fp.close()

    # pos lang model - 4gram

    fp = open(pos_four_perp_features)
    data = fp.readlines()
    for line in data:
        items = line.strip().split(' ')
        pos_four_perp.append(float(items[0]))

    fp.close()

    # pos lang model - 3gram

    fp = open(pos_three_perp_features)
    data = fp.readlines()
    for line in data:
        items = line.strip().split(' ')
        pos_three_perp.append(float(items[0]))

    fp.close()

    # pos lang model - ratio

    fp = open(pos_ratio_features)
    data = fp.readlines()
    for line in data:
        items = line.strip().split()
        r1.append(float(items[0]))
        r2.append(float(items[1]))
        r3.append(float(items[2]))

    fp.close()

    return four_grams_perp, five_grams_perp, three_grams_perp, trifive_ratio, triquad_ratio, trisix_ratio,
    ratio1, ratio2, entropy, r1, r2, r3, pos_four_perp, pos_three_perp, median, maxx, minn, mean, ratio, grammaticality, grammar_score,
    stopwords, ttr, rare, sentlen, verb, noun, word2vec_mean

    #ttr, stopwords, trifive_ratio, triquad_ratio, median - FEATURES THAT WORK

'''
def main():
    #three_grams_perp, four_grams_perp, five_grams_perp = extractFourGram('pos_3_train.txt','pos_4_train.txt','emp_train.txt','perp_5_train.txt','perp_4_train.txt','basic.csv')
    print ('hello')
    ttr, stopwords, three_grams_perp, four_grams_perp, five_grams_perp = extractFourGram('pos_3_train.txt','pos_4_train.txt','emp_train.txt','perp_5_train.txt','perp_4_train.txt','basic.csv')
    print ('hello')
    #ttr, stopwords, sentlen, rare, three_grams_perp, four_grams_perp, five_grams_perp, entropy, pos_three_perp, pos_four_perp

if __name__ == '__main__':
    main()
'''

