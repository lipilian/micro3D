# %% import the package
import cv2
print(cv2.__version__)
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame, Series  # for convenience
import pims
import trackpy as tp
import numpy as np
from scipy import misc
import glob
import inspect
import argparse
# %% parameter need to set
plt.ioff()
def main():
    estimateFeatureSize = args.Size # must be odd numer
    path = args.Path
    minMass = args.MinMass
    separation = args.Seperation
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    f = tp.locate(img, estimateFeatureSize)

    fig, ax = plt.subplots()
    plt.ioff()
    ax.hist(f['mass'], bins=20)
    ax.set(xlabel='mass', ylabel='count');
    fig.savefig('mass.png')

    h1 = plt.figure(figsize=(12,12))
    f = tp.locate(img, estimateFeatureSize, minmass= minMass, separation =2)
    tp.annotate(f, img);
    h1.savefig('target.png')

    f.to_csv(r'./CenterPoints.csv')
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--Path", type=str, help="Path to save the images")
    parser.add_argument("-s", "--Size", type=int, help="Feature Size")
    parser.add_argument("-m", "--MinMass", type=int, help="minMass required for the feature")
    parser.add_argument("-sp", "--Seperation", type=int, help="minDistance between features")
    args = parser.parse_args()
    main()
