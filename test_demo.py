# To run the pipeline

from wheat.logger import logging
import os,sys
from wheat.pipeline.pipeline import Pipeline

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == "__main__":
    main()

# python test_demo.py