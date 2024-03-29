import numpy as np 

def map_feature(x1, x2):
#   x1, x2 type: numpy array
#   Returns a new feature array with more features, comprising of 
#   x1, x2, x1.^2, x2.^2, x1*x2, x1*x2.^2, etc.

    degree = 6
    out = np.ones([len(x1), int((degree + 1) * (degree + 2) / 2)])
    idx = 1

    for i in range(1, degree + 1):
        for j in range(0, i + 1):
            a1 = x1 ** (i - j)
            a2 = x2 ** j
            out[:, idx] = a1 * a2
            idx += 1

    return out

def map_feature_one_point(x1, x2):
    # the same as map_feature function but for just 1 point (x1, x2),
    # not the whole array of x1 and x2.
    degree = 6
    out = np.ones(int((degree + 1) * (degree + 2) / 2))
    idx = 1

    for i in range(1, degree + 1):
        for j in range(0, i + 1):
            a1 = x1 ** (i - j)
            a2 = x2 ** j
            out[idx] = a1 * a2
            idx += 1

    return out