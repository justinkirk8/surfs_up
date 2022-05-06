# surfs_up
## Overview of Analysis:
Client requested an analysis of the weather given the provided dataset Hawaii.sqlite. Specifically, an analysis of summary statistics of temperature and precipitation for given months of the year.

## Resources
- Software: pgAdmin4, PostgreSQL 14, Python 3.10 (64-bit), Jupyter Notebook 6.4.8


## Results
Key differences between temperatures in the months of June and December:
- The mean temperature drops by three degrees when going from June to December while the standard deviation also increased in December. This indicate that while the average temperature will stay about the same, that there will be much more variation in temperature in December. 
- The minimum temperature drops the most out of any other metric. When compared to the Q1 (25%) which represents a less significant drop, we can see that a few cold days are causing the majority of the change in variation and average.
- The maximum temperature drops the least when going from June to December which indicates that, while there is a much bigger spread of temperatures, warm days on the beach can still be possible in December. 

<p align="center">
  <img src="https://github.com/justinkirk8/surfs_up/blob/main/images/June_temps.png" width="240" /><space>
  <img src="https://github.com/justinkirk8/surfs_up/blob/main/images/Dec_temps.png" width="300" /> 
</p>

## Summary
When comparing the months of June and December, there is a noticeable change in temperature and precipitation. The average temperature decreases, the average precipitation increases, and both metrics become more variable in the month of December. That being said. The averages them selves do not change drastically. Looking further into the data it can also be seen that the majority o the change in variability is due to a few readings that are potential outliers. In temperature we can see that the first quartile (25%) only drops 4 degrees while the minimum drops a whole 8 degrees. Similarly in precipitation, we can see that in Q3 (75%) we only see a 0.03 inch increase while the maximum sees approximately a 2 inch increase in precipitation. Because of this, I think the client can be fairly confident that they will be able to see consistent business throughout the year despite some rainy or cold days in the winter months. 

<p align="center">
  <img src="https://github.com/justinkirk8/surfs_up/blob/main/images/June_perc.png" width="260" /><space>
  <img src="https://github.com/justinkirk8/surfs_up/blob/main/images/Dec_perc.png" width="300" /> 
</p>

