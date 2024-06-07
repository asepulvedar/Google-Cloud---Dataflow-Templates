# Apache Beam Dataflow Pipelines on Google Cloud

This repository contains examples and scripts for running Apache Beam pipelines on Google Cloud Dataflow. The examples focus on data transfer between BigQuery and SQL Server, and between JDBC sources.

## Repository Structure

### BigQuery-To-JDBC
This directory contains the scripts and pipeline for transferring data from BigQuery to an SQL Server.

- **bq-to-sqlserver.py**: Apache Beam pipeline for transferring data from BigQuery to SQL Server.
- **execute-dataflow-pipeline.sh**: Shell script to execute the Dataflow pipeline.

### JDBC-To-JDBC
This directory contains the scripts and pipeline for transferring data between JDBC sources.

- **jdbc-to-jdbc.py**: Apache Beam pipeline for transferring data between two JDBC sources.
- **execute-dataflow-pipeline.sh**: Shell script to execute the Dataflow pipeline.

## Prerequisites

Before running these pipelines, ensure you have the following:

- Google Cloud SDK installed and configured.
- Apache Beam installed.
- Access to Google BigQuery and SQL Server instances.
- Necessary JDBC drivers for your databases.

## Getting Started

1. **Clone the repository**:
    ```sh
    git clone https://github.com/asepulvedar/GCP-Dataflow-Demo.git
    cd GCP-Dataflow-Demo
    ```

2. **Set up your environment**:
    Make sure to set up your Google Cloud project and authenticate with the following command:
    ```sh
    gcloud auth login
    gcloud config set project YOUR_PROJECT_ID
    ```

3. **Install Apache Beam**:
    ```sh
    pip install apache-beam[gcp]
    ```

## Running the Pipelines

### BigQuery to SQL Server

1. Modify the `bq-to-sqlserver.py` file to include your BigQuery and SQL Server details.
2. Run the shell script to execute the Dataflow pipeline:
    ```sh
    cd BigQuery-To-JDBC
    ./execute-dataflow-pipeline.sh
    ```

### JDBC to JDBC

1. Modify the `jdbc-to-jdbc.py` file to include your source and destination JDBC details.
2. Run the shell script to execute the Dataflow pipeline:
    ```sh
    cd JDBC-To-JDBC
    ./execute-dataflow-pipeline.sh
    ```

## Pipeline Details

### BigQuery to SQL Server (`bq-to-sqlserver.py`)

This pipeline reads data from a specified BigQuery table and writes it to a specified SQL Server table. It demonstrates the use of Beam's I/O connectors for BigQuery and JDBC.

### JDBC to JDBC (`jdbc-to-jdbc.py`)

This pipeline reads data from a specified JDBC source and writes it to another JDBC destination. It demonstrates the use of Beam's JDBC connectors for both input and output.

## Shell Scripts

The `execute-dataflow-pipeline.sh` scripts in each directory are designed to run the corresponding Python pipelines on Google Cloud Dataflow. Ensure you have the necessary permissions and configurations set up in your Google Cloud environment.

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request with your changes. 

