# How to create a Split-Bar plot with `matplotlib`:


## Requirements:
- numpy
- matplotlib

## Installation:
(Use `!pip` for notebook installations, Jupyter, Colab, etc.)
```
pip install git+https://github.com/pmdscully/plot_split_bar.git
```

Open an [Example notebook in Google-Colab](https://colab.research.google.com/drive/1p7v7e3AY6kCOEhR2mNhFp7lEvt2cAj--?usp=sharing)

## Example 1: Usage with Global CO2 emissions from fossil-fuel data:
[Source of dataset](https://ourworldindata.org/grapher/co2-emissions-by-fuel-line)
```python
from splitbar import plot_split_bar
import pandas as pd
import numpy as np

df = pd.read_csv('https://github.com/owid/co2-data/raw/master/owid-co2-data.csv')
columns1 = ['year','oil_co2','coal_co2','gas_co2','other_industry_co2','cement_co2','flaring_co2','trade_co2',]
data = df[(df['country']=='World') & (df['year']>=2005)][columns1].set_index('year').iloc[::-1]

plot_split_bar(data=data.to_numpy(), 
               rows=data.index, 
               columns=[c.replace('_',' ').title().replace('Co2','\nCO2') for c in data.columns], 
               precision=1,
               fn_suffix='world_co2',
               lower_caption='Data on CO2 and Greenhouse Gas Emissions by Our World in Data. World data 2005 to 2022.',
               fig_size=(7, 3),
               WRITE=True
              )
```
##### Output:
<img src="https://github.com/pmdscully/plot_split_bar/assets/3637403/9741990d-410c-44fb-82ab-825ec6806402" width="750">

## Example 2: Usage with Pseudorandom generated data:
```python
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
               precision=2,
               fn_suffix='',
               lower_caption='This plot contains randomly generated data.',
               fig_size=(7, 5),
               WRITE=False
              )
```

##### Output:
<img src="https://github.com/pmdscully/plot_split_bar/assets/3637403/3c62c6c3-7a27-4441-aa2c-5cefc1cc6614" width="750">
