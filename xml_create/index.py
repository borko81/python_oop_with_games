# import xml.etree.ElementTree as ET
from xml.dom import minidom

import os

"""
<?xml version="1.0" encoding="utf-8" ?>
<TransferData xmlns="urn:Transfer">
 <Accountings>
<Accounting Number=" " AccountingDate="2022-09-13" ViesMonth="2022-09-01" DueDate="2022-09-13" Term="покупка" Reference=" " Vies="1" VatTerm= "2" >
  <Document Date="2022-09-13" Number="0000000020" DocumentType="3" /> 
  <Company Name="ЪНРИЪЛСОФТ - ООД" Bulstat="112042200" VatNumber="BG112042200"/>
 <AccountingDetails>
  <AccountingDetail AccountNumber="401" Amount="-4.80" Direction="Credit" />
  <AccountingDetail AccountNumber="304" Amount="-4.00" Direction="Debit" />
  <AccountingDetail AccountNumber="453/1" Amount="-0.80" Direction="Debit" />
 </AccountingDetails>
</Accounting>
</Accountings>
</TransferData>
"""

PATH = os.getcwd()
FILE = 'check.xml'
FULL_PATH = os.path.join(PATH, FILE)


data = [
	{
		'data': '2022-09-13',
		'Number': '0001',
		'Company': 'Firm One',
		'Bulstat': '12345678',
		'VatNumber': 'BG12345678',
		'info': [
			{'name': 'First name', 'salary': 100, 'age': 41},
		    {'name': 'Second name', 'salary': 50, 'age': 40},
		    {'name': 'Last name', 'salary': 100, 'age': 40},
		]
  	},
  	{
		'data': '2022-09-14',
		'Number': '0002',
		'Company': 'Firm Two',
		'Bulstat': '12345678',
		'VatNumber': 'BG12345678',
		'info': [
			{'name': 'First ', 'salary': 1, 'age': 4},
		    {'name': 'Second ', 'salary': 5, 'age': 4},
		    {'name': 'Last ', 'salary': 1, 'age': 4},
		]
  	},
]


# Root create
root = minidom.Document()
TransferData = root.createElement('TransferData')
root.appendChild(TransferData)
Accountings = root.createElement('Accountings')
TransferData.appendChild(Accountings)

def insert_into_accountings(
	AccountingDate, fak_number, firm_name, Bulstat, VatNumber,
	Number=' '
):
	Accounting = root.createElement('Accounting')
	Accounting.setAttribute('Number', Number)
	Accounting.setAttribute('AccountingDate', AccountingDate)

	Document = root.createElement('Document')
	Document.setAttribute('Date', AccountingDate)
	Document.setAttribute('Number', fak_number)
	Company = root.createElement('Company')
	Company.setAttribute('Name', firm_name)
	Company.setAttribute('Bulstat', Bulstat)
	Company.setAttribute('VatNumber', VatNumber)

	Accounting.appendChild(Document)
	Accounting.appendChild(Company)

	return Accounting


for i in data:
	Accountings.appendChild(insert_into_accountings(
		i['data'], i['Number'], i['Company'] , i['Bulstat'], i['VatNumber']
	))


xml_file = root.toprettyxml(indent='\t')
print(xml_file)
