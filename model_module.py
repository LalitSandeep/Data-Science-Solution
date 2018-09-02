import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.externals import joblib


def simplify_backers(df):
    
    bins = (-1, 2, 12, 56, 219382)
    group_names = ['1_quartile', '2_quartile', '3_quartile', '4_quartile']
    categories = pd.cut(df.backers, bins, labels=group_names)
    df.backers = categories
    return df

def encode_features(df_test):
    features = ['main_category', 'backers']
    df_combined = df_test[features]
    
    for feature in features:
        le = preprocessing.LabelEncoder()
        le = le.fit(df_combined[feature])
        df_test[feature] = le.transform(df_test[feature])
    return df_test

def test(filename):
    data_test=pd.read_csv(filename + ".csv")
    data_test['difference_in_val'] = data_test['usd_pledged_real'] - data_test['usd_goal_real']
    data_test.head(3)
    
    data_test['difference_in_val'][data_test['difference_in_val']>0]=1
    data_test['difference_in_val'][data_test['difference_in_val']<0]=0
    
    data_test=simplify_backers(data_test)

    data_test= encode_features(data_test)
    
    data_test = data_test.drop(['state','name','category','currency','deadline','goal','launched','pledged','country','usd pledged','usd_pledged_real','usd_goal_real'], axis=1)

    
    filename='saved_model.sav'
    
    loaded_model = joblib.load(filename)
    

    #X_all = data_train.drop(['state', 'ID','name','category','currency','deadline','goal','launched','pledged','state','country','usd pledged','usd_pledged_real','usd_goal_real'], axis=1)
    ids = data_test['ID']
    predictions = loaded_model.predict(data_test.drop('ID', axis=1))
    
    output = pd.DataFrame({ 'ID' : ids, 'state': predictions })
    
    output['state'] = output['state'].replace([1,0],['successful', 'not successful'])
    

   # output['state'] = output['state'].replace('0', 'not successful')
    
    output.to_csv('kickstarter-predictions.csv', index = False)




    



    

    