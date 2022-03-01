#!/usr/bin/env python3

#raw dataset from Project FeederWatch, containing bird count observations during the 2020-2021 survey
#dataset available at https://clo-pfw-prod.s3.us-west-2.amazonaws.com/data/PFW_2021_public.csv
#data courtesy of the Cornell Lab of Ornithology, Birds Canada, and thousands of volunteer participants

import pandas as pd                                                 #import pandas library
import matplotlib                                                   #import matplotlib library
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pprint                                                       #import pprint library

def main():

    print("\nBird count of North America, 2020-2021\n")             #display title of this project

    #read file and transform into dataframe
    bird_df = pd.read_csv("/home/student/PFW_2021_public.csv", usecols = ['obs_id','species_code','how_many'])
    bird_df.rename(columns = {'obs_id':'obs_id','species_code':'sp_code','how_many':'count'}, inplace = True)
    print(bird_df, "\n")

    print('----------------------------------------')

    #group by species_code
    grp_data = bird_df.groupby(['sp_code']).size()
    print(grp_data, "\n")

    print('----------------------------------------')

    input("\n")

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
    "merlin":  {"name":"Merlin", "count":""}}

    ### above script works

    for bird in b_dict:
        spec_count = bird_df.groupby('sp_code')['obs_id'].count()[bird]
#        print(bird, "    ", spec_count)                                #this line works
#        print(b_dict[bird]["name"], "    ", spec_count)                #this line works
#        print(bird, "   ", b_dict[bird]["name"], "     ", spec_count)  #superseded by new_df section below
        b_dict[bird]["count"] = spec_count

#    pprint.pprint(b_dict)
     ### above script works; "for loop" is populating b_dict for subsequent use

#   ------------------------------------------------------

#    print('b_dict=', type(b_dict))
#    print('spec_count=', type(spec_count))

#    for bird2 in b_dict:                   #pulls out common names
#        values = b_dict[bird2]["name"]
#        print(values)
#    print('values=', type(values))         #prints common names, one per line

### better output display
    newb_df = pd.DataFrame.from_dict(b_dict, orient = 'index')          #supersedes lines-47, 48, 54
    print(newb_df)

    #following error: "AttributeError: 'numpy.int64' object has no attribute 'plot'"
    #spec_count.plot(kind='bar')
    #plt.savefig('/home/student/static/birdplot_2.png', bbox_inches = 'tight')

    #following works but is not desired outcome
    #filter_1 = bird_df.loc[bird_df['species_code'] == b_list[11]]
    #print(filter_1)

    #following works but is not desired outcome
    #filter_2 = bird_df.isin(b_list)  
    #filter_2p = filter_2.groupby(['species_code']).size()
    #print(b_list, filter_2p, "\n")
    
    #plot group by sp_code (species_code)
    newb_df.plot(kind='bar')
    plt.savefig('/home/student/static/birdplot.png', bbox_inches = 'tight')

    print('\n>  Chart printed to /home/student/static\n')

if __name__ == "__main__":
    main()
