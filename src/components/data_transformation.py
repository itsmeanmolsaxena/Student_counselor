import sys
# from dataclasses import dataclass
 
import pandas as pd
from src.exception import CustomException
from src.logger import logging
# from src.utils import save_object

class DataTransformation:

    def calculate_average_of_scores(self):
        try:

            data_path = "notebook/data/student_data.csv"
            df = pd.read_csv(data_path)

            logging.info("Read data completed")

            numeric_columns = ['MathScore', 'ReadingScore', 'WritingScore']

            # Add a new column with the sum of the three numeric columns
            df['Total Score'] = df[numeric_columns].sum(axis=1)

            columns = ['MathScore', 'ReadingScore', 'WritingScore', 'Total Score']

            # Calculate the average of each column
            column_averages = df[columns].mean(axis=0)

            #convert series to dictionary
            average_scores = column_averages.to_dict()

            average_scores = {key: round(value, 2) for key, value in average_scores.items()}

            return average_scores

        except Exception as e:
            raise CustomException(e, sys)
