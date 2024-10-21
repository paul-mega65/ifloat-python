# *******************************************************************************************
# *******************************************************************************************
#
#		Name : 		mathop.py
#		Purpose :	Mathematical Operation Base Classes
#		Date :		21st October 2024
#		Author : 	Paul Robson (paul@robsons.org.uk)
#
# *******************************************************************************************
# *******************************************************************************************

import os,sys,math,random
from ifloat import *

# *******************************************************************************************
#
#								Operation Class
#
# *******************************************************************************************

class MathOperation(object):
	def __init__(self):
		self.source = RandomSource()
	def getErrorPercent(self,a,b):
		return 0.01


# *******************************************************************************************
#
#							   Unary Operation Class
#
# *******************************************************************************************

class UnaryOperation(MathOperation):
	pass

# *******************************************************************************************
#
#							   Binary Operation Class
#
# *******************************************************************************************

class BinaryOperation(MathOperation):
	#
	#		Calculate a op b, using integer or float method.
	#
	def calculate(self,a,b):
		if a.exponent == 0 and b.exponent == 0:
			return self.calculateInteger(a,b)
		else:
			return self.calculateFloat(a,b)
	#
	#		Do one test
	#
	def test(self,forceInteger = False):

		isOk = False  																		# Get two valid values, both may be integers
		while not isOk:
			if forceInteger:
				a = RandomIInt()
				b = RandomIInt()
			else:
				a = self.source.get()
				b = self.source.get()
			isOk = self.validate(a,b)
			isOk = True

		isInteger = a.exponent == 0 and b.exponent == 0  									# Error allowed. If both values are integers error is zero.
		correct = self.getResult(a,b)		
		if IFloat(correct).exponent != 0:  													# .... except if the result is a float, in which case precision may be lost
			isInteger = False
		error = self.getErrorPercent(a,b)

		calculated = self.calculate(a,b)  													# Calculate result. This normally changes a & b
		calculated.verify()   																# Is it a legal float
		calculated.checkRange(calculated.get(),correct,0 if isInteger else error)  			# Check the answer.
