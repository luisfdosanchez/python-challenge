import csv
import os

inputdata=os.path.join(".","rawdata","budget_data.csv")     #Set input file route

cou=0   #Var that counts months
sum=0   #Var that sums total profits

with open(inputdata,"r",encoding="UTF-8") as csvfile:   #Open input file
    csvreader=csv.reader(csvfile,delimiter=",")   #Open input file

    title=next(csvreader)   #Title rows
    print(f"{title}")   #Double check title rows

    for row in csvreader:   #For each row in file
        if row[0]!="Date":  #Do not consider first row
            cou=cou+1   #Count current month
            sum=sum+float(row[1])   #Sum current profits
            if cou==1 :    #If first month
                low=float(row[1])   #Save profit value (for average)
            elif cou==2:    #If second month
                chg=float(row[1])-before    #Save profit change
                incnum=chg  #Set initial changes for lowest and highest
                decnum=chg  #Set initial changes for lowest and highest
                incdate=row[0]  #Set initial dates for lowest and highest changes
                decdate=row[0]  #Set initial dates for lowest and highest changes
            else:   #Other months
                if (float(row[1])-before)>incnum:   #If current profit change>than previous
                    incnum=(float(row[1])-before)   #Save current profit change
                    incdate=row[0]   #Save current date
                if (float(row[1])-before)<decnum:   #If current profit change<than previous
                    decnum=(float(row[1])-before)   #Save current profit change
                    decdate=row[0]  #Save current date
            before=float(row[1])    #Save current profit to compare in future periods

avg=round(float((before-low)/(cou-1)),2)    #Calculate average
sum=round(sum,0)    #Round sum

outputfile=os.path.join("PyBankSolved.csv") #Set output file

res=[]  #Set list for output file

#Print results adn store results in list
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

#Export results
with open(outputfile, "w") as datafile:
    writer=csv.writer(datafile)
    for x in res:
        writer.writerow([x])

