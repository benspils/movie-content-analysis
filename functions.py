

def bar_plot_success(groupby,label):
    
    import matplotlib.pyplot as plt
    import seaborn as sns
    #importing relevant libraries

    import os
    import pandas as pd 
    import numpy as np

    #Turn data folder into list of data file names

    data_path = os.path.join('data','zippedData')
    data_files = os.listdir(data_path)
    data_files.pop(data_files.index('.ipynb_checkpoints'))
    data_files.pop(data_files.index('Untitled.ipynb'))
    data_files = [os.path.join(data_path,file) for file in data_files]
    data_files

    #Turn all data files into pandas dataframes

    data = {}
    name_dict={'imdb.title.crew.csv.gz':"crew",
               'tmdb.movies.csv.gz':"movies",
               'imdb.title.akas.csv.gz':"akas",
               'imdb.title.ratings.csv.gz':"ratings",
               'imdb.name.basics.csv.gz':"name_basics",
               'rt.reviews.tsv.gz':"reviews",
               'imdb.title.basics.csv.gz':"title_basics",
               'rt.movie_info.tsv.gz':"movie_info",
               'tn.movie_budgets.csv.gz':"movie_budgets",
               'bom.movie_gross.csv.gz':"movie_gross",
               'imdb.title.principals.csv.gz':"principals"
              }
    for file in data_files:
        try:
            df = pd.read_csv(file)
        except:
            print(file)
            continue
        file_name = file.split('/')[-1]
        data[name_dict[file_name]] = df

    data["movie_info"]=pd.read_csv('data/zippedData/rt.movie_info.tsv.gz', sep="\t")
    data["reviews"]=pd.read_csv('data/zippedData/rt.reviews.tsv.gz', sep="\t", encoding="latin1")

    #Renaming columns to be able to merge on 'title' column

    data['title_basics'] = data['title_basics'].rename(columns={'primary_title':'title'})
    data['movie_budgets'] = data['movie_budgets'].rename(columns={'movie':'title'})

    #Getting rid of commas and dollar signs to make dataframe values easier to work with 

    data['movie_budgets']['worldwide_gross'] = data['movie_budgets']['worldwide_gross'].str.replace(',', '')
    data['movie_budgets']['worldwide_gross'] = data['movie_budgets']['worldwide_gross'].str.replace('$', '')
    data['movie_budgets']['worldwide_gross'] = data['movie_budgets']['worldwide_gross'].astype(int)

    data['movie_budgets']['production_budget'] = data['movie_budgets']['production_budget'].str.replace(',', '')
    data['movie_budgets']['production_budget'] = data['movie_budgets']['production_budget'].str.replace('$', '')
    data['movie_budgets']['production_budget'] = data['movie_budgets']['production_budget'].astype(int)

    data['movie_budgets']['domestic_gross'] = data['movie_budgets']['domestic_gross'].str.replace(',', '')
    data['movie_budgets']['domestic_gross'] = data['movie_budgets']['domestic_gross'].str.replace('$', '')
    data['movie_budgets']['domestic_gross'] = data['movie_budgets']['domestic_gross'].astype(int)

    #Dropping unecessary columns

    data['movie_budgets'] = data['movie_budgets'].drop(columns=['release_date','domestic_gross'])

    #Filter ratings dataframe to a minimum of 100 votes

    data['ratings'] = data['ratings'][data['ratings'].numvotes >= 100]

    #Renaming more columns *****Add this to other renaming cell

    data['akas'].rename(columns={'title_id': 'tconst'}, inplace = True)

    #Merging data on tconst

    tconst_to_title = pd.merge(data['akas'],data['ratings'],on='tconst')

    #Dropping uncessary columns from tconst_to_title dataframe

    tconst_to_title = tconst_to_title.drop(columns=['ordering','region','language','types','attributes','is_original_title'])

    #Merging tconst_to_title dataframe with movie_budgets dataframe on 'title' column

    master_table = pd.merge(tconst_to_title,data['movie_budgets'],on='title')

    master_table.head()

    #Defining 'Composite Quality Score' to help define successful movies

    master_table['success_score'] = master_table.averagerating * (master_table.worldwide_gross / master_table.production_budget)

    #Dropping duplicates from 'tconst' column in master_table dataframe

    master_table.drop_duplicates(subset = ['tconst'],inplace=True)

    master_table.head()

    #Merging title_basics dataframe to master_table dataframe on tconst

    master_table = pd.merge(data['title_basics'],master_table,on='tconst')

    master_table.head()

    #Making genre dataframe with individualized genres 

    gml=list(master_table["genres"].unique())
    genre_list=[]
    for genres in gml:
        genre_list.append(genres.split(","))
    genre_list
    genre_master=[]
    for genre in genre_list:
        for subgenre in genre:
            genre_master.append(subgenre)
    unique_genre_master=set(genre_master)
    vector=list(range(0,2521))
    df_genres=[]
    df_consts=[]
    for genre in unique_genre_master:
        for number in vector:
            if genre in master_table.iloc[number, 5]:
                df_genres.append(genre)
                df_consts.append(master_table.iloc[number, 0])
    genre_table=pd.DataFrame({'tconst':df_consts, 'genre':df_genres})
    complete_genre_table=pd.merge(genre_table, master_table, how="left", on="tconst")

    #Merging movie_info dataframe with master_table dataframe

    master_table = pd.merge(master_table, data['movie_info'],on='id')

    master_table = master_table.drop(columns=['original_title','theater_date','dvd_date','currency','box_office','studio','synopsis'])

    master_table.sort_values(by='worldwide_gross', ascending = False, inplace=True)

    master_table = master_table.dropna(subset = ['director'])

    master_table.isnull().sum()

    #Creating df_composer dataframe 

    df_composer = data['name_basics'].dropna(subset=['primary_profession','known_for_titles'])
    df_composer["title_length"]=df_composer["known_for_titles"].map(lambda x: x.count(',') + 1)
    df_composer = df_composer[df_composer.primary_profession.str.contains('composer')]

    #sorting for most popular composers

    df_composer.sort_values(by='title_length',ascending=False, inplace=True)

    #Making composer dataframe by making tconst individualized *****CHANGE NAMES TO REFLECT DIFFERENCE FROM GENRE

    gml=list(df_composer["known_for_titles"][:32])
    genre_list=[]
    for genres in gml:
        genre_list.append(list(genres.split(",")))
    genre_list
    genre_master=[]
    genre_master=[]
    for genre in genre_list:
        for subgenre in genre:
            genre_master.append(subgenre)

    unique_genre_master=set(genre_master)
    vector=list(range(0,46984))
    df_genres=[]
    df_consts=[]

    for genre in unique_genre_master:
        for number in vector:
            if genre in df_composer.iloc[number, 5]:
                df_genres.append(genre)
                df_consts.append(df_composer.iloc[number, 1])

    genre_table=pd.DataFrame({'composer':df_consts, 'tconst':df_genres})

    genre_table

    #Merging master with composer table

    master_composer = pd.merge(master_table,genre_table, on='tconst')



    #Removing problem data

    master_composer = master_composer[master_composer.composer != 'Matthew Emerson Brown']
    master_composer = master_composer[master_composer.composer != 'Joshua Morrison']
    master_composer = master_composer[master_composer.composer != 'Jeramy Koepping']
    master_composer = master_composer[master_composer.composer != 'Ed Cortes']

    master_composer.sort_values(by='success_score', ascending = False, inplace = True)

    master_table["roi"]=master_table.worldwide_gross/master_table.production_budget
    master_table["net_profit"]=master_table.worldwide_gross-master_table.production_budget
    figure, ax = plt.subplots(2, 2, figsize=(30, 30))
    x=master_table.groupby(groupby).mean().index
    y0_gross_rev= master_table.groupby(groupby).mean().worldwide_gross
    y1_net_prof= master_table.groupby(groupby).mean().worldwide_gross-master_table.groupby(groupby).mean().production_budget
    y2_roi_percent= master_table.groupby(groupby).mean().worldwide_gross/master_table.groupby(groupby).mean().production_budget
    y3_comp= master_table.groupby(groupby).mean().success_score 

    ax[0][0].set_title('Gross Revenue vs {}'.format(label))
    ax[0][0].set_xlabel('{}'.format(label))
    ax[0][0].set_ylabel('Gross Revenue ($)')
    ax[0][1].set_title('Net Profit vs {}'.format(label))
    ax[0][1].set_xlabel('{}'.format(label))
    ax[0][1].set_ylabel('Net Profit ($)')
    ax[1][0].set_title('Percent Return on Investment vs {}'.format(label))
    ax[1][0].set_xlabel('{}'.format(label))
    ax[1][0].set_ylabel('ROI (%)')
    ax[1][1].set_title('Composite Success Score vs {}'.format(label))
    ax[1][1].set_xlabel('{}'.format(label))
    ax[1][1].set_ylabel('Success Score')

    ax[0][0].set_xticklabels(x,rotation=45)
    ax[0][1].set_xticklabels(x,rotation=45)
    ax[1][0].set_xticklabels(x,rotation=45)
    ax[1][1].set_xticklabels(x,rotation=45)

    ax[0][0].spines['top'].set_visible(False)
    ax[0][0].spines['right'].set_visible(False)
    ax[0][0].spines['left'].set_visible(False)
    ax[0][0].spines['bottom'].set_color('#DDDDDD')

    ax[0][1].spines['top'].set_visible(False)
    ax[0][1].spines['right'].set_visible(False)
    ax[0][1].spines['left'].set_visible(False)
    ax[0][1].spines['bottom'].set_color('#DDDDDD')

    ax[1][0].spines['top'].set_visible(False)
    ax[1][0].spines['right'].set_visible(False)
    ax[1][0].spines['left'].set_visible(False)
    ax[1][0].spines['bottom'].set_color('#DDDDDD')

    ax[1][1].spines['top'].set_visible(False)
    ax[1][1].spines['right'].set_visible(False)
    ax[1][1].spines['left'].set_visible(False)
    ax[1][1].spines['bottom'].set_color('#DDDDDD')

    sns.set_style("whitegrid")
    sns.barplot(x, y0_gross_rev, ax=ax[0][0], color='green')
    sns.barplot(x, y1_net_prof, ax=ax[0][1], color='yellow')
    sns.barplot(x, y2_roi_percent, ax=ax[1][0], color='blue')
    sns.barplot(x, y3_comp, ax=ax[1][1], palette='YlGn')
    
    return figure