import os
import sys
import pandas as pd
import numpy as np
'''
Defining common constant var for traing pipeline 
'''
TARGET_COLUMN = "Result"
PIPELINE_NAME :str = "NetworkSecurity"
ARTIFACT_DIR :str = "Artifacts"
FILE_NAME : str = "phisingData.csv"

TRAIN_FILE__NAME : str = "train.csv"
TEST_FILE_NAME : str = "test.csv"

'''
Schema file path
'''
SCHEMA_FILE_PATH = os.path.join("data_schema","schema.yaml")

'''
Data Ingestion related constant start with Data_Ingestion VAR NAME
'''

DATA_INGESTION_COLLECTION_NAME : str = "NetworkData"
DATA_INGESTION_DATABASE_NAME : str = "YAGHYA_AI"
DATA_INGESTION_DIR_NAME : str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR : str = "feature_store"
DATA_INGESTION_INGESTED_DIR : str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO : float = 0.2

'''
Data Validation related constant start eith Data_Validation VAR name
'''

DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_VALID_DIR:str = "validated"
DATA_VALIDATION_INVALID_DIR:str ="invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str ="report.yaml"