# Compile the Template

To compile and execute the JDBC-to-JDBC template using Apache Beam on Google Cloud Dataflow, follow these steps. This example demonstrates transferring data from one PostgreSQL database to another.

## Command Overview

The following command runs the `jdbctojdbc` Python module with specified parameters to configure and execute the Dataflow pipeline:

```sh
python3 -m jdbctojdbc \
--runner=DataflowRunner \
--region=us-central1 \
--project=PROJECTID \
--num_workers=1 \
--max_num_workers=5 \
--input_jdbc_url=jdbc:postgresql://1.1.1.1:5432/demo1 \
--input_driver_class_name=org.postgresql.Driver \
--input_sql_server_query=select * from public.inputdata \
--input_table_name=public.inputdata \
--input_username=postgres \
--input_password=SECUREPASSWORD \
--output_jdbc_url=jdbc:postgresql://1.1.1.1:5432/demo2 \
--output_driver_class_name=org.postgresql.Driver \
--output_table_name=public.outputdata \
--output_username=postgres \
--output_password=SECUREPASSWORD \
--staging_location=gs://BUCKETNAME/staging \
--temp_location=gs://BUCKETNAME/temp \
--template_location=gs://BUCKETNAME/templates/jdbc-to-jdbc/new \
--pipeline_name=jdbctojdbc

```
## Parameter Breakdown

- `--runner=DataflowRunner`: Specifies that the pipeline should run on Google Cloud Dataflow.
- `--region=us-central1`: Specifies the region where Dataflow jobs will run.
- `--project=PROJECTID`: Your Google Cloud project ID.
- `--num_workers=1`: The initial number of workers to start the pipeline with.
- `--max_num_workers=5`: The maximum number of workers to scale up to.
- `--input_jdbc_url=jdbc:postgresql://1.1.1.1:5432/demo1`: JDBC URL for the input PostgreSQL database.
- `--input_driver_class_name=org.postgresql.Driver`: Driver class name for the input database.
- `--input_sql_server_query=select * from public.inputdata`: SQL query to select data from the input database.
- `--input_table_name=public.inputdata`: Name of the input table.
- `--input_username=postgres`: Username for the input database.
- `--input_password=SECUREPASSWORD`: Password for the input database.
- `--output_jdbc_url=jdbc:postgresql://1.1.1.1:5432/demo2`: JDBC URL for the output PostgreSQL database.
- `--output_driver_class_name=org.postgresql.Driver`: Driver class name for the output database.
- `--output_table_name=public.outputdata`: Name of the output table.
- `--output_username=postgres`: Username for the output database.
- `--output_password=SECUREPASSWORD`: Password for the output database.
- `--staging_location=gs://BUCKETNAME/staging`: Google Cloud Storage bucket for staging files.
- `--temp_location=gs://BUCKETNAME/temp`: Google Cloud Storage bucket for temporary files.
- `--template_location=gs://BUCKETNAME/templates/jdbc-to-jdbc/new`: Google Cloud Storage location to save the Dataflow template.
- `--pipeline_name=jdbctojdbc`: Name of the pipeline.
