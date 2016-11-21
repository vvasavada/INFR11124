import json
import pandas as pd
import os

if __name__ == "__main__":
#	user_reviews = {}
	user_ids = []
	with open("data/edinburgh_restaurant_reviews.json") as f:
		data = json.loads(f.readline())

	for business_id in data:
		for review in data[business_id]:
#			user_id = review["user_id"]
#			if user_id in user_reviews.keys():
#				user_reviews[user_id].append(review)
#			else:
#				user_reviews[user_id] = [review]

#	with open("data/edinburgh_user_reviews.json", "w") as f:
#		json.dump(user_reviews,  f)
			user_ids.append(review["user_id"])

	with open("data/yelp_academic_dataset_user.json") as f:
		for line in f:
			data = json.loads(line)
			if data["user_id"] in user_ids:
				user = {}
				user["user_id"] = data["user_id"]
				user["review_count"] = data["review_count"]
				user["average_stars"] = data["average_stars"]
				user["votes"] = data["votes"]
				user["friends"] = data["friends"]
				user["elite"] = data["elite"]
				user["yelping_since"] = data["yelping_since"]
				user["compliments"] = data["compliments"]
				user["fans"] = data["fans"]
				with open("data/edinburgh_restaurant_users.json", 'a') as f:
					if os.path.getsize("data/edinburgh_restaurant_users.json") > 0:
						f.write("\n" + json.dumps(user))
					else:
						f.write(json.dumps(user))
