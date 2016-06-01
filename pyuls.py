#!/usr/bin/python

import csv
"""The purpose of this module is to parse each FCC
ULS database type into corresponding python types"""

def tryConvertString( input ):
	"""
	Try some different string encodings.
	Hopefully someday we can find the standard the FCC uses.
	I asked them, but I don't think they understood the question.
	"""
	for conversion in [ 'iso_8859_1', 'cp1252', 'utf-8' ]:
		try:
			return unicode(input, conversion, 'strict' )
		except UnicodeDecodeError:
			pass
	return unicode( input, 'iso_8859_1', 'ignore' )

import schema_parser
tables={}
for sheet in schema_parser.extract_tables("docs/pa_ddef42.xls"):
	tables[sheet[0]]=(sheet[1],list(sheet[2]))

def metaparser( keyList, fileLikeObject ):
	"""Map a key list onto a CSV file and do some conversions"""
	keys = tables[tableKey][1]
	for row in csv.reader(fileLikeObject, delimiter='|'):
		yield dict(zip(keys, row))

from functools import partial
exec("""def a(x):\n\tpass""")
parseA2 = partial(metaparser,"A2")
parseAD = partial(metaparser,"AD")
parseAM = partial(metaparser,"AM")
parseBC = partial(metaparser,"BC")
parseCG = partial(metaparser,"CG")
parseCO = partial(metaparser,"CO")
parseEN = partial(metaparser,"EN")
parseF5 = partial(metaparser,"F5")
parseF6 = partial(metaparser,"F6")
parseFA = partial(metaparser,"FA")
parseHD = partial(metaparser,"HD")
parseHS = partial(metaparser,"HS")
parseLA = partial(metaparser,"LA")
parseLM = partial(metaparser,"LM")
parseMI = partial(metaparser,"MI")

def parseMW(fileLikeObject):
	"""Parse MW.dat table - MICROWAVE"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"ebfNumber",
		"callSign",
		"packIndicator",
		"packRegistrationNumber",
		"packName",
		"typeOfOperation",
		"smsaCode",
		"stationClass",
		"cummulativeEffortIsMajor",
		"statusCode",
		"statusDate",
		]

	return parse( fileLikeObject, keys )

def parseP2(fileLikeObject):
	"""Parse P2.dat table - Leased Microwave Path"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"ebfNumber",
		"callSign",
		"leaseId",
		"leasedSiteLinkIdentifier",
		"actionPerformed",
		"licensedPathNumber",
		"licensedTransmitLocationNumber",
		"licensedTransmitAntennaNumber",
		"licensedReceiverLocationNumber",
		"licensedReceiverAntennaNumber",
		"masDemsSubTypeOfOperation",
		"pathTypeCode",
		"passiveReceiverIndicator",
		"countryCode",
		"interferenceToGso",
		"receiverCallSign",
		"angularSeparation",
		"certNoAlternative",
		"certNoInterference",
		"statusCode",
		"statusDate",
		]

	return parse( fileLikeObject, keys )

def parseRI(fileLikeObject):
	"""Parse RI.dat table - Revenue Information"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"ebfNumber",
		"entityType",
		"yearSequenceId",
		"grossRevenues",
		"yearEndDate",
		"averageGrossRevenues",
		"assetDisclosure",
		"statementType",
		"inExistence",
		]

	return parse( fileLikeObject, keys )

def parseRE(fileLikeObject):
	"""Parse RE.dat table - REASON"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"ebfNumber",
		"reason",
		]

	return parse( fileLikeObject, keys )

