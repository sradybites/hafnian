import numpy as np
from itertools import combinations, chain


"""
So you were working on this last on 3/26/2020. You were not doing too well.
The algorithm came from https://arxiv.org/pdf/1107.4466.pdf, pages 5 and 6.
You were stuck on how to implement the squeeze operation, since it is defined recursively
and you don't know how to use i as an input for the helper function. This was also tricky since
the squeeze factor seems to be defined in terms of the matrix from the previous stage and the current stage number.

Note: powerset is not utilized since I wrote it while I was attempting to implement the second algorithm in the paper.
When I eventually get around to writing that, I will use it again.
"""


def hafnian(m):
    """
    Computes the hafnian of a symmetric matrix
    :param m: a numpy array representing a symmetric matrix
    :return: the hafnian of m
    """
    # initialize variables
    h = 1
    b = m
    n = m.shape[0]/2

    for i in range(1, n+1):
        squeeze_factor = 1 + i*b[0, 1]
        b = squeeze_op(b, i)
        h = h*squeeze_factor
    return h


def squeeze_op(curr, i):
    """
    Performs the "squeeze" operation on the input matrix
    :param curr: a numpy array representing a symmetric matrix
    :param i: an int, stage of algorithm
    :return: a numpy array squeezed to the next stage
    """
    n = curr.shape[0]
    res = np.zeros((n-2, n-2))
    for j in range(n-2):
        for k in range(n-2):
            if j == k:
                res[j, k] = 0
            else:
                s = i*(curr[0, j+2]*curr[1, k+2]+curr[0, k+2]*curr[1, j+2])
                res[j, k] = curr[j+2, k+2] + s
    return res


def powerset(iterable):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    s = list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))
