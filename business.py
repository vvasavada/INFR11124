class Business:
	def setID(self, id):
		setattr(self, "id", id)

	def getID(self):
		return self.id

	def setReviewCount(self, review_count):
		setattr(self, "review_count", review_count)

	def getReviewCount(self):
		return self.review_count

	def setStarRatings(self, ratings):
		setattr(self, "stars", ratings)

	def getStarRatings(self):
		return self.stars