def parseSC(fileLikeObject):
	"""Parse SC.dat table - SPECIAL CONDITION"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"ebfNumber",
		"callSign",
		"specialConditionType",
		"specialConditionCode",
		"statusCode",
		"statusDate",
		]

	return parse( fileLikeObject, keys )

def parseSE(fileLikeObject):
	"""Parse SE.dat table - SHIP EXEMPTION"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"ebfNumber",
		"callSign",
		"shipCallSign",
		"portRegistry",
		"owner",
		"operator",
		"charter",
		"agent"
		"radiotelephoneExemptionRequested",
		"gmdssExemptionRequested",
		"radioDirectionExemptionRequested",
		"previousExemptionFileNumber",
		"foreignPort",
		"vesselSizeException",
		"equipmentExemption",
		"limitedRoutesExemption",
		"conditionOfVoyagesExemption",
		"otherExemption",
		"otherExemptionDescription",
		"shipType",
		"numberOfCrew",
		"numberOfPassengers",
		"numberOfOthers",
		"countOfVhf",
		"countOfVhfDsc",
		"countOfEpirb",
		"countOfSurvivalCraft",
		"countOfEarthStation",
		"countOfAutoAlarm",
		"countOfSingleSideBand",
		"singleSideBandTypeMf",
		"singleSideBandTypeHf",
		"singleSideBandTypeDsc",
		"countOfNavtex",
		"countOf9GhzRadar",
		"countOf500KhzDistress",
		"countOfReservePower",
		"countOfOther",
		"descriptionOfOther",
		]

	return parse( fileLikeObject, keys )

def parseSF(fileLikeObject):
	"""Parse SF.dat table - LICENSE FREE FORM SPECIAL CONDITION"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"ebfNumber",
		"callSign",
		"licenseFreeFormType",
		"uniqueLicenseFreeFormIdentifier",
		"sequenceNumber",
		"licenseFreeFormCondition",
		"statusCode",
		"statusDate",
		]

	return parse( fileLikeObject, keys )

def parseSH(fileLikeObject):
	"""Parse SH.dat table - SHIP"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"ebfNumber",
		"callSign",
		"typeOfAuthorization",
		"numberInFleet",
		"generalClassOfShipCode",
		"specialClassOfShipCode",
		"shipName",
		"officialNumberOfShip",
		"internationalVoyagesIndicator",
		"foreignCommunicationsIndicator",
		"radiotelegraphWorkingSeriesRequired",
		"requestForMmsi",
		"grossTonnage",
		"shipLength",
		"workingFreqS1",
		"workingFreqS2",
		"selCallNumber",
		"selCallInmarsat",
		"mmsiNumber",
		"requiredCatA",
		"requiredCatB",
		"requiredCatC",
		"requiredCatD",
		"requiredCatE",
		]

	return parse( fileLikeObject, keys )


def parseSR(fileLikeObject):
	"""Parse SR.dat table - SHIP RESCUE ADMINISTRATION"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"ebfNumber",
		"callSign",
		"epirbIdentificationCode",
		"inmarsatA",
		"inmarsatB",
		"inmarsatC",
		"inmarsatM",
		"inmarsatMini",
		"vhf",
		"mf",
		"hf",
		"dsc",
		"epirb_406_mhz",
		"epirb_121_5_mhz",
		"sart",
		"raftCount",
		"lifeboatCount",
		"vesselCapacity",
		]

	return parse( fileLikeObject, keys )

def parseSV(fileLikeObject):
	"""Parse SV.dat table - SHIP VOYAGE"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"ebfNumber",
		"callSign",
		"voyageNumber"
		"voyageDescription",
		]

	return parse( fileLikeObject, keys )

def parseTP(fileLikeObject):
	"""Parse TP.dat table - Transmission Method or Protocol"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"ebfNumber",
		"callSign",
		"locationNumber",
		"antennaNumber",
		"prototypeSequenceId",
		"protocol",
		"protocolDescription",
		"actionPerformed",
		"statusCode",
		"statusDate",
		]

	return parse( fileLikeObject, keys )

def parseVC(fileLikeObject):
	"""Parse VC.dat table - Vanity Call Sign"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"ebfNumber",
		"orderOfPrecedence",
		"requestedCallSign",
		]

	return parse( fileLikeObject, keys )
