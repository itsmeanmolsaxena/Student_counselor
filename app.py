from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipelines.analysis_pipeline import CustomData

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/options',methods=['GET','POST'])
def chatbot_services():
    if request.method=='GET':
        return render_template('chatbot_options.html')
    else:
        pass

    
@app.route('/details',methods=['GET','POST'])
def details_datapoint():
    if request.method=='GET':
        return render_template('student_details.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score')),
            math_score=float(request.form.get('math_score')),

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")
        results = [23]
        return render_template(('student_details.html'))

@app.route('/course',methods=['GET','POST'])
def course_recomendation():
    if request.method=='GET':
        return render_template('course_suggestions.html')
    else:
        pass


if __name__=="__main__":
    app.run(host="0.0.0.0")
         

