import pandas as pd

from src.pipeline.transform import contact_dataframes


def test_contact_dataframes():
    # Test case 1: Concatenating two dataframes with same columns
    df_1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    df_2 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    arrange = pd.concat([df_1, df_2], ignore_index=True)
    act = contact_dataframes([df_1, df_2])
    assert act.equals(arrange)
    assert act.shape == (4, 2)
    assert arrange.shape == (4, 2)

    # Test case 2: Concatenating two dataframes with different columns
    df_3 = pd.DataFrame({'col1': [1, 2], 'col3': [5, 6]})
    df_4 = pd.DataFrame({'col1': [3, 4], 'col4': [7, 8]})
    arrange = pd.concat([df_3, df_4], ignore_index=True)
    act = contact_dataframes([df_3, df_4])
    assert act.equals(arrange)
    assert act.shape == (4, 3)
    assert arrange.shape == (4, 3)

    # Test case 3: Concatenating three dataframes
    df_5 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    df_6 = pd.DataFrame({'col1': [3, 4], 'col2': [5, 6]})
    df_7 = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})
    arrange = pd.concat([df_5, df_6, df_7], ignore_index=True)
    act = contact_dataframes([df_5, df_6, df_7])
    assert act.equals(arrange)
    assert act.shape == (6, 2)
    assert arrange.shape == (6, 2)

    # Test case 4: Concatenating empty dataframes
    df_8 = pd.DataFrame()
    df_9 = pd.DataFrame()
    arrange = pd.concat([df_8, df_9], ignore_index=True)
    act = contact_dataframes([df_8, df_9])
    assert act.equals(arrange)
    assert act.shape == (0, 0)
    assert arrange.shape == (0, 0)
