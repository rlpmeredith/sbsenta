import csv
from datetime import datetime
import pandas as pd

# Setup dictionary with column names

cnames = []
singledict ={}
with open('columns.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        cname = row[0]
        cnames.append(cname)

# Process csv

with open('exported.csv') as csv_file2:
    csv_reader2 = csv.reader(csv_file2, delimiter=',')
    next(csv_reader2, None)
    next(csv_reader2, None)
    for row in csv_reader2:
        singledict = dict.fromkeys(cnames, None)
        singledict['Client ID'] = row[0]
        singledict['Client name'] = row[1]
        singledict['State'] = "Client"
        if row[14] == "Ltd Co.":
            singledict['Type'] = "Limited company"
        elif row[14] == "Partnership":
            singledict['Type'] = "Partnership"
        elif row[14] == "Sole Trade":
            singledict['Type'] = "Sole trader"
        elif row[14] == "Ltd Liability Partnership":
            singledict['Type'] = "LLP"
        singledict['Account manager'] = "Gavin"
        singledict['Telephone'] = row[10]
        singledict['Address Line 1'] = row[5]
        singledict['Address Line 2'] = row[6]
        singledict['District'] = row[7]
        singledict['Town / city'] = row[18]
        singledict['Postcode'] = row[9]
        if singledict['Type'] == "Limited company":
            singledict['Company no'] = row[13]
        if singledict['Type'] == "LLP":
            singledict['LLP Registered Number'] = row[13]
        if singledict['Type'] == "Sole trader":
            singledict['ST Accounting year end date'] = row[20]
        if singledict['Type'] == "Partnership":
            singledict['Partnership Accounting year end date'] = row[20]
        singledict['Bookkeeping method'] = "Online"

# Setup VAT Service

        vatdate = str(row[17])
        if len(vatdate) > 0:
            vatdate = datetime.strptime(vatdate, '%d/%m/%Y')
            print(vatdate)

            singledict['VAT service'] = "y"

            if vatdate.month == 3 or vatdate.month == 6 or vatdate.month == 9 or vatdate.month == 12:
                singledict['VAT quarter'] = "mar/jun/sep/dec"
            if vatdate.month == 4 or vatdate.month == 7 or vatdate.month == 10 or vatdate.month == 1:
                singledict['VAT quarter'] = "jan/apr/jul/oct"
            if vatdate.month == 5 or vatdate.month == 8 or vatdate.month == 11 or vatdate.month == 2:
                singledict['VAT quarter'] = "feb/may/aug/nov"

# Setup Book Keeping Service

        bookkeepingdate = str(row[15])

        print(singledict)


