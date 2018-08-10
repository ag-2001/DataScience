##twitter data PROJECT
import json
##open json file to get tweet datascience
tweetFile = open("tweets.json", "r")
##convert data to use in Python
tweetData = json.load(tweetFile)
##close families
tweetFile.close()

print(tweetData[0]["text"])

for tweet in tweetData:
    testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
    testimonial.sentiment
        Sentiment(polarity=0.39166666666666666, subjectivity=0.4357142857142857)
    testimonial.sentiment.polarity
        0.39166666666666666
