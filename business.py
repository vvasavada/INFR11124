class Business:
	def setID(self, id):
		setattr(self, "id", id)

	def getID(self):
		if hasattr(self, "id"):
			return self.id
		raise Exception("Business ID doesn't exist")

	def setReviewCount(self, review_count):
		setattr(self, "review_count", review_count)

	def getReviewCount(self):
		if hasattr(self, "review_count"):
			return self.review_count

		raise Exception("Business Review Count doesn't exist")
