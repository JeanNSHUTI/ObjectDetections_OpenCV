# Object Detection with OpenCV

Using Canny Edge Detector and OpenCV for detecting objects.

## Getting Started

This is meant to be a simple guide on how to install OpenCV, numpy and all tools needed to experiment with 
the Canny Edge Detector and identifiying objects in images and/or in video frames such as the video captured
from a webcam device connected on your computer.
This guide assumes that you already have python installed and working on your computer here: 

```
https://www.python.org/downloads/
```

More information on the Canny Edge Detector:

```
https://docs.opencv.org/3.1.0/da/d22/tutorial_py_canny.html
```

### Installing OpenCV

1.	Go here and find the OpenCV installation package (.whl) that suits your PC and python version best.
	With python 3.6 installed and a x86 machine I chose the package "opencv_python-3.3.1-cp36-cp36m-win32.whl"
2.	Place this file into the source file where your python version is installed. (
	eg C:\Users\Dell\AppData\Local\Programs\Python\Python36-32)
3.	Open the command line and type the following:

```
python –m pip install "python folder location + name_of_openCVfile.whl"
```

### Installing additional packages

Run the following commands to install numpy and matplotib:

```
python -m pip install numpy
```

```
python -m pip install matplotlib
```

### Running Tests
#### script.py

In the command line, navigate to the folder containing your source code and run script.py as a first test:

``` 
