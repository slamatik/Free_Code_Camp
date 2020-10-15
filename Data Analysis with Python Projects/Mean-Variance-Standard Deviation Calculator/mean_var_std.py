import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    calculations = {'mean': [], 'variance': [], 'standard deviation': [], 'max': [], 'min': [], 'sum': []}

    data = np.asmatrix(list).reshape(3, 3)

    get_mean(data, list, calculations)
    get_var(data, list, calculations)
    get_std(data, list, calculations)
    get_max(data, list, calculations)
    get_min(data, list, calculations)
    get_sum(data, list, calculations)

    return calculations


def get_mean(data, flat, calcs):
    mean_ax1 = []
    mean_ax2 = []
    for i in range(len(data)):
        mean_ax1.append(np.mean(data[:, i]))
        mean_ax2.append(np.mean(data[i]))
    mean_flat = np.mean(flat)
    calcs['mean'].append(mean_ax1)
    calcs['mean'].append(mean_ax2)
    calcs['mean'].append(mean_flat)


def get_var(data, flat, calcs):
    var_ax1 = []
    var_ax2 = []
    for i in range(len(data)):
        var_ax1.append(np.var(data[:, i]))
        var_ax2.append(np.var(data[i]))
    mean_flat = np.var(flat)
    calcs['variance'].append(var_ax1)
    calcs['variance'].append(var_ax2)
    calcs['variance'].append(mean_flat)


def get_std(data, flat, calcs):
    std_ax1 = []
    std_ax2 = []
    for i in range(len(data)):
        std_ax1.append(np.std(data[:, i]))
        std_ax2.append(np.std(data[i]))
    mean_flat = np.std(flat)
    calcs['standard deviation'].append(std_ax1)
    calcs['standard deviation'].append(std_ax2)
    calcs['standard deviation'].append(mean_flat)


def get_max(data, flat, calcs):
    max_ax1 = []
    max_ax2 = []
    for i in range(len(data)):
        max_ax1.append(np.max(data[:, i]))
        max_ax2.append(np.max(data[i]))
    mean_flat = np.max(flat)
    calcs['max'].append(max_ax1)
    calcs['max'].append(max_ax2)
    calcs['max'].append(mean_flat)


def get_min(data, flat, calcs):
    min_ax1 = []
    min_ax2 = []
    for i in range(len(data)):
        min_ax1.append(np.min(data[:, i]))
        min_ax2.append(np.min(data[i]))
    mean_flat = np.min(flat)
    calcs['min'].append(min_ax1)
    calcs['min'].append(min_ax2)
    calcs['min'].append(mean_flat)


def get_sum(data, flat, calcs):
    sum_ax1 = []
    sum_ax2 = []
    for i in range(len(data)):
        sum_ax1.append(np.sum(data[:, i]))
        sum_ax2.append(np.sum(data[i]))
    mean_flat = np.sum(flat)
    calcs['sum'].append(sum_ax1)
    calcs['sum'].append(sum_ax2)
    calcs['sum'].append(mean_flat)