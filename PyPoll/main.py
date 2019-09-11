import csv
import os

inputfile=os.path.join(".","rawdata","election_data.csv")

cou=0
candidates={}
with open(inputfile,"r",encoding="UTF-8") as csvfile:
    csvreader=csv.reader(csvfile)
    for row in csvreader:
        x=row[2]
        if x!="Candidate":
            cou+=1
            if x in candidates.keys():
                couca=int(candidates[x])+1
                #print(cou)
                #print(couca)
                candidates.update({x:couca})
                #print(x)
                #print(row)
                #print(candidates) 
                #a=1               
            else:
                candidates.update({x:int(1)})
                #print(cou)
                #print(x)
                #print(row)
                #print(candidates)
 
outputfile=os.path.join("PyPollSolved.csv")
res=[]

print(f"\nVotes: {cou}")
res.append("Notes: "+str(cou))
print(f"-------------------")
res.append("-------------------")
c=0
for x in candidates.keys():
    pct=round(100*candidates[x]/cou,3)
    print(f"{x}: {pct}% ({candidates[x]})")
    res.append(str(x)+": "+str(pct)+"% ("+str(candidates[x])+")")
    now=candidates[x]
    if c==0:
        win=x
        c=1
        before=candidates[x]
    else:
        if now>before:
            win=x
        
print(f"-------------------")
res.append("-------------------")
print(f"Winner: {win}")
res.append("Winner: "+str(win))
print(f"-------------------\n")
res.append("-------------------")

with open(outputfile, "w") as datafile:
    writer=csv.writer(datafile)
    for x in res:
        writer.writerow([x])
