__author__ = 'shridharmanvi'

import numpy as np
from sklearn.naive_bayes import GaussianNB

three = {(
(170, 57, 32),
(190, 95, 28),
(150, 45, 35),
(168, 65, 29),
(175, 78, 26),
(185, 90, 32),
(171, 65, 28),
(155, 48, 31),
(165, 60, 27),
(182, 80, 30),
(175, 69, 28),
(178, 80, 27),
(160, 50, 31),
(170, 72, 30))
}

g = np.array(three)

x = np.array([[1,2,3],[2,4,3],[7,-1,-9],[6,4,5]])

y = np.array(['W','M','M','W'])


clf = GaussianNB()

clf.fit(x, y)

GaussianNB()

x = clf.predict([3, 4, 3])

print x

