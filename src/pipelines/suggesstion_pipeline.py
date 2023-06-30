import sys
import pandas as pd
from src.exception import CustomException


class SugesstionPipeline:
    def __init__(self):
        pass

class CourseData:
    def __init__(  self,
        reading_score: int,
        writing_score: int,
        math_score: int):

        self.reading_score = reading_score

        self.writing_score = writing_score

        self.math_score = math_score

    def get_score_as_a_dict(self):
        try:
            custom_data_input_dict = {
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
                "math_score": [self.math_score],
            }

            df = pd.DataFrame(custom_data_input_dict)
            
            student_score = df.to_dict(orient='records')

            return student_score

        except Exception as e:
            raise CustomException(e, sys)
        
    # def get_highest_marks():

