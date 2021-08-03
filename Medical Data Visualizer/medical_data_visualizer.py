import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
overweight = []
for i in range(len(df)):
    bmi = df['weight'][i] / (df['height'][i] / 100) ** 2
    overweight.append(int(bmi > 25))
    
df['overweight'] = overweight

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
for i in range(len(df)):
    if(df['cholesterol'][i] == 1):
        df.at[i, 'cholesterol'] = 0
    else:
        df.at[i, 'cholesterol'] = 1
        
    if(df['gluc'][i] == 1):
        df.at[i, 'gluc'] = 0
    else:
        df.at[i, 'gluc'] = 1

def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    #df_cat = None

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(x ="variable", hue = "value", col ="cardio", data = df_cat, kind ="count")
    g.set_axis_labels("variable", "total")
    fig = g.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype = bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask = mask , vmax = .258, center = 0, 
            square = True, linewidths = .5, cbar_kws = {"shrink": .5}, annot = True, fmt ='.1f')
    
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig