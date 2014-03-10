# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 22:02:21 2014

@author: Nitya Dhanushkodi and Casey Alvarado
"""
from pattern.web import *
from pattern.en import *
import time
import matplotlib.pyplot as plt

## SS: Great job guys! This is some beautiful code and you execute the requirements of the assignment
##     beautifully! 

## SS: Great job on the amount of comments. The style of this code is great. Doc strings are explanatory
##     of what's going on, and your variable names are self-explanatory. Great job there! I might suggest
##     using more explantory names of funcitons in the future, for example, I didn't really get that 
##     facebook_search() was looking for a specific topic. 

## SS: Maybe it'd be a good idea to have the licesnce as the input to the functions it's necessary in
##     and similarly with the topic. These should be function inputs. 


## SS: For this funciton, it might be good to add in the doc string what the values in the list of
##     tuples represent
def facebook_status1():
    
    """
    This function retreives all the sentiments of the profile's friend's posts 
    and outputs them in a list of tuples.  
    TO USE: add license below in the empty license string
    """
    f = Facebook(license='',throttle=1)
    me = f.profile()
    my_friends = f.search(me[0], type=FRIENDS, count=5)

    statuses = []
    status_sentiments = []
    
    for i in range(len(my_friends)): #loop through friends 
        retry = True
        while retry:
            try:
                friend_news = f.search(my_friends[i].id, type=NEWS, count=3) #get the friends posts
                retry = False

            except:
                print "Got an Error here!"
                time.sleep(5)

        for news in friend_news: #this loop is to put statuses and sentiments into a list
            statuses.append(news.text)
            print statuses[i]
            print sentiment(statuses[i])
            status_sentiments.append(sentiment(statuses[i]))
    return status_sentiments
    

def facebook_search():

    """
    This function searches through all public posts for a certain topic, which can be changed in the first
    for loop below. It returns a list of sentiments on the topic. 
    TO USE: add license below in the empty license string
    """
    
    f = Facebook(license='',throttle=1)
    me = f.profile()
    
    news = []
    sentiment_list = []
    
    for post in f.search('sochi', type=SEARCH, count=150): #can change thie topic searched here
        news.append(post.text)
#        news.append(comments.text for comments in f.search(post.id, type=COMMENTS))

    for i in range(len(news)): #puts the sentiments in a list
        print news[i]
        print sentiment(news[i])
        print ''
        sentiment_list.append(sentiment(news[i]))
        
    return sentiment_list

        
        
        
def get_feelings(sentiment_tuple_list):
    
    """
    This function gets the first element of each tuple in a list of sentiment tuples, which 
    is the feelings polarity for the sentiment analysis.
    """    
    feelings = [x[0] for x in sentiment_tuple_list] #gets the first element of each tuple
    return feelings



def get_feelings_unit_test():
    
    """
    This is the unit test for get_feelings. It prints out all the sentiment tuples then the first element
    of each tuple for easy comparison. 
    """      
    all_sentiment = facebook_search() 
    print 'All sentiment tuples' + all_sentiment
    print ''
    feelings = get_feelings(all_sentiment)
    print 'Feelings Values' + feelings
    
    
     
def get_subjectivity(sentiment_tuple_list):

    """
    This function gets the second element of each tuple in a list of sentiment tuples, which 
    is the subjectivity for the sentiment analysis.
    """     
    subjectivity = [x[1] for x in sentiment_tuple_list] #gets the second element of each tuple
    return subjectivity

    
    
def get_subjectivity_unit_test():

    """
    This is the unit test for get_subjectivity. It prints out all the sentiment tuples then the second element
    of each tuple for easy comparison. 
    """     
    all_sentiment = facebook_search() 
    print 'All sentiment tuples' + all_sentiment
    print ''
    subjectivity = get_subjectivity(all_sentiment)
    print 'Subjectivity Values'+ subjectivity
     
  
def plot_histogram(which_sentiment, status_or_search):

    """
    This function takes two inputs: which_sentiment, and status_or_search, which are strings
    that tell the function whether to make a histogram of feelings or subjectivity, and whether
    to do this sentiment analysis on friends posts or public posts on a certain topic. which_sentiment
    should be either 'feelings' or 'subjectivity' and status_or_search should be either 'search public' or 
    'status'. It returns the number of posts in each bin of the histogram for testing purposes. 
    You can compare the returned values in the array to make sure that the histogram is plotted right. 
    If the operation times out, just run it again. It shouldn't time out with a smaller count in 
    facebook_search, but we think it's because sometimes the internet is slow. 
    """

    if which_sentiment == 'feelings': #checks which to plot-- feelings or subjectivity
        ## SS: It might be better to use 'if' then 'elif'
        if status_or_search == 'search public': #checks whether to search public posts or friend posts
            all_sentiment = facebook_search() 
        if status_or_search == 'status': #friend posts
            all_sentiment = facebook_status1() 
        data = get_feelings(all_sentiment)
        x, y, o = plt.hist(data) 
        plt.axis([-1, 1, 0, 50]) #sets the axes
        plt.xlabel('Feelings Polarity')
        plt.ylabel('Number of Posts')
        plt.title('Histogram of Feelings')
        plt.show()
        return x #so we can look at how many posts in each bin 

    if which_sentiment == 'subjectivity':
        if status_or_search == 'search public':
            all_sentiment = facebook_search() 
        if status_or_search == 'status':
            all_sentiment = facebook_status1()       
        data = get_subjectivity(all_sentiment)
        x1, y1, o1 = plt.hist(data)
        plt.axis([0, 1, 0, 50])
        plt.xlabel('Subjectivity')
        plt.ylabel('Number of Posts')
        plt.title('Histogram of Subjectivity')
        plt.show()
        return x1
        
      
    