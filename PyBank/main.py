import csv
import os

inputdata=os.path.join(".","rawdata","budget_data.csv")
cou=0
sum=0

with open(inputdata,"r",encoding="UTF-8") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")

    title=next(csvreader)
    print(f"{title}")

    for row in csvreader:
        if row[0]!="Date":
            cou=cou+1
            sum=sum+float(row[1])
            if cou==1 :
                low=float(row[1])
            elif cou==2:
                chg=float(row[1])-before
                incnum=chg
                decnum=chg
                incdate=row[0]
                decdate=row[0]
            else:
                if (float(row[1])-before)>incnum:
                    incnum=(float(row[1])-before)
                    incdate=row[0]
                if (float(row[1])-before)<decnum:
                    decnum=(float(row[1])-before)
                    decdate=row[0]
            before=float(row[1])

avg=round(float((before-low)/(cou-1)),2)
sum=round(sum,0)

outputfile=os.path.join("PyBankSolved.csv")

res=[]

print("\n")
res.append("\n")
print(f"Financial Analysis")
res.append("Financial Analysis")
print(f"---------------------------")
res.append("---------------------------")
print(f"Total Months: {cou}")
res.append("Total Months: "+str(cou))
print(f"Total: ${sum}")
res.append("Total: $"+str(sum))
print(f"Average Change: ${avg}")
res.append("Average Change: $"+str(avg))
print(f"Greatest Increase in Profits: {incdate} $({incnum})")
res.append("Greatest Increase in Profits: "+str(incdate)+" $("+str(incnum)+")")
print(f"Greatest Decrease in Profits: {decdate} $({decnum})")
res.append("Greatest Decrease in Profits: "+str(decdate)+" $("+str(decnum)+")")
print("\n")

with open(outputfile, "w") as datafile:
    writer=csv.writer(datafile)
    for x in res:
        writer.writerow([x])

