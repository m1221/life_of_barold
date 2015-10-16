import random
import math
import loading

class Barry:
  'Total Badass'
  name = "Barry"
  BarryCount = 0
  
  def __init__(self, happyness, cash):
    self.happyness = happyness
    self.cash = cash
  
  def displayHappyness(self):
    loading.load_string("Happyness level : " + str(self.happyness), 70)
    
  def displayCash(self):
    loading.load_string("Cash : " + str(self.cash), 70)
    
  def changeMeter(self, meter, value):
    if meter == 'cash':
      self.cash = self.cash + value
      loading.load_string("Cash gained/lost: " + str(value), 70)
      self.displayCash()
    elif meter == 'happy':
      self.happyness = self.happyness + value
      loading.load_string("Happiness gained/lost: " + str(value), 70)
      self.displayHappyness()
    else:
      print "Invalid input. Cash or Happy"
      
def continueGame():
  print "Continue to tomorrow? Y or N"
  valid_input = False
  while valid_input == False:
    user_input = raw_input()
    if user_input == "Y":
      valid_input = True
    elif user_input == "N":
      print "Goodbye!"
      exit()
    else:
      print "Please enter Y or N"
  

def createEventsList(eventsDict):
  events = []

  i = 0
  while i < 7:
    x = random.randint(1, len(eventsDict))
    probType = random.randint(1,4)
    
    if eventsDict[str(x)]['selected'] == False:
      eventsDict[str(x)]['selected'] = True
      i += 1
      probDiff = eventsDict[str(x)]['difficulty']
      prob, answer = createQAs(probType, probDiff)  
      events.append([str(x), [prob, answer]])
    else:
      pass
  
  return events
  
def createQAs(type, diff):

  if type == 1: #multiplication
    prob, answer = createMulti(diff)
  elif type == 2: # division
    prob, answer = createDiv(diff)
  elif type == 3: # factorial
    prob, answer = createFactorial(diff)
  else: # powers
    prob, answer = createPowers(diff)
  return prob, answer

def createMulti(diff):
  num1 = diff * random.randint(9,12)
  num2 = diff * random.randint(5,8)
  
  return str(num1) + " * " + str(num2) + " = ?", num1*num2
  
def createDiv(diff):
  # print "Remember to round down."
  num1 = diff * random.randint(23, 127)
  num2 = random.randint(3, 10)
  
  return str(num1) + " / " + str(num2) + " = ?", num1/num2
  
def createFactorial(diff):
  if diff == 1:
    num1 = random.randint(4, 5)
  elif diff == 2:
    num1 = random.randint(5, 6)
  elif diff == 3:
    num1 = random.randint(6, 7)
  else:
    num1 = random.randint(8, 9)
  
  return str(num1) + "!" + " = ?", math.factorial(num1)
  
def createPowers(diff):
  num1 = random.randint(3, 7)
  num2 = diff * random.randint(2, 3)
  
  return str(num1) + "^" + str(num2) + " = ?", math.pow(num1, num2) 

  
def playDayAndNight(daysEventsList, barry):
  loading.load_string("Welcome to the Life of Barold!", 25)
  loading.load_string("You have happiness, you have cash. Make more cash and get more happy by solving problems at work!",40)
  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  for i in range(0,7):
    print "----" + days[i] +"----"
    playDay(barry, daysEventsList[i])
    continueGame()
  print "End game stats: "
  barry.displayHappyness()
  barry.displayCash()
    
def playDay(barry, dayEventValues): # day is an integer value ranging from 0 to 6
  loading.load_string("The start of a new day! You roll out of bed, stretching and yawning, preparing yourself to take on the day, whatever it entails. You are on-call this week, so you should be kept busy.", 200)
  loading.load_string("You sit at your desk and wait for the work to come...", 50)
  loading.loading(1, 3)
  loading.load_string("Event!!\n" + dayEvents[dayEventValues[0]]['name'])
  loading.load_string(dayEvents[dayEventValues[0]]['descrip'], 80)
  loading.load_string("SOLVE THIS PROBLEM: (NO CALCULATORS, USE MENTAL MATH! :-)  )", 20)
  loading.loading(1, 6)
  loading.load_string( dayEventValues[1][0]) # prints math q
  
  answerIsInt = False
  while answerIsInt == False:
    answer = raw_input()
    try:
      answer = int(answer)
      answerIsInt= True
    except:
      print "Please enter an integer"
  
  if int(answer) == dayEventValues[1][1]:
    loading.playSound('woohoo')
    loading.load_string("CORRECT!")
    happyChange = dayEvents[dayEventValues[0]]['passEffect'][1]
    cashChange = dayEvents[dayEventValues[0]]['passEffect'][0]
    barry.changeMeter('cash', cashChange)
    barry.changeMeter('happy', happyChange)
  else:
    loading.playSound('doh')
    loading.load_string("WRONGO!")
    happyChange = dayEvents[dayEventValues[0]]['failEffect'][1]
    cashChange = dayEvents[dayEventValues[0]]['failEffect'][0]
    barry.changeMeter('cash', cashChange)
    barry.changeMeter('happy', happyChange)
