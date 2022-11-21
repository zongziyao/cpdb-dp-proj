import warnings
import time
import snsql
from snsql import Privacy


def dp_execute_sql_query(database, metadata, query, epsilon, delta):
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning)

        start = time.time()
        privacy = Privacy(epsilon=epsilon, delta=delta)
        reader = snsql.from_connection(database, privacy=privacy, metadata=metadata)
        result = reader.execute(query)
        exec_time = time.time() - start
        return result, exec_time


def execute_sql_query(database, query):
    cur = database.cursor()
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    return result


def compute_epsilon(x, err_rate, sensitivity=1):
    err = x * err_rate
    return (2 * sensitivity / err) ** 0.5


def get_delta(n):
    return 1 / n * (n ** 0.5)
