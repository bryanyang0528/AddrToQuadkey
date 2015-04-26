#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest2

class Test_addrToQuadkey(unittest2.TestCase):

	def test_read_csv_rows(self):
		from addrToQuadkey.addrToQuadkey import AddrToQuadkey
		df = AddrToQuadkey().read_csv('test/addrList.csv')
		self.assertEqual(len(df), 4)

	def test_read_csv_cols(self):
		from addrToQuadkey.addrToQuadkey import AddrToQuadkey
		df = AddrToQuadkey().read_csv('test/addrList.csv')
		self.assertEqual(len(df[1]),2)

	def test_read_csv_cell(self):
		from addrToQuadkey.addrToQuadkey import AddrToQuadkey
		df = AddrToQuadkey().read_csv('test/addrList.csv')
		self.assertEqual(df[0][0], u'原燒(台中中港店)')


	def test_toQuadkey_geo_N(self):
		from addrToQuadkey.addrToQuadkey import AddrToQuadkey
		df = AddrToQuadkey().read_csv('test/addrList.csv')
		newDf = AddrToQuadkey().toQuadkey(df, col = 2, level = 15)
		self.assertEqual(newDf[0][-1], '132123211300310' )		

	def test_toQuadkey_geo_Y(self):
		from addrToQuadkey.addrToQuadkey import AddrToQuadkey
		df = AddrToQuadkey().read_csv('test/addrList.csv')
		newDf = AddrToQuadkey().toQuadkey(df, col = 2, level = 15, geo = 'Y')
		self.assertEqual(newDf[0][-1], 120.658781 )
		self.assertEqual(newDf[0][-2], 24.15702 )
		self.assertEqual(newDf[0][-3], '132123211300310' )

if __name__ == '__main__':
	unittest2.main()