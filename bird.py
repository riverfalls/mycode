#!/usr/bin/env python3

""" Project FeederWatch raw dataset, containing bird count observations during the 2020-2021 survey
dataset available at https://clo-pfw-prod.s3.us-west-2.amazonaws.com/data/PFW_2021_public.csv
dataset courtesy of Cornell Lab of Ornithology, Birds Canada, and thousands of volunteer participants """

import pandas as pd                                                 #import pandas library
import matplotlib                                                   #import matplotlib library
matplotlib.use('Agg')
import matplotlib.pyplot as plt                                     #import pyplot sub-library
import pprint                                                       #import pprint library

def main():

    print('\nBird Count of North America, 2020 - 2021')             #display title of this project
    print('------------------------------------------------------------------')
    print('Figure 1. Reading dataset observations (n=2,897,105 x 22 columns).\n')

    #read file and transform into dataframe
    bird_df = pd.read_csv('PFW_2021_public.csv', usecols = ['subnational1_code','obs_id','species_code','how_many'])
    bird_df.rename(columns = {'subnational1_code':'location','obs_id':'obs_id','species_code':'sp_code','how_many':'count'}, inplace = True)
    print(bird_df, '\n')

    print('------------------------------------------------------------------')
    print('Figure 2. Grouping observations by species code (n=563).\n')

    #group by species_code
    grp_data = bird_df.groupby(['sp_code']).size()
    print(grp_data, end = ' ')

    input('\n')  
    print('------------------------------------------------------------------') 
    print('Figure 3. Filtering and sorting selected species (n=18).\n')

    #create dictionary of (n=18) select species_code and common names
    b_dict = {
    "annhum":  {"name":"Anna's Hummingbird", "count":""},
    "balori":  {"name":"Baltimore Oriole", "count":""},
    "belkin1": {"name":"Belted Kingfisher", "count":""},
    "grbher3": {"name":"Great Blue Heron", "count":""},
    "stejay":  {"name":"Steller's Jay", "count":""},
    "baleag":  {"name":"Bald Eagle", "count":""},
    "grhowl":  {"name":"Great Horned Owl", "count":""},
    "snoowl1": {"name":"Snowy Owl", "count":""},
    "norcar1": {"name":"Northern Cardinal", "count":""},
    "westan":  {"name":"Western Tanager", "count":""},
    "pilwoo":  {"name":"Pileated Woodpecker","count":""},
    "mallar3": {"name":"Northern Mallard", "count":""},
    "coohaw":  {"name":"Cooper's Hawk", "count":""},
    "perfal":  {"name":"Peregrine Falcon", "count":""},
    "merlin":  {"name":"Merlin", "count":""},
    "calqua":  {"name":"California Quail", "count":""},
    "bkhgro":  {"name":"Black-headed Grosbeak", "count":""},
    "greroa":  {"name":"Greater Roadrunner", "count":""}}    

    #populate dictionary "count" for each species code
    for bird in b_dict:
        spec_count = bird_df.groupby('sp_code')['obs_id'].count()[bird]
        b_dict[bird]["count"] = spec_count

    #create dataframe for plotting and sort from smallest to largest count size
    newb_df = pd.DataFrame.from_dict(b_dict, orient = 'index')          #
    newb_df_sort = newb_df.sort_values('count')                         #
    print(newb_df_sort)

    #plot bar graph and save as .png to specified directory 
    newb_df_sort.plot(x='name', y='count', kind='bar')
    plt.savefig('/home/student/static/birdplot.png', bbox_inches = 'tight')

    print('\n>  Chart printed to /home/student/static', end='')
    input('\n') 

    #search location data for any species_code in custom dictionary above
    count = 0
    count_fig = 4
    while count < 3:
        count = count + 1
        print('------------------------------------------------------------------')
        n = input('Enter species code to show locations:  ')
        print(' ')
        for x in b_dict:
            if x == n:
                print(f'Figure {count_fig}. Observed locations of ', end='') 
                print(b_dict[x]['name'], end='') 
                print('.\n')
                options = [n]
                result_df = bird_df[bird_df['sp_code'].isin(options)]
                result_locate = result_df.groupby(['location']).size()
                print(result_locate, '\n')
                count_fig = count_fig + 1
                
                ## displays mean, min, max 
                result_stat = result_df.groupby(['location']).agg({'count': ['mean','min','max']})
                print(result_stat)

    input('\n') 

    ## search for unique observation identifier based on species code and count size 
    print('------------------------------------------------------------------')
    print('Search for location and unique observation identifier.\n')

    set_1 = 0
    while set_1 < 2:
        set_1 = set_1 + 1
        p = input('Enter species code:  ')
        q = input('Enter count size:    ')
        print(' ')
        for y in b_dict:
            if y == p:
                print('>  Location and unique observation identifier (obs_id) for species')
                print('  ', b_dict[y]['name'], end=' ')
                print(f'({p}) with count size {q}:\n')
                q_1 =int(q)
                result2_df = bird_df[bird_df['sp_code'].str.contains(p)]
                result3_df = result2_df.loc[result2_df['count'] == q_1]
                print(result3_df, '\n'*2)

    print('>  Thank you for visiting today. We hope to see you again soon.\n')

if __name__ == "__main__":
    main()
