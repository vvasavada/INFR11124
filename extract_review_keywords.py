# Adopted from https://github.com/sialan/yelp-review-sentiment-analysis/blob/master/src/extract_review_keywords.py

import pandas as pd
import json
import sys
import csv_io
import sets

reload(sys)
sys.setdefaultencoding("utf-8")

from textblob import TextBlob
from collections import Counter
from rake import Rake

if __name__ == "__main__":
	results = {}
	rake = Rake("SmartStoplist.txt")

	with open("data/edinburgh_restaurant_reviews.json") as f:
		data = json.loads(f.readline())

		
	for business_id in data:
		results[business_id] = {}
		for review in data[business_id]:
			b = TextBlob(review["text"])
			keywords = rake.run(b)
			for topic in keywords:
				if topic[0] not in results[business_id]:
					results[business_id][topic[0]] = {
						'count': 0,
						'reviews': []
					}
				results[business_id][topic[0]]['reviews'].append(review['text'])
				results[business_id][topic[0]]['count'] += 1


	effective_keywords = []
	for business_id in  results:
		if len(results[business_id].keys()) != 0:
			#header = ['name', 'count']
			#temp = sets.Set()
			count = 0
			for key, value in results[business_id].iteritems():
				count += int(value['count'])
			avg_count = count/len(results[business_id].keys())
			for key, value in results[business_id].iteritems():
				if int(value['count']) > avg_count:
					effective_keywords.append(key)
			frequency_list = Counter(effective_keywords)
			#print temp
			#print effective_keywords
			#if len(temp) == 0 or len(effective_keywords) == 0:
			#	effective_keywords = effective_keywords.union(temp)
			#else:
			#	effective_keywords = effective_keywords.intersection(temp)
			#if int(value['count']) != 1:
			#	temp.append([key, value['count']])
		#if len(temp) != 0:
		#	csv_io.array_to_csv("Sentiment Analysis/" + business_id + '.csv', temp, header)

	for pair in frequency_list.most_common():
		with open("frequency_list", 'a') as f:
			f.write(pair[0] + "," + str(pair[1]) + "\n")

	#print sorted(frequency_list, key=frequency_list.get)
