import pandas as pd 
from typing import List

def contact_dataframes(data_frame_list: list[pd.DataFrame]) -> pd.DataFrame:
    """
    função para transformar uma lista de dataframes em um único dataframe

    """
    return pd.concat(data_frame_list, ignore_index=True)