

def extractFourGram():
    fp = open('featureFour_dev.txt')
    data = fp.readlines()
    four_grams = []
    perplexity = []
    rarewords = []
    ttr = []
    for line in data:
        items = line.strip().split(' ')
        perplexity.append(float(items[0]))
        four_grams.append(float(items[1]))

    fp.close()

    fp = open('basic_dev.csv')
    fp.readline()
    data = fp.readlines()
    for line in data:
        items = line.strip().split(',')
        rarewords.append(float(items[2]))
        ttr.append(float(items[3]))

    return rarewords, ttr, perplexity, four_grams


def main():
    rarewords, ttr, perplexity, four_grams = extractFourGram()
    print 'hello'


if __name__ == '__main__':
    main()