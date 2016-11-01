import json
import pandas as pd

from business import Business
from user import User

def getBusinesses():

	ret = []
	with open("data/edinburgh_restaurants.json") as f:
		data = f.readlines()

	data = map(lambda x: x.rstrip(), data)
	data_json_str = "[" + ','.join(data) + "]"
	data_df = pd.read_json(data_json_str)
	for i in range(0, data_df.shape[0]):
		datai = data_df.iloc[i]
		b = Business()
		b.setID(datai["business_id"])
		b.setReviewCount(datai["review_count"])
		ret.append(b)

	return ret

def getUsers():

	ret = []
	with open("data/edinburgh_restaurant_users.json") as f:
		data = f.readlines()

	data = map(lambda x: x.rstrip(), data)
	data_json_str = "[" + ','.join(data) + "]"
	data_df = pd.read_json(data_json_str)
	for i in range(0, data_df.shape[0]):
		datai = data_df.iloc[i]
		u = User()
		u.setID(datai["user_id"])
		u.setReviewCount(datai["review_count"])
		ret.append(u)
	
	return ret
