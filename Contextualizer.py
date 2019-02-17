import nltk
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords
import os

#stopWords = ['I','am','a','an','is','the','appreciate','need','to','want','my','be','love','like','How','do','go','what','when','why','whose','whom','please','system']
stopWords = set(stopwords.words('english'))
nounList = []
verbList = []
context = ''
sentence = input("Enter Query String : ")
tagged = nltk.pos_tag(word_tokenize(sentence))

#tagged2 = nltk.pos_tag(sentence.split())
#The statement does the same as word_tokenize()
for item in tagged :
    if (item[1]=='NN' or item[1]=='NNS' or item[1]=='NNP' or item[1]=='NNPS'):
        nounList.append(item[0])
    elif (item[1]=='VB' or item[1]=='VBD' or item[1]=='VBG' or item[1]=='VBN' or item[1]=='VBZ'):
        verbList.append(item[0])

##print (tagged)
##print ('-----------------------')
##print (verbList)
##print (nounList)


for item in nounList :
    for item1 in stopWords :
        if (item.lower()==item1.lower()):
            nounList.remove(item)
for item in verbList :
    for item1 in stopWords :
        if (item.lower()==item1.lower()):
            verbList.remove(item)

##print ('-----------------------')
##print (verbList)
##print (nounList)

if(len(nounList)==0):
    for item in verbList:
        context=context+' '+item
elif (len(verbList)==0):
    for item in nounList:
        context=context+' '+item
else:
    for item in verbList:
        context=context+' '+item
    for item in nounList:
        context=context+' '+item
##print ('-----------------------')
print ("Context of Statement : ", context)

