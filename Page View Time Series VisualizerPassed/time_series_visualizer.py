import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to "date".)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col = "date")

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize = (16, 5))
    plt.plot(df, 'r')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.xticks(range(0, len(df), len(df) // 7))
    plt.ylabel("Page Views")

    # Save image and return fig (don"t change this part)
    fig.savefig("line_plot.png")
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    months_dict = {
      "01" : "January", 
      "02" : "February", 
      "03" : "March", 
      "04" : "April", 
      "05" : "May", 
      "06" : "June", 
      "07" : "July", 
      "08" : "August", 
      "09" : "September", 
      "10" : "October", 
      "11" : "November", 
      "12" : "December"   
      }
    bar_list = []
    for i in range(len(df)):
      bar_list.append([df.index[i].split("-")[0], months_dict[df.index[i].split("-")[1]], df["value"][i]])

    # Draw bar plot
    fig = plt.figure(figsize = (12, 12))
    df_bar = pd.DataFrame(bar_list, columns = ["Years", "Months", "Average Page Views"])
    sns.barplot(x ="Years", y ="Average Page Views", hue ="Months", hue_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], data = df_bar, ci = 0, saturation = 1)
    
    # Save image and return fig (don"t change this part)
    fig.savefig("bar_plot.png")
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done ! )
    months_dict = {
      "01" : "Jan", 
      "02" : "Feb", 
      "03" : "Mar", 
      "04" : "Apr", 
      "05" : "May", 
      "06" : "Jun", 
      "07" : "Jul", 
      "08" : "Aug", 
      "09" : "Sep", 
      "10" : "Oct", 
      "11" : "Nov", 
      "12" : "Dec"   
      }
    df_box = df.copy()
    df_box.reset_index(inplace = True)
    df_box["Year"] = [df.split("-")[0] for df in df_box.date]
    df_box["Month"] = [months_dict[df.split("-")[1]] for df in df_box.date]
    df_box.rename(columns = {"value": "Page Views"}, inplace = True)

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize = (16, 5))
    sns.boxplot(ax = axes[0], x ="Year", y ="Page Views", data = df_box).set_title("Year-wise Box Plot (Trend)")
    sns.boxplot(ax = axes[1], x ="Month", y ="Page Views", data = df_box, order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]).set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don"t change this part)
    fig.savefig("box_plot.png")
    return fig
