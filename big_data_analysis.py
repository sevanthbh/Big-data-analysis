import dask.dataframe as dd
import numpy as np
import pandas as pd
from dask.distributed import Client
import multiprocessing

def create_large_dataset(seed):
    """Generate a large random dataset."""
    np.random.seed(seed)
    data = np.random.rand(10_000, 10)  # 10,000 rows, 10 columns
    df = pd.DataFrame(data, columns=[f'col_{i}' for i in range(10)])
    print(f"✅ Large dataset {seed} created!")
    return df

if __name__ == '__main__':
    # Initialize Dask client
    client = Client()
    print(f"🚀 Dask Client Started: {client.dashboard_link}")

    # Use multiprocessing to generate multiple datasets
    with multiprocessing.Pool(5) as pool:
        datasets = pool.map(create_large_dataset, range(5))  # Create 5 datasets

    # Convert datasets into a single Dask DataFrame
    ddf = dd.from_pandas(pd.concat(datasets), npartitions=5)

    # Perform a basic analysis (e.g., mean of all columns)
    result = ddf.mean().compute()
    
    print("\n✅ Data Analysis Result:")
    print(result)

    # Close Dask Client
    client.close()

