import time
import winsound
import sys

def playSound(sound): #need to record sounds in wav format
  winsound.PlaySound('sounds/%s.wav' % sound, winsound.SND_FILENAME)

#default graphics[default], default sound[none], default reps[1]
#default graphics[undc], def sound[none]
def loading(*args):
  length = len(args)
  if length == 1:
    dur = args[0]
    loading_subfunct(dur, 1, 'none', 'default')
  elif length == 2:
    dur, reps = args
    loading_subfunct(dur, reps, 'none', 'default')
  elif length == 3:
    dur, reps, sound = args
    loading_subfunct(dur, reps, sound, 'default')
  elif length == 4:
    dur, reps, sounds, graphics = args
    loading_subfunct(dur, reps, sounds, graphics)
  else:
    print "invalid input"  

# function used by loading()  
def loading_subfunct(dur, reps, sounds, graphics):
  graphics = graphics_dict[graphics]
  if sounds == 'none':
    pass
  else:
    sounds.playSound(sound)

  # dur refers to total duration of graphics event
  # dur/reps = the duration of each repetition
  # the dur of each rep = len(graphics) * rep_time
  # because of mechanics of inner for-loop below
  # algebra yields the equation below
  rep_time = float(dur) / float(reps) / float(len(graphics))
  
  for j in range(0, reps):
    # make a generator
    # this is supposed to avoid memory problems with:
    #                 for b in list_A loops
    # but I don't think it does, need to learn about
    # memory optimization
    'http://stackoverflow.com/questions/4507496/read-data-from-specific-memory-address-reference-to-object'
    graphics_gen = (x for x in graphics)
    #disp_num = str(float(dur) - j * float(dur)/float(reps))[0:3]
    #should this be a feature???
    
    for i in graphics_gen:
      #print '%s' % disp_num,
      print '%s' % i,
      print '%s' % i,
      print '%s' % i,
      print '%s' % i,
      print '%s' % i,
      print '%s' % i,
      print '%s\r' % i,
      time.sleep(rep_time)
  print "                     "
    
"""GRAPHICS DICTIONARIES
Each key in graphics_dict corresponds to a list containing
the characters that will be displayed on-screen.
"""
graphics_dict = {
  'default': ['/', '|', '\\', '-']
}

"""STRING PRINT FUNCTION"""
def load_string(*args):
  length = len(args)
  if length == 1:
    words = args
    load_string_subfunct(words, 15)
  elif length == 2: 
    words, speed = args
    load_string_subfunct(words, speed) # a larger integer for speed yields faster typing
  else:
    print 'invalid input'

def load_string_subfunct(*args):
  words, speed = args
  if type(words) == tuple:
    words = words[0]
  else:
    pass
  for i in range(0, len(words)):
    sys.stdout.write(words[i]) # used instead of print. print with , have spaces in between characters
    time.sleep(float(1) / float(speed))
  print ''

"""TESTING"""
'''
load_string("""GRAPHICS DICTIONARIES
Each key in graphics_dict corresponds to a list containing
the characters that will be displayed on-screen.
""")'''
#loading(2, 6, 'none', graphics_dict['default'])