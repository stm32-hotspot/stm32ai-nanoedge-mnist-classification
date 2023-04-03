# MNIST NanoEdge AI Studio project example

This repository contains the project shown at the NanoEdge AI Studio workshop (which is a ST software). This is a classification project with the MNIST dataset.

In the folder /MNIST classification with NEAI, you will find 2 folders:
* /project_template contains everything to do the project, but you do all the steps in the notebooks
* /project6_done contains the completed project


## Contents
- [Prerequisites](#prerequisites)
- [Mnist-dataset](#mnist-dataset)
- [The project](#description-of-the-project)
- [Project architecture](#project-architecture)

## Prerequisites

* Python (here we were using python version 3.9.10)
* Python libraries:
	* numpy 
	* pandas
	* PIL
	* matplotlib
	* idx2numpy

To install python : https://www.python.org/
To install a library, open a cmd and type: **pip install [library_name]**


## Mnist dataset

The dataset files are already in the folder /data in both project, but you can find the original page here: http://yann.lecun.com/exdb/mnist/
The dataset is composed of 4 .zip files of idx format:
* train images
* train labels
* test images
* test labels

## how to do the project

In both folders (project_template or project_done), you will find 2 notebooks (.ipynb files) and 1 script (.py)

In the notebooks, you will find comment on every steps.

In the case of /project_done, the project is finished, so you can play with the classifier and the png digit using the classify.py script. Just open a cmd and run the command (at the right path): **python classify.py**

Else, if you want to redo the project from scratch, go to the /project_template folder and do the following:

* First, use the Data_manipulation.pynb notebook to extract the data, convert them and visualize them. Then you will split the data containing all the digits (from 0 to 9) to multiple .csv containing only one kind of digits, to be later used in NanoEdge AI Studio.

* Then we the CLI_and_Emulator.ipynb to create a NanoEdge AI Studio project using the CLI (command line interface). In this notebook, you will first find all the step to use the CLI in the cmd, from launching the engine to completing the project. Then you will find an example on how to use the emulator with python.

* Finnaly, you will also find a python script to load a png image and use the model trained with the second notebook to classify the image as a digit between 0 to 9. In the video, we use paint to create the digits and the script to classify it. Same, use the command: **python classify.py**

## Project architecture

If you clone this project, you will find:
 * a folder /data, containing the MNIST dataset original zip files.
 * a folder /emulators, it is the emulator trained in the workshop, if you are in /project_template, you will get it at a certain point.
 * two folders, /train_files and /test_files that contains .csv files for each digits (0 to 9) that we use to create the model with the CLI.
 * a folder /neai_cli_win_v2022.10.18.0, which is the CLI that we use. You can delete it and use the last one, downloadable on NanoEdge AI Studio.
 * Two notebooks and python script described above.
 * a png file, of size 28x28 were we draw digit and classify them with the python script.

