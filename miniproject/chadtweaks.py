#!/usr/bin/env python3

#raw dataset from Project FeederWatch, containing bird count observations during the 2020-2021 survey
#dataset available at https://clo-pfw-prod.s3.us-west-2.amazonaws.com/data/PFW_2021_public.csv
#data courtesy of the Cornell Lab of Ornithology, Birds Canada, and thousands of volunteer participants

import pandas as pd                                                 #import pandas library
import matplotlib                                                   #import matplotlib library
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pprint

def main():

    print("\nBird count of North America, 2020-2021\n")      #display title of this project

    #read file and transform into dataframe
    bird_df = pd.read_csv("PFW_2021_public.csv", usecols = ['obs_id','species_code','how_many'])
    #bird_df.rename(columns = {'species_code':'Name', 'how_many':'Count'}, inplace = True)
    print(bird_df, "\n")

    #group by 'Name' (species_code)
    grp_data = bird_df.groupby(['species_code']).size()
    print(grp_data, "\n")

    #create dictionary of (n=12) select species_code and common names
    b_dict = {
    "annhum":  {"name":"Anna's Hummingbird", "count":""},
    "balori":  {"name":"Baltimore Oriole", "count":""},
    "daejun":  {"name":"Dark-eyed Junco","count":""},
    "belkin1": {"name":"Belted Kingfisher", "count":""},
    "grbher3": {"name":"Great Blue Heron","count":""},
    "stejay":  {"name":"Steller's Jay", "count":""},
    "baleag":  {"name":"Bald Eagle","count":""},
    "grhowl":  {"name":"Great Horned Owl","count":""},
    "snoowl1": {"name":"Snowy Owl", "count":""},
    "amegfi":  {"name":"American Goldfinch","count":""},
    "norcar1": {"name":"Northern Cardinal", "count":""},
    "westan":  {"name":"Western Tanager", "count":""}}

    #b_list = ["annhum","balori","daejun","belkin1","grbher3","stejay","baleag","grhowl", "snoowl1", "amegfi", "norcar1", "westan"]

    #dict_2 = {
    #        'Name':["annhum", "balori","daejun","belkin1","grbher3","stejay","baleag","grhowl", "snoowl1", "amegfi", "norcar1", "westan"]}

    ### above script works

    print('----------  ----------\n')

    for bird in b_dict:
        spec_count = bird_df.groupby('species_code')['obs_id'].count()[bird]
        print(bird, "    ", spec_count)
        b_dict[bird]["count"] = spec_count
              #annhum

    pprint.pprint(b_dict)
    ### above script works

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

    
    #plot group by 'Name' (species_code)
    #grp_data.plot(kind='bar')
    #plt.savefig('/home/student/static/birdplot.png', bbox_inches = 'tight')
    #script works above; however, plot is cluttered and difficult to read"""


if __name__ == "__main__":
    main()
