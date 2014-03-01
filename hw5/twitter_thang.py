# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:36:06 2014

@author: ndhanushkodi
"""

from pattern.web import *
from pattern.en import *
from pattern.web    import Twitter
from pattern.en     import tag
from pattern.vector import KNN, count

def get_hashtag(hashtag):
    count = 0
    
    s = Twitter().stream(hashtag)
    for i in range(10):
        time.sleep(1)
        s.update(bytes=1024)
        if s: 
            print s[-1].text
            #print 'Sentiment' + str(sentiment(s[-1].text))
        else:
            print ''
            
def twitter_search():

    twitter = Twitter(license=(
                        "UCFYU8ZA8pPKo1Uk9hOdA",
                        "sNzOnVqAtoisWKjaiNpR5hwtOorwj5ACGfsbQefQzs",
                        ("1360983104-sjxt7h0UZCnzg6qztJGgQQQmcV1neIFjtz6zQgT",
                         "2qoQ8NqwIF8cdkGWpdZ0JcJqKMq0doLs2QX3gFQJafYfw")))
    knn = KNN()
 
    for i in range(1, 10):
        for tweet in twitter.search('#win OR #fail', start=i, count=100):
            print tweet
    print knn.classify('sweet potato burger')
    print knn.classify('stupid autocorrect')
      
def get_sentiment(hashtag):
    print 'hey'

          
def get_hashtag1(hashtag):
    count = 0
    s = Twitter().stream(hashtag)
    for i in range(10):
        time.sleep(1)
        s.update(bytes=1024)
        if count<1 and s: 
            count +=1
            print s[-1].text 
        elif count < 1:
            print ''
        else:
            break