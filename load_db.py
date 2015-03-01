#!/usr/bin/python
import pyuls
import sqlite3

conn = sqlite3.connect('uls.db')
conn.isolation_level = None

c = conn.cursor()
c.execute("begin")

c.execute('''CREATE TABLE IF NOT EXISTS en
	(
	recordType CHAR(2),
	uniqueSystemIdentifier INT,
	ulsFileNumber TEXT,
	ebfNumber TEXT,
	callSign TEXT,
	entityType CHAR,
	licenseeId TEXT,
	firstName TEXT,
	middleInitial TEXT,
	lastName TEXT,
	suffix TEXT,
	phone TEXT,
	fax TEXT,
	email TEXT,
	address TEXT,
	city TEXT,
	state TEXT,
	zip INT,
	poBox TEXT,
	attentionLine TEXT,
	sgin TEXT,
	fccRegistrationNumber INT,
	applicationTypeCode CHAR(1),
	applicationTypeCodeOther TEXT,
	statusCode TEXT,
	statusDate TEXT
	)''')

c.executemany('''INSERT INTO en VALUES
	(
	:recordType,
	:uniqueSystemIdentifier,
	:ulsFileNumber,
	:ebfNumber,
	:callSign,
	:entityType,
	:licenseeId,
	:firstName,
	:middleInitial,
	:lastName,
	:suffix,
	:phone,
	:fax,
	:email,
	:address,
	:city,
	:state,
	:zip,
	:poBox,
	:attentionLine,
	:sgin,
	:fccRegistrationNumber,
	:applicationTypeCode,
	:applicationTypeCodeOther,
	:statusCode,
	:statusDate
	)''', pyuls.parseEN( open( "EN.dat", 'rb' ) ) )

c.execute("commit")
