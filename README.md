# Hafnian in Python

This project relates to my work in the McMahon Lab in the School of Applied and Engineering Physics at Cornell University. As part of my research on Gaussian Boson Sampling (GBS), I would like to further understand the hafnian and its (classical) computation, so I created this project to code algorithm(s) for its computation in Python. By the end of this project, I hope to better understand the hafnian, its classical computation, and how the complexity scales as graphs/matrices grow in size.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

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

into your Windows command line (I am using Windows and this doesn't constitute anything major in my research so I am hoping I won't have to write instructions for other systems, since I don't know what the differences are).

The automated test file makes use of some other libraries, namely networkx, matplotlib, unittest, and thewalrus, but these are not necessary unless you are interested in implementing and testing your own algorithm. They can be installed the same way as numpy.

## Contributing

Feel free to contribute! I am not doing anything revolutionary or groundbreaking, so if you stumble upon this and want to contribute, just go for it.

## Authors

* **Brady Sites** - *Initial work* - [sradybites](https://github.com/sradybites)

## Acknowledgments

* The paper I referenced in the paragraph above: https://arxiv.org/pdf/1107.4466.pdf
* Xanadu's definitive library for GBS: https://the-walrus.readthedocs.io/en/latest/
