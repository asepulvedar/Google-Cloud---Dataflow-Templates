# Import necessary libraries
import apache_beam as beam
from apache_beam import coders
from apache_beam.io.gcp.bigquery import ReadFromBigQuery
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.jdbc import WriteToJdbc
from typing import NamedTuple


# Define pipeline options
options = PipelineOptions(
        region='us-central1',
        worker_zone='us-central1-c',
        num_workers=1,
        max_num_workers=5)
options.view_as(beam.options.pipeline_options.SetupOptions).save_main_session = True

# Set project ID and BigQuery table
project_id = "projectid"
bq_query="SELECT column1, column2 FROM projectid.dataset.table"

# Set SQL Server connection parameters
jdbc_driver_class_name="com.microsoft.sqlserver.jdbc.SQLServerDriver"
jdbc_url = "jdbc:sqlserver://serverip;databaseName=demo;;trustServerCertificate=true;"
jdbc_user = "sqlserver_user"
jdbc_password = "*****"
jdbc_output_tablename = "***"

# Bigquery Named Tuple for Query Table Schema
db_table_schema = NamedTuple(
     "table_schema",
     [
         ("column1", str),
         ("column2", int)
     ])

coders.registry.register_coder(db_table_schema, coders.RowCoder)

# Define pipeline
with beam.Pipeline(options=options) as pipeline:
    # Read data from BigQuery
    data = pipeline | ReadFromBigQuery(
        project=project_id,
        query=bq_query,
        use_standard_sql=True)

    # Map the Schema
    data_with_schema = data | beam.Map(lambda x: db_table_schema(column1=str(x["column1"]),
                                                                 column2=int(x["column2"]))).with_output_types(db_table_schema)

    # Write data to SQL Server
    data_with_schema | WriteToJdbc(driver_class_name=jdbc_driver_class_name,
        jdbc_url=jdbc_url,
        table_name=jdbc_output_tablename,
        username=jdbc_user,
        password=jdbc_password
    )