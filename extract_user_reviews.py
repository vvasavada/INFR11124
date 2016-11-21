import json

from textblob import TextBlob

with open("data/edinburgh_user_reviews.json") as f:
	data = json.loads(f.readline())

user_average_review_length = {}
user_review_business = {}
user_reviews = {}

for user_id in data:
	count = 0
	review_length = 0
	user_reviews[user_id] = []
	for review in data[user_id]:
		user_reviews[user_id].append(review)
		user_review_business[user_id] = review["business_id"]
		b = TextBlob(review["text"])
		review_length += len(b.words)
		count += 1

	if count != 0:
		user_average_review_length[user_id] = float(review_length)/count
