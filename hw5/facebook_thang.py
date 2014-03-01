# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 22:02:21 2014

@author: ndhanushkodi
"""
from pattern.web import *
from pattern.en import *

def facebook_status1():

    statuses = []

    f = Facebook(license='CAAEuAis8fUgBAL85hoR56jWkDVY8n2uzsxytD7dHZA5FUtFpjJ5r3QZBzrQxxW9XQ2w8JRSt6SluWN5OtT9w0cBowJAiM9EGIehhOxZBE6BlVn8pwGhRlxZA1d6fX6XBzaCwJ2lSe07z5X9w4df7Ea550ICWqdUZAL02jAX7UbSZBqR4eF3eJQ ',throttle=1)
    me = f.profile()
    my_friends = f.search(me[0], type=FRIENDS, count=3)

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
    return statuses
    

def facebook_search():
    
    f = Facebook(license='CAAEuAis8fUgBAHw3LItSJZCg3bSYZCSCshh3Q16ChmxeUXKchFmMw8X49c0leLVMn1dhiy99UHDffz7GmyKJah5pZBfUKojvqQ3tk1il3kWds5bFfkOPboTLCfNS8KVbNHrZCOqxHnwoD6zqZB6mnx9qIZAJPeQ7tlqOdGKPiVaaCZAyTOP6zyP',throttle=1)
    
    me = f.profile()
    news = []    
    for post in f.search('britney spears', type=SEARCH, count=100):
        news.append(post.text)
        #print [comments.text for comments in f.search(post.id, type=COMMENTS)]
           

    for i in range(len(news)):    
        print news[i]
        print sentiment(news[i])
        print ''
        
        
    