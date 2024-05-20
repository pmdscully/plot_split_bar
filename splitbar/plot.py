import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle
import matplotlib.font_manager as font_manager
from matplotlib.font_manager import findfont, FontProperties

# font_dir = ['c:/users/_user_/AppData/Local/Microsoft/Windows/Fonts/']
# if any([os.path.exists(fn) for fn in font_dir]):
#     for font in font_manager.findSystemFonts(font_dir):
#         font_manager.fontManager.addfont(font)    
# matplotlib.rcParams['font.family'] = 'sans-serif'
# font = findfont(FontProperties(family=['arial']))
# matplotlib.rcParams['font.sans-serif'] = 'arial'


def plot_split_bar(data:np.array, rows:list, columns:list, 
                   colors=[(0.6431, 0.9412, 1.0),
                         (0.0, 0.6392, 0.6902),
                         (0.0, 0.349, 0.3765),
                         (0.2039, 0.749, 0.8118),
                         (0.0, 0.4392, 0.4745),
                         (0.3686, 0.8549, 0.9255),
                         (0.0, 0.5373, 0.5804)], 
                   precision=2, fig_size=None,
                   lower_caption='',
                   default_font='sans-serif',
                   fn_suffix='', WRITE=True):
    """
    Plot a split-bar plot with given data and categories.

    Usage:
    ```
        cols = 3
        data = pd.DataFrame( np.random.rand(5,cols), columns=[chr(65+i) for i in range(cols)]).iloc[::-1]
        plot_split_bar(data=data.to_numpy(), 
                       rows=data.index.tolist(), 
                       columns=data.columns, 
                       colors=colors_r,
                       precision=2,
                       fn_suffix='Relative',
                       fig_size=(5, 1),
                       WRITE=False
                      )
    ```
    """
    numrows = data.shape[0]
    numcols = data.shape[1]
    data_max = np.max(data)*1.025
    fig, ax = plt.subplots()
    if fig_size:
        fig.set_size_inches(fig_size)
    # Set labels and ticks
    ax.set_xticks(np.arange(len(columns))-0.14)
    ax.set_xticklabels(columns, fontsize=8, fontname=default_font, ha='left', va='bottom', y=1.01, weight='bold')
    ax.xaxis.tick_top()
    ax.xaxis.set_ticks_position('none')
    # ax.yaxis.set_major_locator(plt.NullLocator())
    # ax.yaxis.set_ticks_position('none')
    # ax.set_yticks([])
    # plt.tick_params(left = False)
    ax.set_yticks(np.arange(len(rows))+0.26)
    ax.set_yticklabels(rows, fontsize=7, fontname=default_font, x=-0.025, ha='right')
    ax.spines[['right', 'left']].set_visible(False)

    # Add text annotation
    for i in range(len(data)):
        for j in range(len(data[i])):
            perc = data[i][j]/data_max
            ax.add_patch(Rectangle((j-.29, i-.25), perc, 0.95,
                                     facecolor = colors[j],
                                     alpha=1,
                                     fill=True,
                                  ))
            ax.add_patch(Rectangle((perc+0.01+(j-.29), i-.25), 0.99-perc, 0.95,
                                     facecolor = '#eee',
                                     alpha=0.6,
                                     fill=True,
                                  ))
            text_pos = (j-0.26)+perc if perc < 0.5 else (j-(0.26)+.1)
            text_col = '#333' if perc < 0.5 else 'white'
            text_col = '#333' if text_col=='white' and np.mean(colors[j])>0.5 else text_col
            text_bold = None if perc < 0.5 else 'bold'
            text_perc = f'{data[i][j]:,.{precision}f}' if f'{data[i][j]:,.1f}'[-2:]!='.0' else f'{data[i][j]:,.0f}'
            ax.text(text_pos, i+.15, text_perc, ha='left', va='center', 
                    fontname=default_font, color=text_col, fontsize=7, weight=text_bold)
    ax.grid(False)
    ax.set_ylim(0-0.5, numrows)
    ax.set_xlim(0-0.5, numcols)

    for j in range(len(columns)):
        ax.add_patch(Rectangle((j-0.31, len(data)+1.15), 0.15, .7,
                                 facecolor = colors[j],
                                 clip_on=False,
                                 alpha=1,
                                 fill=True,
                              ))
    if lower_caption:
        ax.text(numcols, -1.15, lower_caption, ha='right', va='center', 
                    fontname=default_font, color='#333', fontsize=7)
    if WRITE:
        plt.tight_layout()
        fig.savefig(f'Split-bar_{fn_suffix}.png',dpi=150)
    plt.show()
