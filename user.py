class User:
	def __init__(self):
		self.friends = []

	def setID(self, id):
		setattr(self, "id", id)
	
	def getID(self):
		return self.id

	def setEliteNum(self, elite_num):
		setattr(self, "elite_num", elite_num)

	def getEliteNum(self):
		return self.elite_num

	def setYelpingSince(self, yelping_since):
		setattr(self, "yelping_since", int(yelping_since.split("-")[0]))
	
	def getYelpingSince(self):
		return self.yelping_since
	
	def setFanCount(self, fan_count):
		setattr(self, "fan_count", fan_count)

	def getFanCount(self):
		return self.fan_count

	def setFriendCount(self, friend_count):
		setattr(self, "friend_count", friend_count)

	def getFriendCount(self):
		return self.friend_count

	def setReviewCount(self, review_count):
		setattr(self, "review_count", review_count)

	def getReviewCount(self):
		return self.review_count

	def setVoteCount(self, vote_count):
		setattr(self, "vote_count", vote_count)

	def getVoteCount(self):
		return self.vote_count

	def getAverageVotes(self):
		if self.getReviewCount() != 0:
			return self.getVoteCount()/self.getReviewCount()
		return 0
	
	def addFriend(self, friend):
		self.friends.append(friend)

	def isFriend(self, user_id):
		if user_id in self.friends:
			return True
		return False
