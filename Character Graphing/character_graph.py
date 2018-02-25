import re
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt

regex = re.compile('[^a-zA-Z]')

count = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0,'e' : 0,'f' : 0,'g' : 0,'h' : 0,'i' : 0,'j' : 0,'k' : 0,
        'l' : 0,'m' : 0,'n' : 0,'o' : 0,'p' : 0,'q' : 0,'r' : 0,'s' : 0,'t' : 0,'u' : 0,'v' : 0,
        'w' : 0,'x' : 0,'y' : 0,'z' : 0}
count2 = {}

i = 0

with open("war_and_peace.txt") as f:
    for line in f.readlines():
        i += 1
        words = line.lower().split()
        for word in words:
            word = regex.sub('', word)
            for character in word:
                count[character] += 1

        if i % 200 == 0:
            for character in sorted(count):
                count2.update({character : count[character]})


            objects = tuple(count2.keys())
            y_pos = np.arange(len(objects))
            performance = list(count2.values())

            plt.bar(y_pos, performance, align='center', alpha=0.5, color='#1995AD')
            plt.xticks(y_pos, objects)
            plt.ylabel('Usage')
            plt.xlabel('Characters')
            plt.title('Character usage')
            plt.savefig('./images/{}.jpg'.format(i))
