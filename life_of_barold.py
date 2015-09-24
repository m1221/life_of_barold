from engine import *
import engine
# why does this line work, but
# import engine
# does not work?
# import engine is if i want to use the methods
# from engine import * is if I want to create objects


"""TESTING"""
'''
barry = Barry(200,200)
barry.checkBarryCount()
barry.displayHappyness()
barry.displayCash()
barry.changeMeter('cash', 200)
barry.changeMeter('happy', 100)
print barry.cash
daysList = createEventsList(dayEvents)
nightsList = createEventsList(nightEvents)
print daysList, 'day events'
print nightsList, 'night events'''
"""END TESTING"""

"""GAME EXECUTION CODE"""
barry = Barry(200,200)
engine.playDayAndNight(engine.createEventsList(engine.dayEvents),barry)
# add loading feature / text loading
# 
# 
# 
# 