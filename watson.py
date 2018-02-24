from __future__ import print_function
import json
import re
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, SentimentOptions, KeywordsOptions

def getSentient(data):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2017-02-27',
        username='4cf22873-ff53-4542-a966-0ce007daea71',
        password='VM2UsYDKHxVa')

    response = natural_language_understanding.analyze(
        text=data,
        features=Features(entities=EntitiesOptions(), sentiment=SentimentOptions()))

    print (json.dumps(response,indent=2))
    return (json.dumps(response, indent=2))

def getScore(info):
    info = getSentient(info)
    a=re.search(r'\b(score)\b', info)
    return float(info[a.end()+3:a.end()+10])

def findFood(score):
    if score>=-1 and score<-0.7:
        print("If you're feeling down, you should eat some ice cream")
    elif score>=-0.7 and score<-0.4:
        print("You seem tired, let's go to a coffee shop")
    elif score>=-0.4 and score<0.4:
        print("When in doubt, fast food never hurts")
    elif score>=0.4 and score<0.7:
        print("You seem pretty relaxed, how about some takeout")
    else:
        print ("You seem happy, let's celebrate with some good food")




