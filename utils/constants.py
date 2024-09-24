import configparser
import os
from datetime import datetime


parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

SECRET = parser.get('api_keys', 'reddit_secret_key')
CLIENT_ID = parser.get('api_keys', 'reddit_client_id')
USER_AGENT = parser.get ('api_keys', 'reddit_user_agent')

OUTPUT_PATH = parser.get('file_paths', 'output_path')

POST_FIELDS = (
    'id',
    'title',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'over_18',
    'edited',
    'spoiler',
    'stickied'
)


file_postfix = datetime.now().strftime("%Y%m%d")
csv_path = f'/opt/airflow/data/output/reddit_{file_postfix}.csv'