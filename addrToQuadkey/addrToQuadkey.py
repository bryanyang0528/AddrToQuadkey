#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import quadkey 
from geocodequery import GeocodeQuery


class AddrToQuadkey:

	def __init__(self):
		#self.input = input
		pass

	def read_csv(self, input, sep = ','):
		df = []
		
		with open(input) as f:
			lines = f.readlines()	
			
			for line in lines:
				row = []
				items = line.split(sep)

				for item in items:
					row.append(item.decode('utf-8'))

				df.append(row)

		return df

	def toQuadkey(self, df, col=2, level=15, geo = 'N'):
		newDf = []

		for row in df:
			newRow = row
			gq = GeocodeQuery("zh-tw", "tw")
			gq.get_geocode(row[col-1].encode('utf-8'))
			lat = gq.get_lat()
			lng = gq.get_lng()
			qk = quadkey.from_geo((lat, lng), level)
			newRow.append(qk.key)
			if (geo == 'Y'):
				newRow.extend([lat, lng]) 

			newDf.append(newRow)

		return newDf


	def toQuadkey_(self, input, export, sep = ',', level = 15):
		toFile = open(export,'w')

		with open(input) as f:
			lines = f.readlines()

			for line in lines:
				name = line.split(sep)[0].strip()
				addr = line.split(sep)[1].strip()
				gq = GeocodeQuery("zh-tw", "tw")
				gq.get_geocode(addr)
				lat = gq.get_lat()
				lng = gq.get_lng()
				qk = quadkey.from_geo((lat, lng), level)
				toFile.write(name + "," + addr + "," + str(lat) + "," + str(lng) + "," + str(qk.key) + '\n')
		toFile.close()

if __name__ == '__main__':
	if (len(sys.argv) != 3):
		print 'usage: addrToQuadkey.py [sourceFile] [targetFile]'
		sys.exit(1)
	aq = AddrToQuadkey()
	aq.toQuadkey_(sys.argv[1], sys.argv[2])

