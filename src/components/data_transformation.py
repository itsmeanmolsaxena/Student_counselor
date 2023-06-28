import sys
# from dataclasses import dataclass
 
import pandas as pd
from src.exception import CustomException
from src.logger import logging
# from src.utils import save_object

class DataTransformation:

    def add_scores_to_dataframe(self):
        try:

            data_path = "notebook/data/student_data.csv"
            df = pd.read_csv(data_path)

            logging.info("Read data completed")

            numeric_columns = ['MathScore', 'ReadingScore', 'WritingScore']

            # Add a new column with the sum of the three numeric columns
            df['Total Score'] = df[numeric_columns].sum(axis=1)

            # Print the updated dataset
            # print(df.head(5))

            columns = ['MathScore', 'ReadingScore', 'WritingScore', 'Total Score']

            # Calculate the average of each column
            column_averages = df[columns].mean(axis=0)

            # Print the column averages
            print(column_averages)

            return column_averages

        except Exception as e:
            raise CustomException(e, sys)
