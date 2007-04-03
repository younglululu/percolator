#! /usr/bin/env python
# script that emaulates the effeects of a combined search.
# the script sorts scores based on the bigger of the scores
# from normal and testset, sorts the scores an report a 1 if
# the normal hit was highest -1 otherwhise.
#
import sys
ffeatures = open(sys.argv[1],"r")
flab = open(sys.argv[2],"r")
fweights = open(sys.argv[3],"r")
onlyTryp = (len(sys.argv)>4 and sys.argv[4]=="Y")
wl=fweights.readlines()
wei=wl[-1].split()
weights = [float(w) for w in wei]
lf=ffeatures.readlines()
ll=flab.readlines()
fweights.close()
flab.close()
ffeatures.close()
sdic = {}
tryp = {}
scores = []
labels = [int(l.split()[1]) for l in ll[1:]]
for i in range(1,len(lf)):
  label=labels[i-1]
  if label<0: ixl= -label
  else: ixl=0
  sum = 0
  wf = lf[i].split()
  theId = wf[0]
  charno = theId.find('_')
  if charno >0:
    theId=theId[charno:]
  if not theId in sdic:
    sdic[theId]=[0,0,0]
    tryp[theId]=[False,False,False]
  for j in range(len(weights)-1):
    sum += float(wf[j+1])*weights[j]
  sdic[theId][ixl]=sum
  tryp[theId][ixl]=(float(wf[12])>0) and (float(wf[13])>0)
for theId in sdic.keys():
  if (sdic[theId][0]>sdic[theId][1]):
    if tryp[theId][0] or not onlyTryp:
      scores += [(sdic[theId][0],1)]
  if (sdic[theId][2]>sdic[theId][1]):
    if tryp[theId][2] or not onlyTryp:
      scores += [(sdic[theId][2],-1)]
scores.sort(reverse=True)
labels = [label for (sc,label) in scores]
for l in labels:
  print(str(l))
