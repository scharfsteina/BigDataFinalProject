import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import statistics
import math

data = pd.read_csv('data/fullymerged.csv', index_col = 0)
# get subset of relevant spotify features + billboard binary
temp = data.iloc[:,6:15]
temp['On Billboard'] = data.iloc[:,-1]
data = temp
features = list(data.columns)
features.pop()

# Normalizing columns
for f in features:
    data[f] = (data[f]- data[f].mean()) / data[f].std()

#print((data[features[0]]).mean()) # should be ~ zero
#print((data[features[0]]).std()) # should be ~ 1

sns.set_theme(style="whitegrid")
ax = sns.countplot(x=data['On Billboard'])
# for p in ax.patches:
#    ax.annotate('{:.1f}'.format(p.get_height()), (p.get_x()+p.get_width()/2-.05, p.get_height()+0.25))
plt.show()



model = LogisticRegression(random_state=0).fit(data[features].values, data['On Billboard'].values)
score = model.score(data[features].values, data['On Billboard'].values)
print(score) # 75 % is not great

w0 = model.intercept_[0]
w = model.coef_[0]
 
equation = "y = %f + (%f * x1) + (%f * x2) + (%f * x3) + (%f * x4)" % (w0, w[0], w[1], w[2], w[3])
print(equation)

idx = 99
x = data.iloc[idx][features].values
y = model.predict_proba(x.reshape(1, -1))[0]
print(y[1])

feature_importance = pd.DataFrame(features, columns = ["feature"])
feature_importance["importance"] = pow(math.e, w)
feature_importance = feature_importance.sort_values(by = ["importance"], ascending=False)
 
ax = feature_importance.plot.barh(x='feature', y='importance')
plt.show()
