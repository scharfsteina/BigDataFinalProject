import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df= pd.read_csv(f"data\genius.csv")
v = TfidfVectorizer()
x = v.fit_transform(df['lyric'])
#print(x.toarray())

tfidf_df= pd.DataFrame(x.toarray(), index= df['track_title'], columns= v.get_feature_names_out())

tfidf_df.to_csv('data/tfidf_embedding.csv', index= True)
