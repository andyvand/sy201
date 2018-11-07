#!/usr/bin/env python3

# class Midshipman:
#    alpha = 211234
#    company = 13
# 
# mid1 = Midshipman()
# mid2 = Midshipman()
# 
# print(mid1.alpha,mid1.company)
# print(mid2.alpha,mid2.company)
#
# ---------------------------------------------------------------------
#
# class Midshipman:
#    def __init__(self,alphaCode,companyNumber):
#       self.alpha = alphaCode
#       self.company = companyNumber
# 
# mid1 = Midshipman(211234,13)
# mid2 = Midshipman(219999,8)
# 
# print(mid1.alpha,mid1.company)
# print(mid2.alpha,mid2.company)
#
# ---------------------------------------------------------------------
#
# class Midshipman:
# 
# 	def __init__ (self,alpha,company):
# 		self.alpha = alpha
# 		self.company = company
# 
# 	def regiment(self):
# 		if self.company <= 15:
# 			reg = "First"
# 		else:
# 			reg = "Second"
# 		return reg
# 
# mid1 = Midshipman(211234,13)
# print(mid1.regiment())
# mid2 = Midshipman(219999,22)
# print(mid2.regiment())
#
# ---------------------------------------------------------------------
#
# class Midshipman:
# 
# 	def __init__ (self,alpha,company,prtScore):
# 		self.alpha = alpha
# 		self.company = company
# 		self.prtScore = prtScore
# 
# 	def prtBonus(self,additionalPoints):
# 		self.prtScore += additionalPoints
# 
# mid1 = Midshipman(211234,13,81)
# print(mid1.prtScore)
# mid1.prtBonus(7)
# print(mid1.prtScore)
#
# ---------------------------------------------------------------------
#
# class Midshipman:
# 	def __init__ (self,alpha,prtScore):
# 		self.alpha = alpha
# 		self.prtScore = prtScore
# 
# class Company:
# 	def __init__ (self):
# 		self.mids = []
# 
# 	def addMid (self,mid):
# 		self.mids.append(mid)
# 
# 	def printScores (self):
# 		for mid in self.mids:
# 			print(mid.alpha,mid.prtScore)
# 
# # New empty Company
# co13 = Company()
# 
# # Create and add mids
# mid = Midshipman(211234,81)
# co13.addMid(mid)
# mid = Midshipman(218888,93)
# co13.addMid(mid)
# mid = Midshipman(219999,88)
# co13.addMid(mid)
# 
# # Print prt scores for all mids
# co13.printScores()
