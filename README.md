# Software Engineering 435 - Project 1

## Description

This program is written in python and works by accepting the folder name with our designated data (ie Programming-Assignment-Data) to produce the required annotated outputs. As such, there are several libraries we must import and potentially install: cv2, re, sys, os. The XML files were parsed to identify the bounds of the leaf nodes. The location of these bounds was then drawn onto the .png images.

## Library Instructions

Run the following installation command before executing the program:

1. pip install opencv-python

## Execution

The program can be executed through the command line in the following format: **python Solution.py [XML/PNG folder path]**. For example, **python Solution.py Programming-Assignment-Data** will produce an input of all our .xml files to be parsed and output each annotated verison of the .png images.

## Design Decisions

Initially, the student used Java to parse the XML files, however since there wasn't an easy method to draw on the bounds of the leaf nodes onto the .png images, the project was transitioned to python for simplicity. Python's cv2 library allows for easy image editing capabilities and built-in methods for drawing lines and rectangles, so given the necessity to draw on boxes around the leaf nodes, python seemed like a more intuitive solution.
