# Pizza-parlour-Study
Generated K points where the pizza station must be placed in order to achieve maximum customers.

## Problem Statement 
Given the list of locations of customers who frequently order pizza we want to find out the optimal locations of pizza  parlours where they should be opened.

__Data Set__ - Generated data from sklearn library using make_blobs which generates the data in the form of clusters with K cneters and return data depending upon the parameters passed to it( like- number of centers and number of features etc ). You can check out further about make_blocks at this <a href="https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html">Documentation</a>.

__Algorithm__ - I have used Kmeans algorithm for generating the K centers where the pizza shops should be placed in order to get the maximum customers.<br>
Main idea behind the algorithm is to first select K random points from the data given and then assigning them nearest neighbours and then again taking mean of the points and updating the centers according to the mean and then assigning the new centers with points near to them carry on this algorithm till you achieved the saturation point.

__Terms used in the code__
- __X__ : It refers to the data containing 500 points with 2 features i.e, x and y coordinates. The shape of the data i
          s 500 X 2.
- __K__ : It refers to the no. of clusters or number of pizza parlours you want in order to achieve optimal position. You need           to input K and value should be samller than 10 as i have assingned color to each cluster and to increase the k more             than 10 then you need to increase colors in the color list contating the colors.
- __make_cluster__ : This function makes a dictionary of dictionary named as clusters which keep track of the properties that                         are attached with each point.
- __distance()__ : This function is to calculate and return the distance between two points or can say between two vectors.
- __Assignpoints()__ : This function calcuate the distance of each point with the corresponding K centers and assing the point                        to that center which is nearest to the point.
- __UpdateCenter()__ : This function is to calculate the mean of the assinged points to each center and then again updates the                        center and return the old centers in the form of lists.
- __PlotCluster()__ : This function simply plots the points and their corresponding centers.
- __Predict()__ : It manages and calls the other functions and search for the optimal solution and returns the optimal centers                   when the optimum position is achieved. 
