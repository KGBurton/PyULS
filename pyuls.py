#!/usr/bin/python

import csv
"""The purpose of this module is to parse each FCC
ULS database type into corresponding python types"""

def parseAM(fileLikeObject):
	"""Parse AM.dat table"""
	for row in csv.reader(fileLikeObject, delimiter='|'):
		retn = dict()
		retn["recordType"] = row[0]
		retn["uniqueSystemIdentifier"] = row[1]
		retn["ulsFileNumber"] = row[2]
		retn["ebfNumber"] = row[3]
		retn["callSign"] = row[4]
		retn["operatorClass"] = row[5]
		retn["groupCode"] = row[6]
		retn["regionCode"] = row[7]
		retn["trusteeCallSign"] = row[8]
		retn["trusteeIndicator"] = row[9]
		retn["physicianCertification"] = row[10]
		retn["veSignature"] = row[11]
		retn["systematicCallSignChange"] = row[12]
		retn["vanityCallSignChange"] = row[13]
		retn["vanityRelationship"] = row[14]
		retn["previousCallSign"] = row[15]
		retn["previousOperatorClass"] = row[16]
		retn["trusteeName"] = row[17]
		yield(retn)

def parseCO(fileLikeObject):
	"""Parse CO.dat table"""
	for row in csv.reader(fileLikeObject, delimiter='|'):
		retn = dict()
		retn["recordType"] = row[0]
		retn["uniqueSystemIdentifier"] = row[1]
		retn["ulsFileNumber"] = row[2]
		retn["callSign"] = row[3]
		retn["commentDate"] = row[4]
		retn["description"] = row[5]
		retn["statusCode"] = row[6]
		retn["statusDate"] = row[7]
		yield(callsign)

def parseEN(fileLikeObject):
	for row in csv.reader(fileLikeObject, delimiter='|'):
		retn = dict()
		retn["recordType"] = row[0]
		retn["uniqueSystemIdentifier"] = int(row[1])
		retn["ulsFileNumber"] = row[2]
		retn["ebfNumber"] = row[3]
		retn["callSign"] = row[4]
		retn["entityType"] = row[5]
		retn["licenseeId"] = row[6]
		retn["entityName"] = row[7]
		retn["firstName"] = unicode(row[8], '8859', "ignore")
		retn["middleInitial"] = unicode( row[9], '8859', "ignore")
		retn["lastName"] = unicode(row[10], '8859', "ignore")
		retn["suffix"] = unicode(row[11], '8859', "ignore")
		retn["phone"] = row[12]
		retn["fax"] = row[13]
		retn["email"] = row[14]
		retn["address"] = unicode(row[15], '8859', "ignore")
		retn["city"] = unicode(row[16], '8859', "ignore")#Retry without ignore
		retn["state"] = row[17]
		retn["zip"] = int(row[18])
		retn["poBox"] = row[19]
		retn["attentionLine"] = row[20]
		retn["sgin"] = row[21]
		retn["fccRegistrationNumber"] = int(row[22])
		retn["applicationTypeCode"] = row[23]
		retn["applicationTypeCodeOther"] = row[24]
		retn["statusCode"] = row[25]
		retn["statusDate"] = row[26]
		yield(retn)

