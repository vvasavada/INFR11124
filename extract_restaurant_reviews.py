# Adopted from https://github.com/sialan/yelp-review-sentiment-analysis/blob/master/src/extract_review_keywords.py

import pandas as pd
import json
import sys
import csv_io
import sets

import parser

reload(sys)
sys.setdefaultencoding("utf-8")

from textblob import TextBlob
from collections import Counter
from rake import Rake

results = {}

rake = Rake("SmartStoplist.txt")

users = parser.getUsers()

with open("data/edinburgh_restaurant_reviews.json") as f:
	data = json.loads(f.readline())

pos_polarity = 0
neg_polarity = 0
for business_id in data:
	results[business_id] = {}
	for review in data[business_id]:
		b = TextBlob(review["text"])
		if b.sentiment.polarity >= 0:
			pos_polarity += b.sentiment.polarity
		else:
			neg_polarity += b.sentiment.polarity
		keywords = rake.run(b)
		for topic in keywords:
			if topic[0] not in results[business_id]:
				results[business_id][topic[0]] = {
					'count': 0
				}
			results[business_id][topic[0]]['count'] += 1

avg_pos_polarity = float(pos_polarity)/len(data.keys())
avg_neg_polarity = float(neg_polarity)/len(data.keys())

effective_keywords = []
for business_id in  results:
	if len(results[business_id].keys()) != 0:
		count = 0
		for key, value in results[business_id].iteritems():
			count += int(value['count'])
		avg_count = count/len(results[business_id].keys())
		for key, value in results[business_id].iteritems():
			if int(value['count']) > avg_count:
				effective_keywords.append(key)

frequency_list = Counter(effective_keywords)
frequency_list = sorted(frequency_list, key=frequency_list.get, reverse=True)
frequency_list = frequency_list[:len(frequency_list)/2]

frequency_votes = {}
subjectivity_votes = {}
subjectivity_review_length = {}
subjectivity_pos_polarity = {}
subjectivity_neg_polarity = {}

elite_frequency_votes = {}

for business_id in data:
	for review in data[business_id]:
		elite_for = 0
                for user in users:
			if review["user_id"] == user.getID():
                        	elite_for = user.getEliteNum()
                                break

		b = TextBlob(review['text'])
		keywords = rake.run(b)
		count = 0
                for topic in keywords:
			if topic[0] in frequency_list:
				count += 1
		percent = float(count*100)/len(keywords)
		
		if percent in frequency_votes.keys():
			frequency_votes[percent] = (frequency_votes[percent] + sum(map(int, review['votes'].values())))/2
			if elite_for > 0:
				elite_frequency_votes[percent] = (frequency_votes[percent] + sum(map(int, review['votes'].values())))/2
		else:
			frequency_votes[percent] = sum(map(int, review['votes'].values()))
			if elite_for > 0:
				elite_frequency_votes[percent] = sum(map(int, review['votes'].values()))

		if b.sentiment.subjectivity in subjectivity_votes.keys():
			subjectivity_votes[b.sentiment.subjectivity] = (subjectivity_votes[b.sentiment.subjectivity] + sum(map(int, review['votes'].values())))/2
		else:
			subjectivity_votes[b.sentiment.subjectivity] = sum(map(int, review['votes'].values()))

		if b.sentiment.subjectivity in subjectivity_review_length.keys():
			subjectivity_review_length[b.sentiment.subjectivity] = (subjectivity_review_length[b.sentiment.subjectivity] + len(b.words))/2
		else:
			subjectivity_review_length[b.sentiment.subjectivity] = len(b.words)
		
		if b.sentiment.polarity >= 0:
			if b.sentiment.subjectivity in subjectivity_pos_polarity.keys():
				subjectivity_pos_polarity[b.sentiment.subjectivity] = (subjectivity_pos_polarity[b.sentiment.subjectivity] + b.sentiment.polarity)/2
			else:
				subjectivity_pos_polarity[b.sentiment.subjectivity] = b.sentiment.polarity
		else:
			if b.sentiment.subjectivity in subjectivity_neg_polarity.keys():
				subjectivity_neg_polarity[b.sentiment.subjectivity] = (subjectivity_neg_polarity[b.sentiment.subjectivity] + b.sentiment.polarity)/2
			else:
				subjectivity_neg_polarity[b.sentiment.subjectivity] = b.sentiment.polarity

#print frequency_votes

#frequency_votes = {}
#for pair in frequency_list.most_common():
#	with open("frequency_list", 'a') as f:
#		f.write(pair[0] + "," + str(pair[1]) + "\n")
#		frequency_votes[pair[1]] = keyword_votes[pair[0]]
#print sorted(frequency_list, key=frequency_list.get)
