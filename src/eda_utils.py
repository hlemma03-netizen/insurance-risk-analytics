import matplotlib.pyplot as plt
import seaborn as sns


def plot_histogram(df, column):
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribution of {column}")
    plt.show()


def plot_boxplot(df, column):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df[column])
    plt.title(f"Boxplot of {column}")
    plt.show()


def plot_bar(df, column):
    plt.figure(figsize=(10, 5))
    df[column].value_counts().head(10).plot(kind='bar')
    plt.title(f"{column} Counts")
    plt.show()
