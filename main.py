# MIT License
#
# Copyright (c) [2024] [Sariya Ansari]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# 1. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# 2. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
This file validates the functionality of Visually package.
It allows to test various methods and combination of parameters to validate the functionality
"""

import pandas as pd
from visual.visually import Visually

if __name__ == '__main__':
    v = Visually()
    v.visualize(data='https://raw.githubusercontent.com/CourseMaterial/DataWrangling/main/flowerdataset.csv', url=True)

    visualizer = Visually('plotly')
    data = pd.read_csv("data/data.csv")  # Replace with your CSV path
    visualizer.visualize(data)

    visualizer = Visually()
    # For Seaborn
    visualizer.set_style('seaborn')
    visualizer.visualize('data/data.csv', visualization_type='scatter', class_variable='Target', filename='filesea')

    # For Plotly
    visualizer.set_style('plotly')
    visualizer.visualize(data='data/data.csv', visualization_type='heatmap', filename='heatmap')

