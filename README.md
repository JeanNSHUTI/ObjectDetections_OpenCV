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

1.	Go here (https://www.lfd.uci.edu/~gohlke/pythonlibs/) and find the OpenCV installation package (.whl) that suits your PC and python version best.
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

* Python version 3.6 -> "python" does not not work, use "py"

```
python -m pip install matplotlib  #plotting library based on NumPy.
```

```
python -m pip install scipy  #SciPy is a scientific Python library, which supplements and slightly overlaps NumPy 
```

```
python -m pip install scikit-image  #provides image processing routines for SciPy. Steps 1 - 3 -> installation 
```

```
python -m pip install imutils
```

### Running Tests
#### Canny2.py

In the command line, navigate to the folder containing your source code and run script.py as a first test:

``` 
python script_name.python
```

You should find an original image of yourself and the canny-edge version:

[![Canny Edge Detector](https://github.com/JeanNSHUTI/ObjectDetections_OpenCV/blob/master/canny2.jpg)](#CannyEdgeDetector)

#### Cannyjpg.py

[![Object detection via image](https://github.com/JeanNSHUTI/ObjectDetections_OpenCV/blob/master/cannyjpg1.jpg)](#ObjectdetectionImage)

#### Canny-colour.py

[![Object detection via video](https://github.com/JeanNSHUTI/ObjectDetections_OpenCV/blob/master/cannycolour.jpg)](#ObjectdetectionVideo)
[![Object detection via video](https://github.com/JeanNSHUTI/ObjectDetections_OpenCV/blob/master/cannycolour1.jpg)](#ObjectdetectionVideo)

#### Ball_tracking.py and plot_canny.py

These are open source examples that experiment with edge detection and the sensitivity of the canny edge detector

## References

https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
https://henrydangprg.com/2016/06/26/color-detection-in-python-with-opencv/