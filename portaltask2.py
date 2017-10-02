import collections
import datetime
Event = collections.namedtuple('Event','description date start finish')

Interview = Event('Interveiw at the Portal',datetime.date(2017,2,23),datetime.time(hour = 15),
                  datetime.time(hour=16,minute=30))
Lunch = Event('Lunch with Cindy',datetime.date(2017,2,25),datetime.time(hour=12),
              datetime.time(hour=13))
Dinner = Event('Dinner with John',datetime.date(2017,2,24),datetime.time(hour=17),
               datetime.time(hour=17,minute=30))
Conference = Event('Conference',datetime.date(2017,2,24),datetime.time(hour=11),
                   datetime.time(hour=17,minute=30))
Game = Event('Basketball Game',datetime.date(2017,2,26),datetime.time(hour=17),
             datetime.time(hour=19))
Gym = Event('Gym',datetime.date(2017,2,26),datetime.time(hour=8),
            datetime.time(hour=9,minute=30))
Class = Event('CS Class',datetime.date(2017,2,26),datetime.time(hour=7),
              datetime.time(hour=9))
Brunch = Event('Brunch',datetime.date(2017,2,23),datetime.time(hour=14),
               datetime.time(hour=16))

eventlist = [Interview,Lunch,Dinner,Conference,Game,Gym,Class,Brunch]

def checkConflict(eventlist:list)->str:
    '''Takes list of events and prints out which ones have
        scheduling conflicts'''
    conflictlist = []
    namelist = []
    otherlist = list(eventlist)
    for event in eventlist:
        otherlist.remove(event)
        for event2 in otherlist:
            if event.date == event2.date:
                if (event.start < event2.finish and event2.start < event.finish):
                    conflictlist.append(event)
        otherlist.append(event)
    for conflict in conflictlist:
        namelist.append(conflict.description)
    return namelist
                 


print(checkConflict(eventlist))
