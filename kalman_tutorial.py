import matplotlib.pyplot as plt
from random import random
z_true = 1
z_dev = 0.1

xk_1 = 1
Pk_1 = 1
Qk = 1e-5
Rk = 0.01**2

for _ in range(1000):
    x_list = []
    z_list = []
    for i in range(50):

        zk = z_true + z_dev*random()
        xk_ = xk_1
        Pk_ = Pk_1 + Qk
        k_gain = Pk_ / (Pk_ + Rk )
        xk = xk_ + k_gain*(zk - xk_)
        Pk = (1 - k_gain)*Pk_

        x_list.append(xk)
        z_list.append(zk)

        xk_1 = xk
        Pk_1 = Pk


    #
    # plt.title(plot_title)
    plt.plot(range(50), x_list,'g',linestyle ='-',label = 'estimate')
    # #test trilateration
    plt.plot(range(50), z_list,'b',linestyle ='--',label = 'measurement')
    #
    # plt.plot(gt_diagonal_x, gt_diagonal_y,'r*',linestyle='--' , label = 'GT')
    # # marker o x + * s:square d:diamond p:five_pointed star
    plt.legend()
    plt.xlim(0.0, 50)
    # plt.xticks(np.linspace(-0.5,1.5,10, endpoint =True))
    # plt.xticks(np.linspace(-0.5,1.5,10, endpoint =True))
    plt.ylim(-0,1.2)
    plt.xlabel("X_axis")
    plt.ylabel("Y_axis")
    fig = plt.gcf()
    plt.show()
    plt.pause(0.01)
    plt.close()
