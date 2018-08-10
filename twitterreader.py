import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#get json tweet data from tweets.json - convert it so python can use it
tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

#Textblob sample (you won't need this in your final file):
tb = TextBlob("You are very pretty")
print(tb.polarity)

#Create a list to hold polarity values for each tweet
polarity = []
subjectivity = []
#Get sentiment data: add polarities into list
for tweet in tweetData:
    polarity.append(tb.polarity)
    subjectivity.append(tb.subjectivity)

for i in range(1):
    polavg = sum(polarity) / len(polarity)
    subavg = sum(subjectivity) / len(subjectivity)
    print("Average polarity: " + str(polavg))
    print("Average subjectivity: " + str(subavAg))

plt.hist([polarity, subjectivity], color=['orange'. 'green'])
plt.xlabel("Polarity/subjectivity")
plt.ylabel("Frequency")
plt.show()

combinedString = ""
for tweet in tweetData:
    combinedString += tweet["text"]

combinedString = TextBlob(combinedString)
filteredWords = {}
deletewords
x = ["polavg", "subavg"]
num_bins = 3
n, bins, patches = plt.hist(x, num_bins, facecolor='red', alpha=0.5)
plt.show()
