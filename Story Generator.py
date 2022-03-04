import random

when = ['Once upon a time','A long time ago','A few days ago','Last night','A while back']
who = ['a rat', 'a lion', 'an elephant', 'a rabbit', 'a cat', 'a dog']
place = ['England','India','Russia','Germany','USA','Italy']
went = ['cinema','kitchen','laundry','school','restaraunt']
happend = ['ate a burger','made new friends','wrote a song','solved a riddle','found a treasure']

print(random.choice(when) + ' , ' + random.choice(who) + ' who lived in ' + random.choice(place) + ' , went to the ' + random.choice(went) + " and " + random.choice(happend))