# Real time data pipeline

This kafka project uses confluent_kafka API to create a kafka producer and consumer to perform ETL process.

## docker-compose.yml

What this yaml file consists of is 2 images: zookeeper, broke and an image for MySQL to send and store data.
Environemnt variables have been added to a `.env` file which is also added to `.gitignore` for security.

## producer.py

A python file which creates the kafka producer, sending events to a topic.

## consumer.py

A python file which creates the kafka consumer, receiving events from a topic.