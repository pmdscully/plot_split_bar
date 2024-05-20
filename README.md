# How to create a Split-Bar plot with `matplotlib`:

<img src="https://github.com/pmdscully/plot_split_bar/assets/3637403/3c62c6c3-7a27-4441-aa2c-5cefc1cc6614" width="300">

## Requirements:
- shapely (via pip) <=2.0.1 or >2.0.1. (only requires `Polygon` class)
- geopandas (often requires install via conda)
- numpy
- matplotlib

## Installation:
(Use `!pip` for notebook installations, Jupyter, Colab, etc.)
```
pip install git+https://github.com/pmdscully/plot_split_bar.git
```

## Example 1: Usage with Pseudorandom generated data:
```
from splitbar import plot_split_bar

import pandas as pd
import numpy as np

rows = 20
cols = 7
data = pd.DataFrame( np.random.rand(rows,cols), 
                    columns=[chr(65+i) for i in range(cols)], 
                    index=[2005+(i) for i in range(rows)]).iloc[::-1]

plot_split_bar(data=data.to_numpy(), 
               rows=data.index, 
               columns=data.columns, 
               precision=3,
               fn_suffix='',
               lower_caption='This plot contains randomly generated data.',
               fig_size=(7, 5),
               WRITE=False
              )
```
