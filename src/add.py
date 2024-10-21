# *******************************************************************************************
# *******************************************************************************************
#
#		Name : 		add.py
#		Purpose :	Addition (and subtraction)
#		Date :		21st October 2024
#		Author : 	Paul Robson (paul@robsons.org.uk)
#
# *******************************************************************************************
# *******************************************************************************************

import os,sys,math,random
from ifloat import *
from mathop import *

# *******************************************************************************************
#
#								Addition Class
#
#	  Subtraction is just addition with the second value having a negated first paremeter
#
# *******************************************************************************************

class AddOperation(BinaryOperation):
	def calculateInteger(self,a,b):
		return self.addCalculator(a,b)
	def calculateFloat(self,a,b):
		return self.addCalculator(a,b)
	#
	#		Refolded together because we have two operations dependent on whether the signs match or not.
	#
	def addCalculator(self,a,b):
		if a.isNegative == b.isNegative:  													# Are the signs the same (it's an ADD)
			newSign = a.isNegative  		 												# Sign of result is the same												
			result = self.addMantissa(a,b)   												# Add mantissae as absolute values
			result.isNegative = newSign  													# give it the new sign.
		else:
			flipSign = a.isNegative  														# Calculate a + -b ; if -a + b negate result
			result = self.subtractMantissa(a,b)  											# Calculate |a| - |b|
			if flipSign:  																	# if it was -a + b then negate answer
				result.isNegative = not result.isNegative 
		return result 
	#
	#		Add 2 mantissa as absolute values
	#
	def addMantissa(self,a,b):
		if a.exponent == 0 and b.exponent == 0:
			return self.addIntegerMantissa(a,b)
		else:
			assert False
	#
	#		Subtract mantissa (e.g. a-b) as absolute values
	#
	def subtractMantissa(self,a,b):
		if a.exponent == 0 and b.exponent == 0:
			return self.subtractIntegerMantissa(a,b)
		else:
			assert False
	#
	#		Add 2 mantissa as absolute values (integer version)
	#
	def addIntegerMantissa(self,a,b):		
		a.mantissa = a.mantissa + b.mantissa  												# Add the mantissa
		a.exponent = 0
		a.isNegative = False
		if (a.mantissa & 0x80000000) != 0:													# Overflow result ?
			a.mantissa = a.mantissa >> 1  													# Shift right and bump exponent
			a.exponent = 1 																	# Can't fit in integer so make it a float
		return a 
	#
	#		Subtract mantissa (e.g. a-b) as absolute values (integer version)
	#
	def subtractIntegerMantissa(self,a,b):	
		a.mantissa = (a.mantissa + b.twosComplement(b.mantissa)) & 0xFFFFFFFF				# calculate the result
		a.exponent = 0
		a.isNegative = False
		if a.mantissa & 0x80000000 != 0:  													# If result -ve (would test sign bit in 2's complement
			a.mantissa = a.twosComplement(a.mantissa)
			a.isNegative = True
		return a

	def getResult(self,a,b):
		return a.get()+b.get()

	def validate(self,a,b):
		result = a.get()+b.get()
		return result >= IFloat.MINVALUE and result < IFloat.MAXVALUE

if __name__ == "__main__":
	random.seed(42)
	to = AddOperation()
	for i in range(0,100):
		to.test(True)
