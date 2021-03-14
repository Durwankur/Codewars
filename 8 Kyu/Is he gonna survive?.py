#Solution 1:
def hero(bullets, dragons):
    return True if bullets>=2*dragons else False
  
#Solution 2:
import math
def hero(bullets, dragons):
    return True if math.floor(bullets)/2>=dragons else False
