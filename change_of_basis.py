import marimo

__generated_with = "0.6.6"
app = marimo.App()


@app.cell
def __():
    import numpy as np
    return np,


@app.cell
def __(np):
    A = np.array([[1, 0, 0],
                  [0, 2, 0],
                  [0, 0, 3]])
    return A,


@app.cell
def __(A, np):
    np.linalg.eig(A)
    return


@app.cell
def __(np):
    T = np.array([[1, 0, 1],
                  [1, 1, 0],
                  [0, 1, 1]])
    return T,


@app.cell
def __(T, np):
    np.linalg.inv(T)
    return


@app.cell
def __(A, T, np):
    B = np.linalg.inv(T) @ A @ T
    B
    return B,


@app.cell
def __(B, np):
    np.linalg.eig(B)
    return


@app.cell
def __(B, T, np):
    T @ B @ np.linalg.inv(T)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
