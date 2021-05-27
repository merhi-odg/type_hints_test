from typing import Dict
import pandas

# modelop.init
def init(job_json: Dict) -> None:
    print("Entering init", flush=True)
    print(job_json, flush=True)


# modelop.score
def score(x: Dict) -> Dict:
    print("Entering score", flush=True)
    print(x, flush=True)
    yield {"input_keys": list(x.keys()), "input_values": list(x.values())}


# modelop.metrics
def metrics(df1: pandas.DataFrame, df2: pandas.DataFrame) -> Dict:
    print("Entering metrics", flush=True)

    yield {"df1_rows": df1.shape[0], "df2_rows": df2.shape[0]}
