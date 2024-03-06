# Databricks notebook source
# MAGIC %pip install openpyxl
# MAGIC
# MAGIC import pandas as pd
# MAGIC excel_df = pd.read_excel("/Volumes/sparkdev/devspark/spark001/Test01.xlsx")
# MAGIC spark_df = spark.createDataFrame(excel_df)
# MAGIC spark_df.write.csv("/Volumes/sparkdev/devspark/spark001/output_csv_file.csv", header=True)
