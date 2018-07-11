#!/usr/bin/python
# -*- coding: UTF-8 -*-

odds = [2.42, 3.08, 3.35]

print ("odds %s, %s, %s" % (odds[0], odds[1], odds[2]) )
print ("Total spend 1000, Buy team A, B, and even, filte only when all chance over -200")

lost = 0
result_A = 0
result_B = 0
result_C = 0
result_cal_A = 0
result_cal_B = 0
result_cal_C = 0
	
for num in range(1,20):
	A_buy = num *50
	cal_A = odds[0] * A_buy - 1000
	
	for num2 in range(1,20-num):
		B_buy = num2 *50
		C_buy = (20 - num - num2) * 50
		cal_B = odds[1] * B_buy - 1000
		cal_C = odds[2] * C_buy - 1000
		cal_lost = cal_A + cal_B + cal_C
		if cal_lost > lost:
			lost = cal_A + cal_B + cal_C
			result_A = A_buy
			result_B = B_buy
			result_C = C_buy
			result_cal_A = cal_A
			result_cal_B = cal_B
			result_cal_C = cal_C
				
		if cal_A >-100 and cal_B >-100 and cal_C>-100:
			print ("%s/%s/%s, cal: %s/%s/%s" % (A_buy, B_buy, C_buy, cal_A, cal_B, cal_C)  )
			
			
print ("the best chance is %s, buy %s/%s/%s, cal: %s/%s/%s" % (lost, result_A, result_B, result_C, result_cal_A, result_cal_B, result_cal_C) )