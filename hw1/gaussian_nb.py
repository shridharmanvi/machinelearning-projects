from __future__ import division

__author__ = 'shridharmanvi'

import math


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

if __name__ == '__main__':
    data = list(three)
    print data
    data_dict = {}
    data_stats = {}
    n_dimension = 3
    features = ['height', 'weight', 'age']
    #  Below, converting data to desired format for easier calculation
    for obs in data:
        key = obs[1]
        value = obs[0]
        try:
            data_dict[key].append(list(value))
        except KeyError:
            data_dict[key] = [list(value)]
    #  Data is now in  data_dict dictionary in desired format

    #  Calculate mean and standard deviation for each feature given class - Calculating the priors
    for cl in data_dict.keys():  # for every class
        print cl
        values = data_dict[cl]
        for i in range(0, n_dimension):  # for evey feature, ex: age, height, weight etc.
            li = []
            values = data_dict[cl]
            for j in range(0, len(data_dict[cl])):  # for data point
                li.append(values[j][i])

            print li
            mean = sum(li)/len(data_dict[cl])
            print mean
            numerator = 0.00
            denominator = len(data_dict[cl])
            for k in li:
                numerator += (abs(k - mean)) ** 2

            print numerator
            print denominator

            ke_mean = str(features[i]) + '_' + 'mean' + '_' + cl
            ke_sd = str(features[i]) + '_' + 'sd' + '_' + cl
            data_stats[ke_sd] = math.sqrt(numerator / denominator-1)
            data_stats[ke_mean] = mean

    print data_stats




