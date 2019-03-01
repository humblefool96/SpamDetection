import os
from collections import Counter
#from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
#making a dictionary which has words as key and value as occurences of that word
def make_dict():
    direc = "emails/"
    files = os.listdir(direc)
    emails = [direc + email for email in files]
    #print(emails)
    words = []
    c = len(emails)
    for email in emails:
        f = open(email, errors='ignore')
        blob = f.read()
        words+=blob.split(" ")
        c-=1
        print(c)

    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""

    dictionary = Counter(words)
    del dictionary[""]
    return dictionary.most_common(3000)

#preapring the dataset
def make_dataset(dictionary):
    direc = "emails/"
    files = os.listdir(direc)
    emails = [direc + email for email in files]

    feature_set = []
    labels = []
    c = len(emails)
    for email in emails:
        data = []
        f = open(email, errors='ignore')
        words = f.read().split(" ")
        print(c)
        c-=1
        for entry in dictionary:
            data.append(words.count(entry[0]))
        feature_set.append(data)
        if "ham" in email:
            labels.append(0)
        if "spam" in email:
            labels.append(1)

    return feature_set, labels


d = make_dict()
features, labels = make_dataset(d)

#print(len(features))
#print(len(labels))
x_train, x_test, y_train, y_test = tts(features,labels,test_size=0.2)

clf = MultinomialNB()
clf.fit(x_train, y_train)

preds = clf.predict(x_test)

print(accuracy_score(y_test,preds))
