import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize = (16, 5))
    plt.scatter(x = df['Year'], y = df["CSIRO Adjusted Sea Level"])
    
    # Create first line of best fit
    first_x = []
    first_y = []
    first_slope, first_intercept, _, _, _ = linregress(df['Year'], df["CSIRO Adjusted Sea Level"])
    for i in range(1880, 2051):
      first_x.append(i)
      first_y.append(first_slope * i + first_intercept)
    plt.plot(first_x, first_y, 'g')
    
    # Create second line of best fit
    df = df[df.Year >= 2000]
    second_x = []
    second_y = []
    second_slope, second_intercept, _, _, _ = linregress(df['Year'], df["CSIRO Adjusted Sea Level"])
    for i in range(2000, 2051):
      second_x.append(i)
      second_y.append(second_slope * i + second_intercept)
    plt.plot(second_x, second_y, 'r')
    
    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
