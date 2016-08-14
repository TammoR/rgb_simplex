import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def plot_rgb_image(image, figsize=(6, 6), fontsize=18, dpi=150,
                   labels=True):
    """
    plot rgb simplex.
    image is an array of shape (X,Y,3)
    """

    x_size, y_size, _ = image.shape

    font = {'family': 'serif',
            'size': 18}
    matplotlib.rc('font', **font)

    fig = plt.figure(figsize=figsize, dpi=dpi, facecolor='white')
    ax = fig.add_subplot(111)
    ax.axis('off')

    if labels is True:
        ax.text(-.1*x_size, -.1*y_size, 'p(u=0)=1')
        ax.text(x_size - .05*x_size, -.1*y_size, 'p(u=1)=1')
        ax.text(x_size/2-.1*x_size, y_size - .1*y_size, 'p(u=1/2)=1')

    ax.imshow(M, interpolation='nearest',
              aspect='equal', origin='lower')

    return fig


if __name__ == '__main__':

    x_size = float(500)  # this parameter controls the resolution
    scale_f = np.sqrt(.75)  # scaling parameter = sin(60)
    y_size = x_size*scale_f

    # define rgb array
    M = np.zeros([int(y_size), int(x_size), 3])

    # iterate over array and create rgb simplex
    for x in range(int(x_size)):
        for y in range(int(y_size)):
            # along the horizontal decrease red and increase blue
            # along the vertical decrease green
            M[y, x, 0] = x/x_size
            M[y, x, 1] = y/y_size
            M[y, x, 2] = 1-x/x_size

            # along the vertical decrease blue/red
            M[y, x, 0] *= 1-y/y_size
            M[y, x, 2] *= 1-y/y_size

            # Cut out triangle
            if y*(1/np.tan(60*(2*np.pi/360))) > x and x <= x_size/2:
                for i in range(3):
                    M[y, x, i] = 1
            if y*(1/np.tan(60*(2*np.pi/360))) > x_size-x and x >= x_size/2:
                for i in range(3):
                    M[y, x, i] = 1

    fig = plot_rgb_image(M)
    fig.show()

