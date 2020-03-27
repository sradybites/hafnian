# Hafnian in Python

This project relates to my work in the McMahon Lab in the School of Applied and Engineering Physics at Cornell University. As part of my research on Gaussian Boson Sampling (GBS), I would like to further understand the hafnian and its (classical) computation, so I created this project to code algorithm(s) for its computation in Python. Currently, I am implementing the first algorithm presented in the paper listed in the Acknowledgments section. I plan on coding both the algorithms presented in the aforementioned paper, but I may not find it necessary after having done the first one. By the end of this project, I hope to better understand the hafnian, its classical computation, and how the complexity scales as graphs/matrices grow in size.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

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

## Contributing

Up to a certain point in my work I discourage contributions since I want to figure the details out for myself (after all, it is a personal learning project). After I finish, I guess I'll allow contributors, although I don't really expect there to be any.

## Authors

* **Brady Sites** - *Initial work* - [sradybites](https://github.com/sradybites)

## License

I don't understand licensing yet but I'll be sure to upgrade this section once I do!

## Acknowledgments

* The paper I referenced in the paragraph above: https://arxiv.org/pdf/1107.4466.pdf
* Xanadu's definitive library for GBS: https://the-walrus.readthedocs.io/en/latest/
