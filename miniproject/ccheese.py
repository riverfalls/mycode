#!/usr/bin/env python3

#Cheddar cheese consumption in pounds per person by year
#data courtesy of https://github.com/rfordatascience/tidytuesday/blob/master/data/2019/2019-01-29/clean_cheese.csv
#scripting goes better with beer 

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

def main():

    #title of this mini-project
    print("\nCheese consumption in the U.S. in pounds per year, 1970 to 2017\n")

    cheese_df = pd.read_csv("clean_cheese.csv", usecols = ['Year', 'Cheddar', 'Mozzarella', 'Swiss'])
    cheese_df.reset_index(drop=True)
    print(cheese_df)

    #plt.cheese_df.plot(x='Year', y=['Cheddar','Mozzarella','Swiss'], kind='bar')
    #plt.savefig.bbox('/home/student/static/ccheese.png')

if __name__ == "__main__":
    main()
