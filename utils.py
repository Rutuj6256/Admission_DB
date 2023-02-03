import pickle
import json
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pymongo
mongo_client = pymongo.MongoClient("mongodb://localhost:27017")
database_name = "Admission_Prediction_Project"
db = mongo_client[database_name]
collection_user = db['user_details']

class AdmissionPrediction():
    def __init__ (self,GRE_Score, TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research):
        self.GRE_Score = GRE_Score
        self.TOEFL_Score = TOEFL_Score
        self.University_Rating = University_Rating
        self.SOP = SOP
        self.LOR = LOR
        self.CGPA = CGPA
        self.Research = Research

        self.collection_user =db['user_details']
        self.collection_user.insert_one({"GRE_Score_db":self.GRE_Score,"TOEFL_Score_db": self.TOEFL_Score,"University_Rating_db" :self.University_Rating ,
        "SOP_db":self.SOP,"LOR_db":self.LOR,"CGPA_db":self.CGPA,"Research_db":self.Research})
        self.collection_prediction =db['Prediction']
        
    def __load_model(self):

        with open('artifacts/Linear_Model.pkl','rb') as f:
            self.linear_model = pickle.load(f)
            print('Linear Model >>>>',self.linear_model)

        with open ('artifacts/Project_Data.json','r') as f:
            self.project_data = json.load(f)
            print('Project Data >>>>',self.project_data)

    def get_prediction(self):

        self.__load_model()

        test_array = np.array([self.GRE_Score,self.TOEFL_Score,self.University_Rating,self.SOP,self.LOR,self.CGPA,self.Research])
        print('Test Array >>>>',test_array)
        adm_prediction = self.linear_model.predict([test_array])
        print('Prediction Percentage >>>',adm_prediction)
        # return adm_prediction

        if (adm_prediction >= 0.85):
            print('Admission Will Take Place')
            self.collection_prediction.insert_one({"Prediction_db":'Admission Will Take Place'})
            return  'Get Admission'
            

        else:
            print('Admission Will Not Take Place')
            self.collection_prediction.insert_one({"Prediction_db":'Admission Will Not Take Place'})
            return 'Not Get Admission'

