import quadkey 
from geocodequery import GeocodeQuery


class AddrToQuadkey:

	def __init__(self, input):
		self.input = input

	def read_csv(self, input, sep = ','):
		self.input = []
		with open(input) as f:
			lines = f.readlines()
			for line in lines:
				


	def toQuadkey(self, export, sep = ',', level = 15):
		toFile = open(export,'w')

		with open(self.input) as f:
			lines = f.readlines()
			for line in lines:
				name = line.split(sep)[0]
				addr = line.split(sep)[1]

				gq = GeocodeQuery("zh-tw", "tw")
				gq.get_geocode(addr)
				lat = gq.get_lat()
				lng = gq.get_lng()
				qk = quadkey.from_geo((lat, lng), level)
				toFile.write(name + "," + addr + "," + str(lat) + "," + str(lng) + "," + str(qk) + "\n")
		toFile.close()



