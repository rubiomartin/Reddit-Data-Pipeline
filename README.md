# Extracting, Cleaning, and Storing Reddit Posts Using the PRAW API and PostgreSQL

This is a project where I use Python and the [Reddit API](https://praw.readthedocs.io/en/stable/ "Reddit API") to extract posts from Reddit, clean the data, and store it in a PostgreSQL database. The purpose of the project is to organize and analyze Reddit data for further insights, such as trends in user posts, popular topics, and discussions. The pipeline ensures that the data is properly formatted and stored.

## Overview

#### The pipeline is designed to:

1. **Extract posts from Reddit using the PRAW API.**
2. **Clean and preprocess the extracted data.**
3. **Store the cleaned data into a PostgreSQL database for analysis and querying..**
![reddit_diagram.jpg](assets%2Freddit_diagram.jpg)
## Tools
1. **[Reddit API](https://praw.readthedocs.io/en/stable/ "Reddit API")**: Source of the data.
2. **Apache Airflow**: Orchestrates the ETL process and manages task distribution.
3. **Pandas library**: Managing and cleaning data.
4. **PostgreSQL**: Storage of the data.
5. **Docker**: Contains the execution of Airflow.
