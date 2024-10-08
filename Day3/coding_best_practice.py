import numpy as np

story = ['Crisp, clear skies cradled the quaint countryside. ',
         'Cascading cherry blossoms danced in the gentle breeze, captivating curious critters that chirped cheerfully. ',
         'Cloaked in a cloak of curiosity, a clever cat named Clementine crept cautiously through the cobblestone streets.\n ',
         'Caught by the scent of freshly baked cookies, Clementine followed her nose to a cozy cottage nestled among cedar trees. ',
         'Curious, she crept closer, craving a crumb of the confectionary delight. ',
         'Cautiously, she climbed onto the windowsill, casting a curious glance inside.\n ',
         'Cuddled by the fireplace, an elderly couple clinked their cups of cocoa, chuckling over cherished memories. ',
         'Caught off guard, they caught sight of Clementine, their eyes widening in surprise. ',
         'Chuckling, the couple welcomed the curious cat inside, sharing their cookies and tales of their travels.\n ',
         'Content and cozy, Clementine curled up by the crackling fire, her curiosity satisfied. ',
         'In that charming cottage, amidst laughter and companionship, Clementine discovered that sometimes, the sweetest moments come from embracing curiosity and connecting with kindred spirits. ']

cs = 0
tale_string = ''
for el in story:
    tale_string += el
a = tale_string.split()
for alet in a:
    if alet.startswith('C') or alet.startswith('c'):
        cs += 1
print(cs)