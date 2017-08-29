# cleanplotlib
Python package to easily create clean matplotlib charts/graphs. You gather, analyze, and organize the data. cleanplotlib transforms it into a pretty plot.  
  
The goal is to assist those who lack design skills and do not have a budget for advanced visualization tools or for hiring a visualization expert. While it is essential that everyone posseses a basic understanding of the fundamentals of visualization, not everyone should have to become a designer.  
  
cleanplotlib aims to alleviate the need to have to become an expert in design, visualization, and matplotlib. Please report any issues, recommend additional features, or suggest chart types that should be included.  
  
## Install  
1. Download by clicking green "Clone or download" button, or clone from console  
```git clone https://github.com/khdc-me/cleanplotlib```  
1. Install  
```pip install cleanplotlib```  
  
## Required  
* Python 3+
* matplotlib
* NumPy
  
## Available plot types  
### Dot Plot  
A dot plot is ideal in the following three scenarios:  
1) As an alternative to pie charts. Tufte sided against the use of pie charts. Unless the size of each segment/slice is noticeably different than the rest, a pie chart can be difficult to read. Pie chart creators may include labels that display the values, making them easier to interpret. But when a specific segment is too small to house the label, the label must be displayed outside of the graphic, with a line drawn to link it to its corresponding segment. This is ugly and add unnecessary junk to the visual. Here is a side-by-side comparison of a pie chart (code [here](https://matplotlib.org/examples/pie_and_polar_charts/pie_demo_features.html)) and the default cleanplotlib dot plot:
![Pie Chart vs Dot Plot](https://github.com/khdc-me/cleanplotlib/blob/master/pievsdot.png)  
  
2) As an alternative to vertical and horizontal bar charts. A dot plot is a simple and clean visualization method when the intention is to compare sizes/amounts but not necessarily exact values.  
  
3) Multiple values for each item/category.
Ex: Sales information for ten articles of clothing and you need to display totals for everyone under 18yrs of age, and everyone who is 18+.
Ex: You have want to display the total sales for the year, for ten articles of clothing, and want to include mid-year totals.  
  
#### Minimum required code  
**my_dot_plot** is currently optimized for a 10"x5" figure. The minimum required code to display a dot plot is:  

    import matplotlib.pyplot as plt
    from matplotlib.pyplot import subplots_adjust
    import cleanplotlib as cpl


    def main():
        categories = {'Category 1': [25],
                      'Category 2': [32],
                      'Category 3': [34],
                      'Category 4': [20],
                      'Category 5': [25],
                      'Category 6': [33],
                      }
    
        fig1 = plt.figure(num=1,
                          figsize=(10, 5),
                          tight_layout=False,
                          facecolor='#fafafa',
                          edgecolor='#ff0000',
                          frameon=True,
                          )
    
        ax1 = plt.subplot2grid((1, 1), (0, 0), frameon=False)
        ax1 = cpl.my_dot_plot(ax1,
                              the_data=categories,
                              title="Totals per Category",
                              )
        fig1.add_subplot(ax1)

        subplots_adjust(right=1.0)
        plt.show()
        plt.close()
        print("closed")
    
    
    if __name__ == '__main__':
        main()
    
#### Notes  
* If more than one value is passed for any given category, a dot will be placed at the first value and at the sum of each of the following values. So if my_dot_plot receives:  
`categories = {'A': [10, 20, 19, 10]}`  
dots will be placed at: (A, 10), (A, 30), (A, 49), and (A, 59)  
A different shade of blue will be used for the dots (up to five dots)  
* my_dot_plot uses the highest value in given data to determine the max value for the x-axis. It then evenly disects the chart into four equal segments via evenly spaced vertical grid lines.  
* category names/lables should be shorter than 12 characters in length.
  
### Horizontal Bar Chart  
A horizontal bar chart can completely substitute a regular (vertical) bar chart in any visualization, especially when:  
1. there are many (more than 5) items/categories  
1. at least 1 item/category label is longer than a bar chart’s x-axis can accommodate  
  
Here is a side-by-side comparison of a standard matplotlib horizontal bar chart (code [here](https://matplotlib.org/devdocs/gallery/lines_bars_and_markers/barh.html) and the default cleanplotlib horizontal bar chart:  
![Comparing Horizontal Bar Charts](https://github.com/khdc-me/cleanplotlib/blob/master/hbarvhbar.png)  

#### Minimum Required Code  
**my_hbar_plot** is currently optimized for a 10"x5" figure. The minimum required code to display a horizontal bar graph is:
  
    import matplotlib.pyplot as plt
    from matplotlib.pyplot import subplots_adjust
    import cleanplotlib as cpl
    
    
    def main():
        test_categories = {'Tom': [10],
                           'Dick': [10.25],
                           'Harry': [10],
                           'Slim': [1, 7.5],
                           'Jim': [13],
                           }
    
        fig1 = plt.figure(num=1,
                          figsize=(10, 5),
                          tight_layout=False,
                          facecolor='#fafafa',
                          edgecolor='#ff0000',
                          frameon=True,
                          )
    
        ax1 = plt.subplot2grid((1, 1), (0, 0), frameon=False)
        ax1 = cpl.my_hbar_plot(ax=ax1,
                              the_data=test_categories,
                              title='Performance: How fast do you want to go today?',
                              )
        fig1.add_subplot(ax1)
    
        subplots_adjust(right=1.0)
        plt.show()
        plt.close()
        print("closed")
    
    
    if __name__ == '__main__':
        main()
    

#### Notes  
* If more than one value is passed for any given category, the values will be added together - displayed as a single bar of SUM length. So if my_hbar_plot receives:  
`categories = {'A': [10, 20, 19, 10]}`,  
it will display a bar for 'A' that is 59 units long.  
* Category names/lables should be shorter than 12 characters in length.  
* If the length of the bar is shorter than the length of the annotation, the annotation's color is inverted and it is placed outside (to the right of) the bar.
  
### Bar Chart (vertical/regular)  
Bar charts illustrate comparisons among categories. It is best suited for categories with short names that can be displayed on the x-axis without risk of overlap, and when there are only a handful (5 or less) categories.  
  
Here is a side-by-side comparison of a standard matplotlib bar chart (code [here](https://pythonspot.com/en/matplotlib-bar-chart/)) and the default cleanplotlib bar chart:  
![Compariong Bar Charts](https://github.com/khdc-me/cleanplotlib/blob/master/barvbar.png)  
  
#### Minimum Required Code  
**my_bar_plot** is currently optimized for a 10"x5" figure. The minimum required code to display a bar graph is:  
  
    import matplotlib.pyplot as plt
    from matplotlib.pyplot import subplots_adjust
    import cleanplotlib as cpl
    
    
    def main():
        tcs = {'Python': [10],
               'C++': [8],
               'Java': [3, 3],
               'Perl': [4],
               'Scala': [2],
               'Lisp': [1],
               }
    
        fig1 = plt.figure(num=1,
                          figsize=(10, 5),
                          tight_layout=False,
                          facecolor='#fafafa',
                          edgecolor='#ff0000',
                          frameon=True,
                          )
    
        ax1 = plt.subplot2grid((1, 1), (0, 0), frameon=False)
        ax1 = cpl.my_bar_plot(ax=ax1,
                             the_data=tcs,
                             title='Programming Language Usage',
                             )
        fig1.add_subplot(ax1)
    
        subplots_adjust(right=1.0)
        plt.show()
        plt.close()
        print("closed")
    
    
    if __name__ == '__main__':
        main()
    
#### Notes  
* If more than one value is passed for any given category, the values will be added together - displayed as a single bar of SUM height. So if my_bar_plot receives:
`categories = {'A': [10, 20, 19, 10]}`,
it will display a bar for 'A' that is 59 units high.  
* If the height of the bar is shorter than the height of the annotation, the annotation's color is inverted and it is placed outside (above) the bar.
