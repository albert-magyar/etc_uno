# Electronic throttle control for the Arduno Uno

## Prerequisites

In order to use this controller, you must install [Python 2.7](https://www.python.org/downloads/release/python-2712/).

## Setup

First, clone the repository, setup pip (a Python package manager), and install the necessary Python packages.

```bash
git clone https://github.com/albert-magyar/etc_uno
cd etc_uno
python get-pip.py
pip install numpy
pip install matplotlib
pip install pySerial
```

Next, plug in the ETC controller to your computer's USB port and the MoTeC Driver TPS1/2 inputs (DTM connector).

## Using the controller.

```bash
python controller.py
```
