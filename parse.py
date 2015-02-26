#!/usr/bin/python

class pyuls:
	"""a generator for each pipe-separated ULS dump file"""

	import csv

	def parseAM(fileLikeObject):
		"""Parse AM.dat table"""
		for row in csv.reader(fileLikeObject, delimiter='|'):
			recordType = row[0]
			uniqueSystemIdentifier = row[1]
			ulsFileNumber = row[2]
			ebfNumber = row[3]
			callSign = row[4]
			operatorClass = row[5]
			groupCode = row[6]
			regionCode = row[7]
			trusteeCallSign = row[8]
			trusteeIndicator = row[9]
			physicianCertification = row[10]
			veSignature = row[11]
			systematicCallSignChange = row[12]
			vanityCallSignChange = row[13]
			vanityRelationship = row[14]
			previousCallSign = row[15]
			previousOperatorClass = row[16]
			trusteeName = row[17]
			yield(callsign)


	def parseCO(fileLikeObject):
		"""Parse CO.dat table"""
		for row in csv.reader(fileLikeObject, delimiter='|'):
			recordType = row[0]
			uniqueSystemIdentifier = row[1]
			ulsFileNumber = row[2]
			callSign = row[3]
			commentDate = row[4]
			description = row[5]
			statusCode = row[6]
			statusDate = row[7]
			yield(callsign)

	def parseEN(fileLikeObject):
		for row in csv.reader(fileLikeObject, delimiter='|'):
			recordType = row[0]
			uniqueSystemIdentifier = row[1]
			ulsFileNumber = row[2]
			ebfNumber = row[3]
			callSign = row[4]
			entityType = row[5]
			licenseeId = row[6]
			entityName = row[7]
			firstname = unicode(row[8], '8859', "ignore")
			middleInitial = unicode( row[9], '8859', "ignore")
			lastname = unicode(row[10], '8859', "ignore")
			suffix = unicode(row[11], '8859', "ignore")
			phone = row[12]
			fax = row[13]
			email = row[14]
			address = unicode(row[15], '8859', "ignore")
			city = unicode(row[16], '8859', "ignore")#Retry without ignore
			state = row[17]
			zip = row[18]
			poBox = row[19]
			attentionLine = row[20]
			sgin = row[21]
			fccRegistrationNumber = row[22]
			applicationTypeCode = row[23]
			applicationTypeCodeOther = row[24]
			statusCode = row[25]
			statusDate = row[26]
			yield(callSign)

	def parseHD(fileLikeObject):
		"""Parse HD.dat table"""
		for row in csv.reader(fileLikeObject, delimiter='|'):
			recordType = row[0]
			uniqueSystemIdentifier = row[1]
			ulsFileNumber = row[2]
			ebfNumber = row[3]
			callSign = row[4]
			licenseStatus = row[5]
			radioServiceCode = row[6]
			grantDate = row[7]
			expiredDate = row[8]
			cancellationDate = row[9]
			eligibilityRuleNum = row[10]
			#Row[11](position12) is reserved
			alien = row[12]
			alienGovernment = row[13]
			alienCorporation = row[14]
			alienOfficer = row[15]
			alienControl = row[16]
			revoked = row[17]
			convicted = row[18]
			adjudged = row[19]
			#Row[20](position21) is reserved
			commonCarrier = row[21]
			nonCommonCarrier = row[22]
			privateComm = row[23]
			fixed = row[24]
			mobile = row[25]
			radiolocation = row[26]
			satellite = row[27]
			developmentalOrStaOrDemonstration = row[28]
			interconnectedService = row[29]
			certifierFirstName = row[30]
			certifierMI = row[31]
			certifierLastName = row[32]
			certifierSuffix = row[33]
			certifierTitle = row[34]
			female = row[35]
			blackOrAfricanAmerican = row[36]
			nativeAmerican = row[37]
			hawaiian = row[38]
			asian = row[39]
			white = row[40]
			hispanic = row[41]
			effectiveDate = row[42]
			lastActionDate = row[43]
			auctionId = row[44]
			broadcastServicesRegulatoryStatus = row[45]
			bandManager = row[46]
			broadcastServicesTypeOfRadioService = row[47]
			alienRuling = row[48]
			licenseeNameChange = row[49]
			yield(callSign)

	def parseHS(fileLikeObject):
		"""Parse HS.dat table"""
		for row in csv.reader(fileLikeObject, delimiter='|'):
			recordType = row[0]
			uniqueSystemIdentifier = row[1]
			ulsFileNumber = row[2]
			callSign = row[3]
			logDate = row[4]
			code = row[5]
			yield(callSign)

	def parseLA(fileLikeObject):
		"""Parse LA.dat table"""
		for row in csv.reader(fileLikeObject, delimiter='|'):
			recordType = row[0]
			uniqueSystemIdentifier = row[1]
			callSign = row[2]
			attachmentCode = row[3]
			attachmentDescription = row[4]
			attachmentDate = row[5]
			attachmentFileName = row[6]
			actionPerformed = row[7]
			yield(callSign)

	def parseSC(fileLikeObject):
		"""Parse SC.dat table"""
		for row in csv.reader(fileLikeObject, delimiter='|'):
			recordType = row[0]
			uniqueSystemIdentifier = row[1]
			ulsFileNumber = row[2]
			ebfNumber = row[3]
			callSign = row[4]
			specialConditionType = row[5]
			specialConditionCode = row[6]
			statusCode = row[7]
			statusDate = row[8]
			yield(callSign)

	def parseSF(fileLikeObject):
		"""Parse SF.dat table"""
		for row in csv.reader(fileLikeObject, delimiter='|'):
			recordType = row[0]
			uniqueSystemIdentifier = row[1]
			ulsFileNumber = row[2]
			ebfNumber = row[3]
			callSign = row[4]
			licenseFreeFormType = row[5]
			uniqueLicenseFreeFormIdentifier = row[6]
			sequenceNumber = row[7]
			licenseFreeFormCondition = row[8]
			statusCode = row[9]
			statusDate = row[10]
			yield(callSign)