"""DICTIONARIE(S)"""
dayEvents = {
  '1': {
    'name': 'Emergency meeting! - SERVER UPGRADE GONE ROGUE',
    'descrip': 'Your bosses call you and your coworkers for an emergency meeting. Boss B accidentally authorized a server upgrade that hadn\'t been cleared for implementation and now the upgrade is causing havoc on your client\'s servers.\nAfter Boss B passes the blame to the lack of communication skills of an employee on the technical team, they ask you, the "chosen one" to help fix this fiasco.' ,
    'difficulty': 4, # 1-3
    'passEffect': [300, 25],
    'failEffect': [150, -75],
    'selected': False
  },
  '2': {
    'name': 'Emergency situation! - DATA LOSS',
    'descrip': 'One of your coworkers went out of town while he was on call and didn\'t bring his beeper with him. So when there was a hard drive failure in the RAID 5 array he was supposed to be watching, he was unaware of it and therefore could not take the appropriate course of action nor could he contact someone to take the appropriate course of action. Soon thereafter, another disk failed, resulting in permanent data loss. Explain to your bosses that the data is lost forever.' ,
    'difficulty': 3, # 1-3
    'passEffect': [150, 0],
    'failEffect': [150, -75],
    'selected': False
  },
  '3': {
    'name': 'Routine Work - OVERSEAS COWORKERS',
    'descrip': 'Some of your coworkers live and work abroad in countries whose populaces struggle heavily with the basics of the English language. Every now and then you have to coordinate with them to complete projects. After having worked with these coworkers a few times now, you\'ve learned that when you ask them if they can do something, they always say yes, regardless of whether or not they can actually do it. If they can\'t do it, then you have to do it. Lucky you, this happens to be one of the instances where they can do what they say they can do.' ,
    'difficulty': 1, # 1-3
    'passEffect': [200, 25],
    'failEffect': [150, -30],
    'selected': False
  },
  '4': {
    'name': 'Routine Work - OVERSEAS COWORKERS',
    'descrip': 'Some of your coworkers live and work abroad in countries whose populaces struggle heavily with the basics of the English language. Every now and then you have to coordinate with them to complete projects. After having worked with these coworkers a few times now, you\'ve learned that when you ask them if they can do something, they always say yes, regardless of whether or not they can actually do it. If they can\'t do it, then you have to do it. UNLUCKY for you, this is one of those cases where they CANNOT do it.' ,
    'difficulty': 3, # 1-3
    'passEffect': [300, 25],
    'failEffect': [100, -75],
    'selected': False
  },
  '5': {
    'name': 'Routine Work - A Okay :)',
    'descrip': 'No problems today, everything is running smoothly. You decided to relax and catch up on some tv.' ,
    'difficulty': 1, # 1-3
    'passEffect': [200, 25],
    'failEffect': [150, 0],
    'selected': False
  },
  '6': {
    'name': 'Routine Work - A Okay :)',
    'descrip': 'No problems today, everything is running smoothly. You decided to relax and catch up on some tv.' ,
    'difficulty': 1, # 1-3
    'passEffect': [200, 25],
    'failEffect': [150, 0],
    'selected': False
  },
  '7': {
    'name': 'Special Mission - IN THE CLOUD',
    'descrip': 'One of your bosses call you in for a special meeting. They tell you how one of them read an article in People about how the Cloud is an important technology for business that want to stay relevant. He wants you to be in charge of migrating the company\'s data to the cloud. He\'s charted a few airplanes to help you get the data there and gives you a company credit card to buy things you\'ll need for this operation. Figure out how to give him what he wants.' ,
    'difficulty': 4, # 1-3
    'passEffect': [700, 50],
    'failEffect': [150, -25],
    'selected': False
  },
  '8': {
    'name': 'Special Mission - SQUARE TRIANGLES',
    'descrip': 'Your bosses inform you that one of your clients has requested the production of a square triangle. The square triangle will be used in another project with a completion deadline of 1 month from today. The purpose of the web app is to help users optimize workflow, predict future outcomes, and flourish regardless of future market conditions using the power of the cloud. Figure out how to give them what they want.' ,
    'difficulty': 3, # 1-3
    'passEffect': [300, 25],
    'failEffect': [150, -50],
    'selected': False
  },
  '9': {
    'name': 'Routine Work - Maintenance',
    'descrip': 'You attempt to perform routine maintenance.' ,
    'difficulty': 2, # 1-3
    'passEffect': [200, 25],
    'failEffect': [150, -25],
    'selected': False
  },
  '10': {
    'name': 'Routine Work - Maintenance',
    'descrip': 'You attempt to perform routine maintenance.' ,
    'difficulty': 2, # 1-3
    'passEffect': [200, 25],
    'failEffect': [150, -25],
    'selected': False
  },
  '11': {
    'name': 'Routine Work - Half Day',
    'descrip': 'Some of your bosses rock. Bob, is one of those bosses, tells you that if you can do quick server configuration for a special client, you can take the rest of the day off.' ,
    'difficulty': 1, # 1-3
    'passEffect': [300, 35],
    'failEffect': [150, 0],
    'selected': False
  },
  '12': {
    'name': 'Routine Work - Server Upgrade',
    'descrip': 'It\'s a routine server upgrade that\'s been tested in a controlled environment. What could possibly go wrong? Murphy\'s law - Whatever can go wrong will go wrong.' ,
    'difficulty': 3, # 1-3
    'passEffect': [300, 25],
    'failEffect': [150, -50],
    'selected': False
  },
  '13': {
    'name': 'Routine Work - Maintenance',
    'descrip': 'You attempt to perform routine maintenance.' ,
    'difficulty': 2, # 1-3
    'passEffect': [200, 25],
    'failEffect': [150, -25],
    'selected': False
  },
  '14': {
    'name': 'Routine Work - Server Upgrade',
    'descrip': 'It\'s a routine server upgrade that\'s been tested in a controlled environment. What could possibly go wrong? Murphy\'s law - Whatever can go wrong will go wrong.' ,
    'difficulty': 3, # 1-3
    'passEffect': [300, 25],
    'failEffect': [150, -50],
    'selected': False
  }
}