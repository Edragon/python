#!/usr/bin/python
# -*- coding: UTF-8 -*-

odds = [2.42, 3.08, 3.35]
#A_odds = input("team A odds...\n")
#B_odds = input("team B odds...\n")
#C_odds = input("team C odds...\n") 

#for num in range (1,10):

print("if buy each 100, 300 total")
cal_A = odds[0] * 100 - 300
cal_B = odds[1] * 100 - 300
cal_C = odds[2] * 100 - 300

print("team A win: %s, team B win: %s, team C win %s" % (cal_A, cal_B, cal_C))


print("if buy one team 200, other two 100, 400 total")

cal_A = odds[0] * 200 - 400
cal_B = odds[1] * 100 - 400
cal_C = odds[2] * 100 - 400

print("team A* win: %s, team B win: %s, team C win %s" % (cal_A, cal_B, cal_C))

cal_A = odds[0] * 100 - 400
cal_B = odds[1] * 200 - 400
cal_C = odds[2] * 100 - 400

print("team A win: %s, team B* win: %s, team C win %s" % (cal_A, cal_B, cal_C))

cal_A = odds[0] * 100 - 400
cal_B = odds[1] * 100 - 400
cal_C = odds[2] * 200 - 400

print("team A win: %s, team B win: %s, team C* win %s" % (cal_A, cal_B, cal_C))