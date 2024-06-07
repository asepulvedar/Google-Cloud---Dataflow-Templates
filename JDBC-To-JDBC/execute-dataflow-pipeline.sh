## Execute the Dataflow pipeline
python3 jdbc-to-jdbc.py \
--project=PROJECTID \
--region=us-central1 \
--pipeline_name=jdbc-to-jdbc-demo \
--runner=DataflowRunner \
--staging_location=gs://BUCKETNAME/staging \
--temp_location=gs://BUCKET/temp \
--job_name=jdbc-to-jdbc-demo