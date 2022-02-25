#!/usr/bin/env python3

#Cheddar cheese consumption in pounds per person by year
#data courtesy of https://github.com/rfordatascience/tidytuesday/blob/master/data/2019/2019-01-29/clean_cheese.csv
#scripting goes better with beer 


def main():

    import csv

    #title of this mini-project
    print("\nCheddar cheese consumption in the U.S., 1970 - 2017\n")

    #headers for output columns to be displayed
    print("Year   lbs per person")
    print("----   --------------")

    # open the .csv file for reading
    with open("clean_cheese.csv", "r") as cheesedata:

        # loop over the file line-by-line
        for eachline in csv.DictReader(cheesedata):
            #decided to comment out next line to declutter the displayed output seen in the  latest version
            #print(f'In {eachline["Year"]}, Cheddar cheese consumption in the U.S. was {eachline["Cheddar"]} pounds per person.') 
            
            print(f'{eachline["Year"]}   {eachline["Cheddar"]}')

main()
