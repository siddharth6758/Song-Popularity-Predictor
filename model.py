import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle as pk
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


df = pd.read_csv('C:\\Users\\Dell\\OneDrive\\Desktop\\Project3\\Dataset\\dataset.csv')
df = df.dropna()  
df = df.drop_duplicates()
df = df.drop_duplicates(subset = ['track_id'])
# freq_encode = df['track_genre'].value_counts(normalize=True)
# df['genre_frequency'] = df['track_genre'].map(freq_encode)
# df.drop(columns=['track_genre'], inplace=True)
df['explicit'] = pd.get_dummies(df['explicit'], drop_first=True)
df = df.drop(['track_id','artists','album_name','track_name','track_genre'],axis=1)
df2 = df.copy()
df2['popularity_Class'] = (df2['popularity'] > 50) * 1
df2 = df2.drop(['popularity'],axis=1)
# dftst = pd.read_csv('C:\\Users\\Dell\\OneDrive\\Desktop\\Project 2\\test.csv')

# X = df.iloc[:,5:19]
# # print(X)
# Y = df['popularity']
X = df.drop('popularity', axis=1)
y = df['popularity']
XClass = df2.drop('popularity_Class', axis=1)
yClass = df2['popularity_Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#Classification Dataset
X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(XClass, yClass, test_size=0.2, random_state=42)
# Xts = dftst
# xtr,xts,ytr,yts = train_test_split(X,Y,test_size=0.3,random_state=1000)

# le = LabelEncoder()
# X['explicit'] = le.fit_transform(X['explicit'])
# Xts['explicit'] = le.fit_transform(Xts['explicit'])
# print(pd.DataFrame(xtr))

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
#Classification Dataset
X_train_scaled2 = scaler.fit_transform(X_train_class)
X_test_scaled2 = scaler.transform(X_test_class)
# sc = StandardScaler()
# X = sc.fit_transform(X)
# Xts = sc.transform(Xts)
# # print(pd.DataFrame(xtr))

#1
# lr = LinearRegression()
# lr.fit(X_train,y_train)
# predictions = lr.predict(X_test)

#2
# lrScaled = LinearRegression()
# lrScaled.fit(X_train_scaled, y_train)
# predictions_scaled = lrScaled.predict(X_test_scaled)

#3
classifier1 = DecisionTreeClassifier(max_leaf_nodes=10,random_state=0)
classifier1.fit(X_train_class,y_train_class)
predictionsClass1 = classifier1.predict(X_test_class)

#4
classifier2 = DecisionTreeClassifier(max_leaf_nodes=15,random_state=0)
classifier2.fit(X_train_scaled2,y_train_class)
predictionsClass2 = classifier2.predict(X_test_scaled2)

#5
dtR = DecisionTreeRegressor().fit(X_train, y_train)
# print(X_test)
predictionsR2 = dtR.predict(X_test)

#6
dtR_Scaled = DecisionTreeRegressor().fit(X_train_scaled, y_train)
predictionsR2_scaled = dtR_Scaled.predict(X_test_scaled)

#7
rfr = RandomForestRegressor(random_state = 42, max_leaf_nodes = 20).fit(X_train, y_train)
predictionsRfr = rfr.predict(X_test)

# lr = LinearRegression()
# lr.fit(X,Y)
pk.dump(rfr,open('flaskmodel.pkl','wb'))

#pickle to access the model outside this file
# testmodel = pk.load(open('flaskmodel.pkl','rb'))
# pred = testmodel.predict(Xts)
# print(pred)
# mse = metrics.mean_squared_error(yts,pred)
# print("MSE:",mse)