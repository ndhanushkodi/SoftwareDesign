# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 22:02:21 2014

@author: ndhanushkodi
"""
from pattern.web import *
from pattern.en import *
import time
import matplotlib.pyplot as plt
import numpy as np

def facebook_status1():


    f = Facebook(license='CAAEuAis8fUgBAL85hoR56jWkDVY8n2uzsxytD7dHZA5FUtFpjJ5r3QZBzrQxxW9XQ2w8JRSt6SluWN5OtT9w0cBowJAiM9EGIehhOxZBE6BlVn8pwGhRlxZA1d6fX6XBzaCwJ2lSe07z5X9w4df7Ea550ICWqdUZAL02jAX7UbSZBqR4eF3eJQ ',throttle=1)
    me = f.profile()
    my_friends = f.search(me[0], type=FRIENDS, count=3)

    statuses = []
    status_sentiments = []
    
    for i in range(len(my_friends)):
        retry = True
        while retry:
            try:
                friend_news = f.search(my_friends[i].id, type=NEWS, count=3)
                retry = False

            except:
                print "Got an Error here!"
                time.sleep(5)

        for news in friend_news:
            statuses.append(news.text)
            print statuses[i]
            print sentiment(statuses[i])
            status_sentiments.append(sentiment(statuses[i]))
    return status_sentiments
    


def facebook_search():
    
    f = Facebook(license='CAAEuAis8fUgBAHw3LItSJZCg3bSYZCSCshh3Q16ChmxeUXKchFmMw8X49c0leLVMn1dhiy99UHDffz7GmyKJah5pZBfUKojvqQ3tk1il3kWds5bFfkOPboTLCfNS8KVbNHrZCOqxHnwoD6zqZB6mnx9qIZAJPeQ7tlqOdGKPiVaaCZAyTOP6zyP',throttle=1)
    me = f.profile()
    
    news = []
    sentiment_list = []
    
    for post in f.search('britney spears', type=SEARCH, count=10):
        news.append(post.text)
#        news.append(comments.text for comments in f.search(post.id, type=COMMENTS))

    for i in range(len(news)):
        print news[i]
        print sentiment(news[i])
        print ''
        sentiment_list.append(sentiment(news[i]))
        
    return sentiment_list

        
        
        
def get_feelings(sentiment_tuple_list):
    
    feelings = [x[0] for x in sentiment_tuple_list]
    return feelings



def get_feelings_unit_test():
    
    all_sentiment = facebook_search() 
    print all_sentiment
    print ''
    feelings = get_feelings(all_sentiment)
    print feelings
    
    
     
def get_subjectivity(sentiment_tuple_list):
     
    subjectivity = [x[1] for x in sentiment_tuple_list]
    return subjectivity

    
    
def get_subjectivity_unit_test():
    
    all_sentiment = facebook_search() 
    print all_sentiment
    print ''
    subjectivity = get_subjectivity(all_sentiment)
    print subjectivity
     
  
   
def plot_histogram(which_sentiment):
    
    if which_sentiment == 'feelings':
        all_sentiment = facebook_search() 
        
        data = get_feelings(all_sentiment)
        x, y, o = plt.hist(data)
        plt.axis([-1, 1, 0, 50])
        plt.xlabel('Feelings Polarity')
        plt.ylabel('Number of Posts')
        plt.title('Histogram of Feelings on Sochi 2014')
        plt.show()
        return x

    if which_sentiment == 'subjectivity':
        all_sentiment = facebook_search()        
        data = get_subjectivity(all_sentiment)
        x1, y1, o1 = plt.hist(data)
        plt.axis([0, 1, 0, 50])
        plt.xlabel('Subjectivity')
        plt.ylabel('Number of Posts')
        plt.title('Histogram of Subjectivity on Sochi 2014')
        plt.show()
        return x1
        
    
       
    