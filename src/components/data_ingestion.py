import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import exception_fun

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class data_ingestion_config:
    raw_data_path = os.path.join('artifacts', 'raw_data.csv')
    train_data_path = os.path.join('artifacts', 'train.csv')
    test_data_path = os.path.join('artifacts', 'test_data.csv')



class data_ingestion:

    def __init__(self):

        self.ingestion_config = data_ingestion_config()


    def start_data_ingestion(self):

        logging.info('started data ingestion...!')

        try:
            logging.info('reading the raw data...!')

            mydata = pd.read_csv('data\\train.csv')

            logging.info('read the raw data...!')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            mydata.to_csv(self.ingestion_config.raw_data_path, index = False, header=True)

            logging.info('splitting the data into training and testing...!')

            train_data , test_data = train_test_split(mydata, test_size = 0.2)

            train_data.to_csv(self.ingestion_config.train_data_path, index = False, header = True)

            test_data.to_csv(self.ingestion_config.test_data_path, index = False, header = True)

            logging.info('completed splitting train and test data...!')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )



        except Exception as error:
            raise exception_fun(error, sys)
        

if __name__ == '__main__':
    load_data = data_ingestion()
    train_data, test_data = load_data.start_data_ingestion()