import matplotlib.pyplot as plt

def create_plot():
    months = ["Jan", "Feb", "Mar", "Apr", "May"]
    sales = [100, 150, 120, 180, 200]
    plt.plot(months, sales, marker="o")
    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.show()

create_plot()