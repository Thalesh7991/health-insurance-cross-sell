import pandas as pd
import numpy as np
import pickle
#import json


class HealthInsurance:
    def __init__( self ):
        # carregar todos os arquivos pickle de transformação de dados
        self.home_path = ''
        self.age_scaler = pickle.load( open( self.home_path + 'parameter/age_reescaling.pkl', 'rb') )
        self.region_encoder = pickle.load( open( self.home_path + 'parameter/encoder_region_coder.pkl', 'rb') )
        self.sales_channel_encoder = pickle.load( open( self.home_path + 'parameter/encoder_sales_channel.pkl', 'rb') )
        self.annual_premium_scaler = pickle.load( open( self.home_path + 'parameter/scaler_annual_premium.pkl', 'rb') )
        self.vintage_reescaling = pickle.load( open( self.home_path + 'parameter/vintage_reescaling.pkl', 'rb') )
    
    def feature_engineering(self, df2):
        # vehicle_damage
        df2['vehicle_damage'] = df2['vehicle_damage'].apply(lambda x: 1 if x == 'Yes' else 0)
        return df2
    
    def data_preparation(self, df4):
        # standat scaler
        df4['annual_premium'] = self.annual_premium_scaler.transform( df4[['annual_premium']].values )
        
        # reescaling
        df4['age'] = self.age_scaler.transform(df4[['age']].values)

        
        df4['vintage'] = self.vintage_reescaling.transform(df4[['vintage']].values)
        
        #encoder
        
        # gender
        list_gender = {'Male':1,'Female':0}
        df4['gender'] = df4['gender'].map(list_gender)
        

        # region_code
        df4.loc[:,'region_code'] = df4['region_code'].map(self.region_encoder)
        #df4.loc[:,'region_code'] = df4['region_code'].map(target_encode_region_code)

        # policy_sales_channel
        df4.loc[:,'policy_sales_channel'] = df4['policy_sales_channel'].map(self.sales_channel_encoder)
        
        # vehicle_age
        #df4 = pd.get_dummies(df4, prefix='vehicle_age',columns=['vehicle_age'])
        
        #Feature Selection
        #df4 = df4[['vintage','annual_premium','region_code','vehicle_damage','previously_insured', 'policy_sales_channel']]
        
        df4 = df4[['vintage', 'annual_premium', 'age', 'region_code','vehicle_damage','policy_sales_channel', 'previously_insured']]
        
        
        return df4
    
    def get_prediction(slef, model, original_data, test_data):
        #return original_data, test_data
        pred = model.predict_proba(test_data)
        ##
        original_data['score'] = pred[:, 1].tolist()
        original_data = original_data.sort_values('score', ascending=False)
        #return orinal_data
        return original_data.to_json(orient='records', date_format='iso')