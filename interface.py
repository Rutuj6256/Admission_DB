from flask import Flask,render_template,jsonify,request
from utils import AdmissionPrediction
import config
import traceback

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admission/prediction',methods = ['GET','POST'])
def predict_admisiion():
    try :
        if request.method == 'POST':
            data = request.form.get
            print(data)
            GRE_Score = eval(data('GRE_Score'))
            TOEFL_Score = eval(data('TOEFL_Score'))
            University_Rating = eval(data('University_Rating'))
            SOP = eval(data('SOP'))
            LOR = eval(data('LOR'))
            CGPA = eval(data('CGPA'))
            Research = eval(data('Research'))
        

        else:
            data = request.args.get
            print(data)
            GRE_Score = eval(data('GRE_Score'))
            TOEFL_Score = eval(data('TOEFL_Score'))
            University_Rating = eval(data('University_Rating'))
            SOP = eval(data('SOP'))
            LOR = eval(data('LOR'))
            CGPA = eval(data('CGPA'))
            Research = eval(data('Research'))
       
    except:
        print(traceback.print_exc())
        return jsonify({"Message" : "Unsuccessful"})

    admission_prediction = AdmissionPrediction(GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research)
    prediction_adm = admission_prediction.get_prediction()
    return render_template('index.html',prediction = prediction_adm )

if __name__ == '__main__':
    app.run(host=config.HOST , port=config.PORT_NO)