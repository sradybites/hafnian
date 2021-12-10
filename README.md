# Hafnian in Python

This project relates to my work in the McMahon Lab in the School of Applied and Engineering Physics at Cornell University. As part of my research on Gaussian Boson Sampling (GBS), I would like to further understand the hafnian and its (classical) computation, so I created this project to code algorithm(s) for its computation in Python.

### Prerequisites

This project is written in Python, and I make heavy use of numpy arrays, as seen below:

```
b = m  # this line of code demonstrates the beauty of Python's dynamic typing
s = i*(curr[0, j+2]*curr[1, k+2]+curr[0, k+2]*curr[1, j+2])  # a requisite step in the first algorithm that accesses elements of a numpy array
```

### Installing

To get your dev environment working for this project, all you need are compatible versions of Python and numpy. The most recent version of Python can be downloaded from https://www.python.org/downloads/. For versions 3.4 or later, the package manager PIP is included by default, so to finish prepping, just type

```
pip install numpy
```

into your command line.

The automated test file makes use of some other libraries, namely networkx, matplotlib, unittest, and thewalrus, but these are not necessary unless you are interested in implementing and testing your own algorithm. They can be installed the same way as numpy.

## Acknowledgments

* The paper I referenced in the paragraph above: https://arxiv.org/pdf/1107.4466.pdf
* Xanadu's definitive library for GBS: https://the-walrus.readthedocs.io/en/latest/
