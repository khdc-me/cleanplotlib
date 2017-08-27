# cleanplotlib
Python package to easily create clean matplotlib charts/graphs. You gather, analyze, and organize the data. cleanplotlib transforms it into a pretty plot.  
  
## Available plot types  
### Dot Plot
A dot plot is ideal in the following three scenarios:  
1) As an alternative to pie charts. Tufte sided against the use of pie charts. Unless the size of each segment/slice is noticeably different than the rest, a pie chart can be difficult to read. Pie chart creators may include labels that display the values, making them easier to interpret. But when a specific segment is too small to house the label, the label must be displayed outside of the graphic, with a line drawn to link it to its corresponding segment. This is ugly and add unnecessary junk to the visual. Here is a side-by-side comparison of a pie chart (code [here](https://matplotlib.org/examples/pie_and_polar_charts/pie_demo_features.html)) and a dot plot:
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
* If more than one value is passed for any given category, a dot will be placed at the first value and at the sum of each of the following values. So if it receives:  
`categories = {'A': [10, 20, 19, 10]}`  
dots will be placed at: (A, 10), (A, 30), (A, 49), and (A, 59)  
A different shade of blue will be used for the dots (up to five dots)  
* my_dot_plot uses the highest value in given data to determine the max value for the x-axis. It then evenly disects the chart into four equal segments via evenly spaced vertical grid lines.  
  
### Horizontal Bar Chart  
A horizontal bar chart can completely substitute a regular (vertical) bar chart in any visualization, especially when:  
1. there are many (more than 5) items/categories  
1. at least 1 item/category label is longer than a bar chart’s x-axis can accommodate
