# Import necessary libraries
import apache_beam as beam
from apache_beam import coders
from typing import NamedTuple
import typing
#from apache_beam.testing.test_pipeline import TestPipeline
#from apache_beam.io import ReadFromBigQuery
from apache_beam.io.gcp.bigquery import ReadFromBigQuery
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.jdbc import WriteToJdbc, ReadFromJdbc

# Define pipeline options
options = PipelineOptions(region='us-central1',
        worker_zone='us-central1-c',
        num_workers=1,
        max_num_workers=5)
options.view_as(beam.options.pipeline_options.SetupOptions).save_main_session = True

# Set JDBC connection parameters
## Input Database Params
input_sql_server_url = "jdbc:postgresql://1.1.1.1:5432/demo1"
input_sql_server_query = "select * from public.inputdata"
input_jdbc_table="public.inputdata"
input_sql_server_user = "postgres"
input_sql_server_password = "securepassword"

## Output Database Params
output_sql_server_url = "jdbc:postgresql://1.1.1.1:5432/demo2"
output_sql_server_table = "public.outputdata"
output_sql_server_user = "postgres"
output_sql_server_password = "securepassword"

# Define pipeline

with beam.Pipeline(options=options) as p:
    result = (
        p
        | 'Read from jdbc' >> ReadFromJdbc(
            table_name=input_jdbc_table,
            driver_class_name="org.postgresql.Driver",
            jdbc_url=input_sql_server_url,
            username=input_sql_server_user,
            password=input_sql_server_password,
        )
        | 'Write To Jdbc' >>  WriteToJdbc(
            driver_class_name="org.postgresql.Driver",
            jdbc_url=output_sql_server_url,
            table_name=output_sql_server_table,
            username=output_sql_server_user,
            password=output_sql_server_password)
        )
