import matplotlib.pyplot as plt
import numpy as np


def my_dot_plot(ax, the_data, title=''):
    y_labels = []
    x_axis_max = 0

    dot_colors = ['#1f77b4',
                  '#d0d0d0',
                  '#50A6C2',
                  '#B2DFEE',
                  '#63D1F4',
                  ]

    ax.set_title(title)

    for k, v in the_data.items():
        y_labels.append([sum(v), k])
        if x_axis_max < sum(v):
            x_axis_max = sum(v)
        for i in range(len(v)):
            if i > 0:
                v[i] += v[i-1]
        the_data[k] = v
    char_width = x_axis_max/74
    line_lengths, y_labels = zip(*sorted(y_labels))
    x_spacing = [0,
                 x_axis_max*1.25*.2,
                 x_axis_max*1.25*.4,
                 x_axis_max*1.25*.6,
                 x_axis_max*1.25*.8,
                 ]
    y_spacing = np.arange(len(y_labels))

    ax.set_xlim(-(char_width / 2), x_axis_max+(2*char_width))
    ax.set_xticks(x_spacing)
    ax.xaxis.grid(color='#d0d0d0')
    plt.yticks(y_spacing, y_labels)
    ax.tick_params(axis='x', bottom="off")
    ax.tick_params(axis='y', left='off')
    ax.barh(y_spacing, line_lengths, height=0.025)

    for y_label, y_coord in zip(y_labels, y_spacing):
        for i, x_coord in enumerate(the_data.get(y_label)):
            plt.plot(x_coord, y_coord, color=dot_colors[i], marker='o')

    return ax


def my_hbar_plot(ax, the_data, title=''):
    y_labels = []
    x_axis_max = 0

    ax.set_title(title)
    ax.get_xaxis().set_visible(False)

    for k, v in the_data.items():
        y_labels.append([sum(v), k])
        if x_axis_max < sum(v):
            x_axis_max = sum(v)
    char_width = x_axis_max/74
    char_height = len(y_labels)*0.0014
    bar_lengths, y_labels = zip(*sorted(y_labels))
    y_spacing = np.arange(len(y_labels))

    plt.yticks(y_spacing, y_labels)
    ax.tick_params(axis='y', left='off')
    ax.barh(y_spacing, bar_lengths, .5)

    for i, bar_length in enumerate(bar_lengths):
        qty = str(bar_length)
        if bar_length < ((len(str(bar_length)) + 2) * char_width):
            x_offset = bar_length + char_width
            color_hex = '#1f77b4'
        else:
            x_offset = bar_length - ((len(str(bar_length)) + 1) * char_width)
            color_hex = '#ffffff'
        y_offset = i - (char_height * 10)
        ax.text(x=x_offset, y=y_offset, s=qty, color=color_hex, weight='bold')

    return ax


def my_bar_plot(ax, the_data, title=''):
    x_labels = []
    y_axis_max = 0

    ax.set_title(title)
    ax.get_yaxis().set_visible(False)

    for k, v in the_data.items():
        x_labels.append([sum(v), k])
        if y_axis_max < sum(v):
            y_axis_max = sum(v)
    char_height = y_axis_max/13.33
    bar_heights, x_labels = zip(*sorted(x_labels, reverse=True))
    x_spacing = np.arange(len(x_labels))

    plt.xticks(x_spacing, x_labels, rotation=45)
    ax.tick_params(axis='x', bottom="off")
    ax.tick_params(axis='y', left='off')
    ax.bar(x_spacing, bar_heights, width=0.5, align='center')

    for i, bar_height in enumerate(bar_heights):
        if bar_height > y_axis_max:
            y_axis_max = bar_height
        qty = str(bar_height)
        if bar_height < char_height:
            y_offset = bar_height + (char_height / 6)
            color_hex = '#1f77b4'
        else:
            y_offset = bar_height - (char_height / 2)
            color_hex = '#ffffff'
        x_offset = i - (len(qty) * 0.03)
        ax.text(x=x_offset, y=y_offset, s=qty, color=color_hex, weight='bold')

    return ax
