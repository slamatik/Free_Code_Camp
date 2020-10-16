import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')
df.index = pd.to_datetime(df.index)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
print(int(df.count(numeric_only=True)))

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df.index, df['value'], c='r')
    ax.set(xlabel='Date', ylabel='Page Views', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['month'], df['year'] = df.index.month, df.index.year
    df_bar = df.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    fig = df_bar.plot(kind="bar", figsize=(10, 10)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                       'November', 'December'], title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    df_box_mon = df_box.copy()
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df_box_mon['month'] = pd.Categorical(df_box_mon['month'], categories=months, ordered=True)
    df_box_mon.sort_values(by='month', inplace=True)

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(nrows=1, ncols=2)
    sns.boxplot(x=df_box['year'], y=df_box['value'], ax=ax[0])
    sns.boxplot(x=df_box_mon['month'], y=df_box_mon['value'], ax=ax[1])

    ax[0].set(title="Year-wise Box Plot (Trend)", xlabel='Year', ylabel='Page Views')
    ax[1].set(title="Month-wise Box Plot (Seasonality)", xlabel='Month', ylabel='Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
