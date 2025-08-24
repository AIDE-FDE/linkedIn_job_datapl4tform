import os
from contextlib import contextmanager
from datetime import datetime
from typing import Union

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from dagster import IOManager, OutputContext, InputContext
from minio import Minio

@contextmanager
def connect_to_clickhouse (config):
    pass


class ClickHouseIOManager (IOManager):
    def __init__(self, config):
        self.config = config

    def load_input(self, context) -> pd.DataFrame:
        pass

    def handle_output(self, context, obj):
        pass
    
