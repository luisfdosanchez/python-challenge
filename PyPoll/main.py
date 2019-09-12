import csv
import os

inputfile=os.path.join(".","rawdata","election_data.csv")   #Set input file route

cou=0   #Set counter of votes
candidates={}   #Set dictionary for candidates and sum of votes
with open(inputfile,"r",encoding="UTF-8") as csvfile:   #Open input file
    csvreader=csv.reader(csvfile)
    for row in csvreader:   #For each row
        x=row[2]    #Store name of candidate   
        if x!="Candidate":  #If row is different from title
            cou+=1     #Sum vote
            if x in candidates.keys():  #If candidate is stored in dictionary
                couca=int(candidates[x])+1  #Add count vote of candidate (from previous count)
                candidates.update({x:couca})    #Update dictionary of candidate with new vote count
            else:      #If candidate is NOT stored in dictionary (first time it appears in datafile)
                candidates.update({x:int(1)})   #Append dictionary with candidate name and 1 vote
 
outputfile=os.path.join("PyPollSolved.csv") #Set output file route
res=[]  #Set results list for output file

#Print results and store results in list
print(f"\nVotes: {cou}")    
res.append("Votes: "+str(cou))
print(f"-------------------")
res.append("-------------------")
c=0
for x in candidates.keys(): #Results for each candidate
    pct=round(100*candidates[x]/cou,3)
    print(f"{x}: {pct}% ({candidates[x]})")
    res.append(str(x)+": "+str(pct)+"% ("+str(candidates[x])+")")
    now=candidates[x]
    if c==0:    #If first listed candidate 
        win=x   #Set as preliminary winner
        c=1
    else:   #If other candidate
        if now>before:  #If votes of current candidate are higher than previous'
            win=x   #Set current winner
    before=candidates[x]    #Save votes of current candidate for future comparison

#Continue printing results and store results in list       
print(f"-------------------")
res.append("-------------------")
print(f"Winner: {win}")
res.append("Winner: "+str(win))
print(f"-------------------\n")
res.append("-------------------")

#Export results to output file
with open(outputfile, "w") as datafile:
    writer=csv.writer(datafile)
    for x in res:
        writer.writerow([x])
