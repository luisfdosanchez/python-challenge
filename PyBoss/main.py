import csv
import os

inputdata=os.path.join(".","rawdata","employee_data.csv")

EmpID=["Emp ID"]
FirstName=["First Name"]
LastName=["Last Name"]
DOB=["DOB"]
SSN=["SSN"]
State=["State"]

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open(inputdata, "r", encoding="UTF-8") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    title=next(csvreader)

    cou=0

    for row in csvreader:
        if cou!=0:
            EmpID.append(row[0])
            FirstName.append(row[1].split(" ")[0])
            LastName.append(row[1].split(" ")[1])
            DOB.append(str(row[2].split("-")[1])+"/"+str(row[2].split("-")[2])+"/"+str(row[2].split("-",)[0]))
            SSN.append("***-**-"+str(row[3].split("-")[2]))
            State.append(us_state_abbrev[row[4]])
        cou=cou+1

outputfile=zip(EmpID,FirstName,LastName,DOB,SSN,State)
results="PyBossSolved.csv"

with open(results, "w") as datafile:
    writer=csv.writer(datafile)
    writer.writerows(outputfile)
