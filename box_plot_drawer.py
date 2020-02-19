import matplotlib.pyplot as plt
import collections
import numpy as np
import os

COLORSET = [(241/255.0, 101/255.0, 65/255.0), (19/255.0, 128/255.0, 20/255.0), (191/255.0, 17/255.0, 46/255.0), (2/255.0, 23/255.0, 157/255.0)]

data_pozyx = [[1,2,5], [5,7,2,2,5], [7,2,5]]
data_RO_SLAM = [[6,4,2], [1,2,5,3,2], [2,3,5,1]]
data_MLP = [[6,4,2], [1,2,5,3,2], [2,3,5,1]]
data_BI_LSTM = [[6,4,2], [1,2,5,3,2], [2,3,5,1]]
data_OURS = [range(1,10), [1,2,5,3,2], [2,3,5,1]]

ticks = ['0_33', '0_66', '1']

class BoxPlotModule:
    def __init__(self):
        self.tmp_dict = None
        self.gt_dir_path = None
        self.dict_gt = None

        self.plt = plt

        self.target_dir_path = {}
        self.dict_al = collections.OrderedDict()

        self.dict_error = collections.OrderedDict()

        self.list_al_name = None
        self.ticks = []

        # self.color_set = ['#34B291', '#FFC000', '#EE3030', '#30EE30', '#3030EE']
        self.color_set = COLORSET

    def do_test(self, gt_path, al_path_list):
        # self.load_gt_set(gt_path)
        for al_path in al_path_list:
            self.load_al_set(al_path, os.path.split(al_path)[1])
        # self.get_dict_error()
        self.do()

    def load_gt_set(self, dir_path):
        self.gt_dir_path = dir_path
        self._read_data_from_gt_(dir_path)

    def load_al_set(self, dir_path, al_name):
        self.target_dir_path[al_name] = dir_path
        self.dict_al[al_name] = self._read_data_from_set_(dir_path)
        self.list_al_name = list(self.dict_al)

    def get_dict_error(self):
        for al_name in self.dict_al.keys():
            self._cal_error_per_al_(al_name)

    def _set_dict_error(self, al_name):
        self.dict_error[al_name] = []
        for item in self.ticks:
            self.dict_al[al_name].append(self.dict_al[al_name][item])

    def _cal_error_per_al_(self, al_name):
        self.dict_error[al_name] = []
        for item in self.ticks:
            self.dict_error[al_name].append(np.sqrt(np.sum(np.square(self.dict_al[al_name][item] - self.np_gt), axis=1)).tolist())

    def _read_data_from_gt_(self, input_path):
        self.np_gt = np.loadtxt(input_path, delimiter=',')[-4800:,-2:]


    def _read_data_from_set_(self, input_path):
        tmp_dict = collections.OrderedDict()
        file_list = os.listdir(input_path)
        for file_name in file_list:
            file_path = os.path.join(input_path, file_name)
            if os.path.isdir(file_path):
                continue
            item_name = os.path.split(file_name)[1].split('.')[0].split('_')[-1]
            tmp_dict[item_name] = np.loadtxt(file_path, delimiter=',')[-4800:,:]
        self.ticks = list(sorted(tmp_dict.keys()))
        return tmp_dict

    def _set_box_color_(self, bp, color):
        self.plt.setp(bp['boxes'], color=color)
        self.plt.setp(bp['whiskers'], color=color)
        self.plt.setp(bp['caps'], color=color)
        self.plt.setp(bp['medians'], color=color)
        self.plt.setp(bp['fliers'], markeredgecolor=color)

    def do(self):
        self.plt.figure()

        offset = 1
        scale = 3
        n = (len(self.list_al_name)-1.0) / 2. * 0.7
        interval = np.arange(-n, n + 0.7, 0.7)
        width = 0.6
        dict_bp = {}

class DataPlotModule:
    def __init__(self):
        self.plt = plt
        self.legend_title = '# of Sensors'
        self.y_axis_name = 'RMSE(cm)'
        self.x_axis_name = 'Sequence length'
        self.list_sequense_length = ['2', '3', '5', '8', '12']
        self.list_beacon_num = ['3', '5', '8']

        self.list_plt = []

    def set_data(self, np_data):
        '''
        :param np_data: raw = seq_len, column = beacon_num
        :return:
        '''
        self.np_data = np_data

    def plot_data(self, np_data):
        self.set_data(np_data)
        self._make_plot_()
        self.plt.show()

    def _make_plot_(self):
        self.plt.figure()
        for idx in range(len(self.list_beacon_num)):
            self.list_plt.extend(self.plt.plot(self.list_sequense_length, self.np_data[idx], label=self.list_beacon_num[idx]))
        self._set_plot_option_()

    def _set_plot_option_(self):
        self.plt.legend(handles=self.list_plt, title=self.legend_title, loc=1)
        self.plt.xlabel(self.x_axis_name, fontsize=15)
        self.plt.ylabel(self.y_axis_name, fontsize=15)

def set_box_color_(plt, bp, color):
        plt.setp(bp['boxes'], color=color)
        plt.setp(bp['whiskers'], color=color)
        plt.setp(bp['caps'], color=color)
        plt.setp(bp['medians'], color=color)
        plt.setp(bp['fliers'], markeredgecolor=color)
        return plt
if __name__ == '__main__':
    legends = ["Liao", "Ma", "Ours"]
    csv_names = ["0_33.csv", "0_66.csv", "1.csv"]
    fig1, ax1 = plt.subplots()
    from matplotlib.ticker import FormatStrFormatter
    ax1.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    gradient = 0.1
    width = 0.08
    scale = 0.3
    import pandas as pd
    for j, legend in enumerate(legends):
        rmses = []
        for i, csv_name in enumerate(csv_names):
            reader = pd.read_csv(os.path.join(legend, csv_name))
            rmse = list(reader["rmse"])
            rmses.append(rmse)
    # dict_rmse = {"1":rmse, "2":rmse, "3":rmse}
        positions = np.array([0.33, 0.66, 1])
        bp = ax1.boxplot(rmses, positions=positions + (j - 1) * gradient, sym='+', widths=width)
        plt.setp(bp['boxes'], color=COLORSET[j])
        plt.setp(bp['whiskers'], color=COLORSET[j])
        plt.setp(bp['caps'], color=COLORSET[j])
        plt.setp(bp['medians'], color=COLORSET[j])
        plt.setp(bp['fliers'], markeredgecolor=COLORSET[j])
        plt.plot([], c=COLORSET[j], label=legends[0])
    plt.legend()
    plt.xlabel("Ratio of sparsity", fontsize=16)
    plt.ylabel("RMSE [m]", fontsize=16)
    plt.xticks([0.33, 0.66, 1.0], [0.33, 0.66, 1.0])
    plt.xlim(0.1, 1.3)
    plt.ylim(0, 15)
    plt.tight_layout()
    fig = plt.gcf()
    plt.show()
    fig.savefig("box_compare2.png")


    # self.plt.legend()
    # self.plt.xlabel("Number of the anchors", fontsize=16)
    # self.plt.ylabel("Error [m]", fontsize=16)
    # self.plt.xticks(range(offset, scale*len(ticks), scale), self.ticks)
    # self.plt.xlim(-scale/2, scale*len(self.ticks))
    # self.plt.ylim(0, 0.3)
    # self.plt.tight_layout()
    # self.plt.savefig('boxcompare.png')
    # self.plt.show()

    # dpm = DataPlotModule()
    # dpm.plot_data([[3, 4, 1, 5, 9],[2, 3, 1, 6, 10],[0, 2, 5, 4, 1]])

