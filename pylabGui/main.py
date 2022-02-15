import matplotlib.pyplot as plt
import numpy as np


def run():

    datasize = 1000

    # Make synthetic data:
    xData = np.random.randint(100, size=datasize)
    yData = np.linspace(0, datasize, num=datasize, dtype=int)

    # Make and show plot
    plt.plot(xData, yData, '.k')
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
