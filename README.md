# Embedded Python Sample Interface

By using tools such as; Python, OpenCV, Numpy, JavaScript, the objective is to create an embedded program with Python that manages to process images, figures or elements that it receives from the Spica emulator and sends them via http protocol to another server. 

<br>

Below you can see images that demonstrate the operation of the image recognition module in which both the centroids and the contours of said images are found. 

<br>

<img width="825" alt="Screen Shot 2019-12-16 at 5 59 47 PM" src="https://cdn.discordapp.com/attachments/872649781221130261/889678124873293905/colores.png">

<br>

It should be noted that within this module the following data must be obtained:
- Particle Detection    
    - Oxygen
    - Hydrogen 
    - Air particles
- Centroid
- Outline

<br>

## Installation requeriments for project
In order to test the effectiveness of the python application, as a first step, clone the repository 

```
    $ git clone 
    https://github.com/DarAkus1420taller-de-integracion-3.git		
```

<br>

Below are the commands that must be executed by console before being able to execute and test the functionality of our project


```console
    $ npm install 
    $ pip install -r requeriments.txt
    $ npx husky install		
```

<br>

## Description of the background of the code implemented in the project

Throughout the programming carried out in the different modules, the implementation of different algorithms can be noticed, among which it is worth highlighting

- hough transform algorithm:
    - The Hough transform is a technique for detecting figures in digital images. This technique is mostly used in the field of Computer Vision. With the Hough transform it is possible to find all kinds of figures that can be expressed mathematically, such as lines, circles or ellipse
    
    <br>

    In the following image we can clearly appreciate the efficiency of the application of this algorithm through the same filter that I dealt with previously. 
    
    <img width="825" alt="Image filter hough" src="https://cdn.discordapp.com/attachments/786409916495298600/895312645169750056/unknown.png">

<br>

- bayesian algorithm
    - Bayesian optimization works by constructing a posterior distribution of functions (Gaussian process) that best describes the function you want to optimize. As the number of observations increases, the posterior distribution improves and the algorithm becomes more certain of which regions of the parameter space are worth exploring.  

    <br>

    <img width='825' alt='Gif bayesian filter' src='https://github.com/simsimi2143/BayesianOptimization/blob/master/examples/bayesian_optimization.gif?raw=true'>


<br>

## Licence of project

MIT License

Copyright (c) 2021 DarAkus1420

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


<img width="1050" alt="Screen Shot 2019-12-16 at 5 59 47 PM" src="https://cdn.discordapp.com/attachments/786409916495298600/896220482964181042/unknown.png">