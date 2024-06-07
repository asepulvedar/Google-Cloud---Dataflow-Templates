## Execute the Dataflow pipeline
python3 bq-to-sqlserver.py \
--project=PROJECTID \
--region=us-central1 \
--pipeline_name=bq-to-sqlserver-demo \
--runner=DataflowRunner \
--staging_location=gs://BUCKETNAME/staging \
--temp_location=gs://bucketname/temp \
--job_name=bq-to-sqlserver-demo