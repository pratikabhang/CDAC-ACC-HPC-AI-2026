import seaborn as sns
import matplotlib.pyplot as plt

def create_plot():
    data = {"Marks": [65, 70, 75, 80, 85, 90, 95]}
    sns.histplot(data["Marks"], bins=5)
    plt.title("Marks Distribution")
    plt.show()

create_plot()