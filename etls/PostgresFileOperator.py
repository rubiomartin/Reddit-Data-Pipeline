from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.providers.postgres.hooks.postgres import PostgresHook
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.constants import csv_path

class PostgresFileOperator(BaseOperator):
    @apply_defaults
    def __init__(self,
                 operation,
                 config={},
                 *args,
                 **kwargs):
        super(PostgresFileOperator, self).__init__(*args, **kwargs)
        self.operation = operation
        self.config = config
        self.postgres_hook = PostgresHook(postgres_conn_id='postgres_default')


    def execute(self, context):
        if self.operation == "write":
            self.writeInDb()

        elif self.operation == "read":
            pass
    
    def writeInDb (self):
        self.postgres_hook.bulk_load(self.config.get('table_name'), csv_path)
