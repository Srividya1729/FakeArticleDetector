#!/usr/bin/env python

from Load_Data import Load_Data, Load_Test_Data
import preprocessData as pd, numpy as np, sys
from StatisticalFeatureExtractor import StatisticalFeatureExtractorFunction
from SyntacticalFeatureExtractor import SyntacticalFeatureExtractorFunction
from MedianSVD_feat import compute_tred_median
from topical_redundancy import compute_tred
from sklearn.externals import joblib
from word2vec import word2vec
from lexicalEntropy import get_lexical_entropy
from LanguageModelFeatures import get_lang_features

if __name__ == "__main__":

	test_file = sys.argv[1]

	Load_Test_Data(test_file)

	X = []

	# sentlen, ttr, stopwords, trifive_ratio, triquad_ratio, entropy, ratio1, ratio2, pos_median 

	testData = pd.preprocessDataFunction(test_file, "dummy-labels.txt")

	ttr, stopWordsRatio = StatisticalFeatureExtractorFunction(testData)
	print "Stat features done!"

	entropy, ratio1, ratio2 = get_lexical_entropy(testData)
	
	avgsentlenF, nounsRatio, verbsRatio, contentToNonPOSRatio, adjNounRatio = SyntacticalFeatureExtractorFunction(testData)
	print len(avgsentlenF), len(nounsRatio), len(verbsRatio), len(contentToNonPOSRatio), len(adjNounRatio)
	print "Syn features done!"
	
	ratioTriQuad, ratioTriFive = get_lang_features(testData)
	print "Lang Features Done!"

	SVDMedian = compute_tred_median(testData)
	print "Median features done!"
	
	# Stats,Syn, SVDMedian, LangModel Ratios, loss, stats, sparse = compute_tred(testData)
	loss,stats,sparse = compute_tred(testData)
	
	print "top_red features done!"
	
	# testData_word2vec = Load_Data(test_file,"dummy-labels.txt")

	# mean_word2vec = word2vec(testData_word2vec.return_train_data())
	# print "word2vec done!"

	# X = np.array([ttr, stopWordsRatio, avgsentlenF, nounsRatio, verbsRatio, contentToNonPOSRatio, adjNounRatio, SVDMedian, loss, stats, sparse, mean_word2vec])
	# print np.array(X)

	X.append(avgsentlenF)
	X.append(ttr)
	X.append(stopWordsRatio)
	X.append(ratioTriFive)
	X.append(ratioTriQuad)
	X.append(entropy)
	X.append(ratio1)
	X.append(ratio2)
	X.append(SVDMedian)


	# X.append(nounsRatio)
	# X.append(verbsRatio)
	# X.append(contentToNonPOSRatio)
	# X.append(adjNounRatio)
	# X.append(mean_word2vec)
	# X.append(loss)
	# # X.append(stats)
	# X.append(sparse)

	X = np.array(X)

	X = X.T[:,:]

	model = joblib.load('abc_best_final.pkl')
	y_predicted = model.predict_proba(X)
	class_threshold = 0.5

	for prediction in y_predicted:
		if prediction[0] > prediction[1]:
			label = 1
		else:
		 	label = 0
		print prediction[0], prediction[1], label



