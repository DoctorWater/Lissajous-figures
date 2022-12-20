import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x_frequency = float(input("Enter x frequency relatively to y frequency\n"))
    y_frequency = float(input("Enter y frequency relatively to x frequency\n"))
    phase_difference = np.pi * float(input("Enter pi multiplier for the phase difference\n")) - (np.pi/2)
    t = np.linspace(-10, 10, 1000, endpoint=False)
    x = []
    y = []

    for i in t:
        x_i = np.sin(x_frequency * i + phase_difference)
        y_i = np.sin(y_frequency * i)
        x.append(x_i)
        y.append(y_i)

    # plot the graph
    plt.plot(x, y)

    # set the title
    plt.title('Plot sin(' + str(y_frequency) + 't)' + ' Vs sin(' + str(x_frequency) + 't)')

    # set the labels of the graph
    plt.xlabel('sin(' + str(x_frequency) + 't)')
    plt.ylabel('sin(' + str(y_frequency) + 't)')

    # display the graph
    plt.show()