def parseHD(fileLikeObject):
	"""Parse HD.dat table"""
	for row in csv.reader(fileLikeObject, delimiter='|'):
		retn = dict()
		retn["recordType"] = row[0]
		retn["uniqueSystemIdentifier"] = row[1]
		retn["ulsFileNumber"] = row[2]
		retn["ebfNumber"] = row[3]
		retn["callSign"] = row[4]
		retn["licenseStatus"] = row[5]
		retn["radioServiceCode"] = row[6]
		retn["grantDate"] = row[7]
		retn["expiredDate"] = row[8]
		retn["cancellationDate"] = row[9]
		retn["eligibilityRuleNum"] = row[10]
		#Row[11](position12) is reserved
		retn["alien"] = row[12]
		retn["alienGovernment"] = row[13]
		retn["alienCorporation"] = row[14]
		retn["alienOfficer"] = row[15]
		retn["alienControl"] = row[16]
		retn["revoked"] = row[17]
		retn["convicted"] = row[18]
		retn["adjudged"] = row[19]
		#Row[20](position21) is reserved
		retn["commonCarrier"] = row[21]
		retn["nonCommonCarrier"] = row[22]
		retn["privateComm"] = row[23]
		retn["fixed"] = row[24]
		retn["mobile"] = row[25]
		retn["radiolocation"] = row[26]
		retn["satellite"] = row[27]
		retn["developmentalOrStaOrDemonstration"] = row[28]
		retn["interconnectedService"] = row[29]
		retn["certifierFirstName"] = row[30]
		retn["certifierMI"] = row[31]
		retn["certifierLastName"] = row[32]
		retn["certifierSuffix"] = row[33]
		retn["certifierTitle"] = row[34]
		retn["female"] = row[35]
		retn["blackOrAfricanAmerican"] = row[36]
		retn["nativeAmerican"] = row[37]
		retn["hawaiian"] = row[38]
		retn["asian"] = row[39]
		retn["white"] = row[40]
		retn["hispanic"] = row[41]
		retn["effectiveDate"] = row[42]
		retn["lastActionDate"] = row[43]
		retn["auctionId"] = row[44]
		retn["broadcastServicesRegulatoryStatus"] = row[45]
		retn["bandManager"] = row[46]
		retn["broadcastServicesTypeOfRadioService"] = row[47]
		retn["alienRuling"] = row[48]
		retn["licenseeNameChange"] = row[49]
		yield(retn)

def parseHS(fileLikeObject):
	"""Parse HS.dat table"""
	for row in csv.reader(fileLikeObject, delimiter='|'):
		retn = dict()
		retn["recordType"] = row[0]
		retn["uniqueSystemIdentifier"] = row[1]
		retn["ulsFileNumber"] = row[2]
		retn["callSign"] = row[3]
		retn["logDate"] = row[4]
		retn["code"] = row[5]
		yield(retn)

def parseLA(fileLikeObject):
	"""Parse LA.dat table"""
	for row in csv.reader(fileLikeObject, delimiter='|'):
		retn = dict()
		retn["recordType"] = row[0]
		retn["uniqueSystemIdentifier"] = row[1]
		retn["callSign"] = row[2]
		retn["attachmentCode"] = row[3]
		retn["attachmentDescription"] = row[4]
		retn["attachmentDate"] = row[5]
		retn["attachmentFileName"] = row[6]
		retn["actionPerformed"] = row[7]
		yield(retn)

def parseSC(fileLikeObject):
	"""Parse SC.dat table"""
	for row in csv.reader(fileLikeObject, delimiter='|'):
		retn = dict()
		retn["recordType"] = row[0]
		retn["uniqueSystemIdentifier"] = row[1]
		retn["ulsFileNumber"] = row[2]
		retn["ebfNumber"] = row[3]
		retn["callSign"] = row[4]
		retn["specialConditionType"] = row[5]
		retn["specialConditionCode"] = row[6]
		retn["statusCode"] = row[7]
		retn["statusDate"] = row[8]
		yield(retn)

def parseSF(fileLikeObject):
	"""Parse SF.dat table"""
	for row in csv.reader(fileLikeObject, delimiter='|'):
		retn = dict()
		retn["recordType"] = row[0]
		retn["uniqueSystemIdentifier"] = row[1]
		retn["ulsFileNumber"] = row[2]
		retn["ebfNumber"] = row[3]
		retn["callSign"] = row[4]
		retn["licenseFreeFormType"] = row[5]
		retn["uniqueLicenseFreeFormIdentifier"] = row[6]
		retn["sequenceNumber"] = row[7]
		retn["licenseFreeFormCondition"] = row[8]
		retn["statusCode"] = row[9]
		retn["statusDate"] = row[10]
		yield(retn)

