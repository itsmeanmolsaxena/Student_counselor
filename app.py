from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from src.pipelines.suggesstion_pipeline import CourseData
from src.pipelines.analysis_pipeline import CustomData
from src.components.data_transformation import DataTransformation

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

        df=data.get_data_as_data_frame()

        # Add a new column with the sum of the three numeric columns
        df['total_score'] = df['reading_score'] + df['writing_score'] + df['math_score']

        student_score = df.to_dict(orient='records')

        data_transformation = DataTransformation()

        avg_score = data_transformation.calculate_average_of_scores()

        return render_template(('analysis.html'),total_score=student_score[0]['total_score'], 
                               math_score = student_score[0]['math_score'], 
                               reading_score = student_score[0]['reading_score'], 
                               writing_score = student_score[0]['writing_score'],
                               avg_total_score = avg_score['Total Score'],
                               avg_reading_score = avg_score['ReadingScore'],
                               avg_writing_score = avg_score['WritingScore'],
                               avg_math_score = avg_score['MathScore'])

@app.route('/course',methods=['GET','POST'])
def course_recomendation():
    if request.method=='GET':
        return render_template('course_suggestions.html')
    else:
        data=CourseData(
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score')),
            math_score=float(request.form.get('math_score')),

        )

        df=data.get_score_as_a_dict()

        return render_template(('career.html'))

if __name__=="__main__":
    app.run(host="0.0.0.0")
         

