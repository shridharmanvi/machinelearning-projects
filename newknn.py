__author__ = 'shridharmanvi'
# Implementing k-nearest neighbors using euclidean distance

import math
import operator

three = {(
(170, 57, 32), 'W'),
((190, 95, 28), 'M'),
((150, 45, 35), 'W'),
((168, 65, 29), 'M'),
((175, 78, 26), 'M'),
((185, 90, 32), 'M'),
((171, 65, 28), 'W'),
((155, 48, 31), 'W'),
((165, 60, 27), 'W'),
((182, 80, 30), 'M'),
((175, 69, 28), 'W'),
((178, 80, 27), 'M'),
((160, 50, 31), 'W'),
((170, 72, 30), 'M')}


two = {(
(170, 57), 'W'),
((190, 95), 'M'),
((150, 45), 'W'),
((168, 65), 'M'),
((175, 78), 'M'),
((185, 90), 'M'),
((171, 65), 'W'),
((155, 48), 'W'),
((165, 60), 'W'),
((182, 80), 'M'),
((175, 69), 'W'),
((178, 80), 'M'),
((160, 50), 'W'),
((170, 72), 'M')}



def eucledian_dist(t1, t2):
    try:
        su = 0
        for i in range(0, len(t1)):
            x = (t1[i]-t2[i]) ** 2
            su+= x
        return math.sqrt(su)
    except:
        print 'Invalid input!!'


def knearest(k, t1):
    if k > len(data):
        print 'K cannot be greater than size of input array!'
    else:

        print 'Value of k:', k
        for i in range(0, len(data)):
            dist.append(eucledian_dist(data[i][0], t1))  # Calculates distances from test data to every other point in
            # training data
        #print dist
        for i in range(0, k):
            min_index, min_value = min(enumerate(dist), key=operator.itemgetter(1))  #returns the index of minimum value
            final_classes.append(data[min_index][1])  # appends the class of least distance value to a list
            print data[min_index], 'Distance:' + str(dist[min_index])
            del dist[min_index]
            del data[min_index]


if __name__ == '__main__':
    data = list(two)  # Converting input data 'set' to list
    #print 'Input data: ',  data
    dist = []
    final_classes = []
    knearest(5, (180, 85))  # Replace new data point here and assign value of k
    print 'Majority of class count from: ', final_classes
    if final_classes.count('M') >= final_classes.count('W'):
        print 'Final class assigned to test data is : M'
    else:
        print 'Final class assigned to test data is : W'



