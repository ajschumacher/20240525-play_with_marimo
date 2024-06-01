import marimo

__generated_with = "0.6.6"
app = marimo.App()


@app.cell
def __():
    import numpy as np
    return np,


@app.cell
def __(np):
    M = np.array([[0, 0, 0, 0, -3],
                  [1, 0, 0, 0,  6],
                  [0, 1, 0, 0,  0],
                  [0, 0, 1, 0,  0],
                  [0, 0, 0, 1,  0]])
    return M,


@app.cell
def __(M, np):
    np.linalg.matrix_power(M, 5) - 6 * M + 3 * np.eye(5)
    return


if __name__ == "__main__":
    app.run()
