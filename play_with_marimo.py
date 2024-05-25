import marimo

__generated_with = "0.6.6"
app = marimo.App()


@app.cell
def imports():
    import numpy as np
    import matplotlib.pyplot as plt
    return np, plt


@app.cell
def generate_data(np):
    x = np.random.randn(10000)
    return x,


@app.cell
def statistic(x):
    y = x.mean()
    print(y)
    return y,


@app.cell
def plot(plt, x):
    plt.hist(x, bins=100)
    plt.show()
    return


if __name__ == "__main__":
    app.run()
