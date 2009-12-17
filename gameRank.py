#!/usr/bin/env python
# encoding: utf-8
"""
gameRank.py

Created by peter on 2009-12-17.
peter@byread.com
http://maweis.com
Copyright (c) 2009 __http://www.byread.com__. All rights reserved.
"""

import operator
import MySQLdb
from operator import itemgetter
import time
import logging

class GameRank:
	
	#
	#typeId  game type
	#dateStr 'YYMMDD'
	#
	def __init__(self,typeId,dateStr):
		
		HOST = 'HOSTADDRESS'
		USER = 'USER'
		PASSWORD = 'PASSWORD'
		DB = 'DBNAME'
		start = time.clock()
		self.db = MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,db=DB)
		end = time.clock()
		print "connect to database Time elapsed = ", end - start, " seconds "
				
		self.moneyResults = {}
		c = self.db.cursor()
		start = time.clock()
		c.execute("""select byId,sum(byreadbb) as money from bill_"""+dateStr+""" where typeId = %s  group by byid """, typeId)
		end = time.clock()
		print "get data from mysql Time elapsed = ", end - start, " seconds "
		rows = c.fetchall()
		
		start = time.clock()
		for r in rows:
			self.moneyResults[str(r[0])] = long(r[1])			
			self.moneyLists = sorted(self.moneyResults.items(),key=lambda(k,v):(v,k),reverse=True)
		end = time.clock()
		print "in python Time elapsed = ", end - start, " seconds "
		
	def 
	
	
	#
	#
	def getTopRank(self,size):
		i = 0
		start = time.clock()
		for m in self.moneyLists:
			i = i + 1
			if i > size:
				return
			print str(m[0]) + " - " + str(m[1])
			end = time.clock()
			print "get Top Rank List Time elapsed = ", end - start, " seconds "
		
		
	#
	#
	#
	def getRankById(self,byid):
		try:
			print [y[0] for y in b].index(byid)
		except ValueError, e:
			print e
		
			
if __name__ == "__main__":

	# 1 = gamble game
	# '090514' bill archive table name
	g = GameRank(1,'090514')
	g.getTopRank(10)
	# g.getRankById('21284841')
