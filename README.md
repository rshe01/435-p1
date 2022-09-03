# Software Engineering 435 - Project 1

## Description

This program is written in python and works by accepting one prefix input (ie com.yelp.android) to produce the required annotated output. As such, there are several libraries we must import and potentially install: cv2, re, sys, os. The XML files were parsed to identify the bounds of the leaf nodes. The location of these bounds were then drawn onto the .png images.

## Library Instructions

Run the following command before executing the program if necessary:

1. pip install opencv-python

## Execution

The program can be executed through the command line in the following format: **python Solution.py [file prefixes]**. For example, **python Solution.py com.google.android.apps.transalte com.pandora.android com.yelp.android com.giphy.messenger-2 com.giphy.messenger-1 com.dropbox.android** will produce an input of all our .xml files to be parsed and an outputed each annotated verison of the .png images.

## Design Decisions

Initially, the student used Java to parse the XML files, however due to the fact that there wasn't an easy method to draw on the bounds of the leaf nodes onto the .png images, the project was transitioned to python for simplicity. Python's cv2 library allows for easy image editting capabilities and built-in methods for drawing lines and rectangles, so given the necessity to draw on boxes around the leaf nodes, python seemed like a more intuitive solution.
