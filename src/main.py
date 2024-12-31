import duckdb
import time
import pandas as pd

def create_duckdb():
    df = duckdb.sql("""
        SELECT date, name, age, city, state, fare, gender, occupation
        FROM read_csv("data/users.csv", AUTO_DETECT=TRUE, sep=',')
    """)

    return df

if __name__ == "__main__":
    import time
    start_time = time.time()

    df = create_duckdb()

    print(df.head())
    took = time.time() - start_time
    print(f"Duckdb Took: {took:.2f} sec")