
## Compile the template
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
--pipeline_name=jdbctojdbc \
