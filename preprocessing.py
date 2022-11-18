import pandas as pd
import glob
import os

#cwd= os.path.abspath(r'data\taylorswift_lyrics')
#print('hello', cwd)
#file_list= os.listdir(cwd)
#print(file_list)

#for filename in os.listdir(cwd): 
    #print(filename)
    #df= pd.read_csv(filename)
    #df_concat= pd.concat([pd.read_csv(filename)], ignore_index= True)

#df_concat


taylor_swift= pd.read_csv(r'C:\Users\aimiw\OneDrive\Desktop\Big Data\BigDataFinalProject\data\taylorswift_lyrics\01-taylor_swift.csv')
#print(taylor_swift)
taylor_swift_edited= taylor_swift.drop('line', axis= 1)
taylor_swift_edited = taylor_swift_edited.groupby(['track_title'])['lyric'].apply(' '.join).reset_index()

taylor_swift_edited.to_csv('taylor_swift_combined_edited.csv', index= True)