# Apache Beam Pipeline for JDBC-to-JDBC Data Transfer

# This Apache Beam pipeline demonstrates how to transfer data from one JDBC source to another using Google Cloud Dataflow. The pipeline reads data from a specified JDBC source and writes it to a specified JDBC destination.


# Import Necessary Libraries

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
## The MyOptions class extends PipelineOptions to include additional arguments required for JDBC configuration.
class MyOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        #parser.add_argument('--region', type=str)
        #parser.add_argument('--worker_zone', type=str)
        #parser.add_argument('--num_workers', type=int)
        #parser.add_argument('--max_num_workers', type=int)
        parser.add_argument('--input_jdbc_url', type=str,default="jdbc:postgresql://server:port/database")
        parser.add_argument('--input_driver_class_name', type=str,default="org.postgresql.Driver")
        parser.add_argument('--input_sql_server_query', type=str,default="select * from table")
        parser.add_argument('--input_table_name', type=str, default="public.tablename")
        parser.add_argument('--input_username', type=str, default="username")
        parser.add_argument('--input_password', type=str,default="password")
        parser.add_argument('--output_jdbc_url', type=str,default="jdbc:postgresql://server:port/database")
        parser.add_argument('--output_driver_class_name',type=str,default="org.postgresql.Driver")
        parser.add_argument('--output_table_name', type=str,default="public.tablename")
        parser.add_argument('--output_username', type=str,default="username")
        parser.add_argument('--output_password', type=str,default="password")

# Set Pipeline Options
# Initialize the pipeline options, including the custom MyOptions.
options = PipelineOptions()
pipeline_config_options  = options.view_as(MyOptions)

# Define pipeline
# Create and execute the Beam pipeline with JDBC read and write transformations.

with beam.Pipeline(options=options) as p:
    result = (
        p
        | 'Read from jdbc' >> ReadFromJdbc(
            table_name=pipeline_config_options.input_table_name,
            driver_class_name=pipeline_config_options.input_driver_class_name,
            jdbc_url=pipeline_config_options.input_jdbc_url,
            username=pipeline_config_options.input_username,
            password=pipeline_config_options.input_password,
        )
        | 'Write To Jdbc' >>  WriteToJdbc(
            driver_class_name=pipeline_config_options.output_driver_class_name,
            jdbc_url=pipeline_config_options.output_jdbc_url,
            table_name=pipeline_config_options.output_table_name,
            username=pipeline_config_options.output_username,
            password=pipeline_config_options.output_password)
        )
