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

    print("\nBird Count of North America, 2020-2021")               #display title of this project
##    input("\n")  
    print('------------------------------------------------------------------')
    print("Figure 1. Reading dataset observations (n=2,897,105 x 22 columns).\n")

    #read file and transform into dataframe
    bird_df = pd.read_csv("PFW_2021_public.csv", usecols = ['subnational1_code','obs_id','species_code','how_many'])
    bird_df.rename(columns = {'subnational1_code':'location','obs_id':'obs_id','species_code':'sp_code','how_many':'count'}, inplace = True)
    print(bird_df, "\n")

    print('------------------------------------------------------------------')
    print('Figure 2. Grouping observations by species code (n=563).\n')

    #group by species_code
    grp_data = bird_df.groupby(['sp_code']).size()
    print(grp_data, end = " ")

##    input("\n")   ## when active, remove \n on next two lines 
    print('\n')
    print('\n------------------------------------------------------------------') 
    print('Figure 3. Filtering and sorting selected species (n=18).\n')

    #create dictionary of (n=12) select species_code and common names
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

    ## above script works

    for bird in b_dict:
        spec_count = bird_df.groupby('sp_code')['obs_id'].count()[bird]
        b_dict[bird]["count"] = spec_count

##  pprint.pprint(b_dict)
    ### above script works; "for loop" is populating b_dict for subsequent use

#   ------------------------------------------------------

##    print('b_dict=', type(b_dict))
##    print('spec_count=', type(spec_count))

#    for bird2 in b_dict:                   #pulls out common names
#        values = b_dict[bird2]["name"]
#        print(values)
#    print('values=', type(values))         #prints common names, one per line

#   better output display
    newb_df = pd.DataFrame.from_dict(b_dict, orient = 'index')          #
    newb_df_sort = newb_df.sort_values('count')                         #
    print(newb_df_sort)

    print('\ntype =', end = ' ')
    print(type(newb_df_sort))

##  following works but... #plot group by sp_code (species_code)
    newb_df_sort.plot(kind='bar')
    plt.savefig('/home/student/static/birdplot.png', bbox_inches = 'tight')

    print('\n>  Chart printed to /home/student/static')

#   search for western tanagers
##    input("\n")   ## when active, remove \n on next line 
    print('\n------------------------------------------------------------------')
    print('Figure 4. Observed locations of Western Tanagers.\n')

    options = ['westan']
    result_df = bird_df[bird_df['sp_code'].isin(options)]
    result_locate = result_df.groupby(['location']).size()
    print(result_locate, '\n')

if __name__ == "__main__":
    main()
