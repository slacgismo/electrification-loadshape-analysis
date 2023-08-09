"""
Module containing utility functions for electrification loadshape analysis
"""

import numpy as np
from sg2t.io.loadshapes.nrel.naming import NREL_COL_MAPPING

def format_columns_df(df):
     # Rename columns using NREL_COL_MAPPING and drop the rest of the columns
    df.rename(columns=NREL_COL_MAPPING, inplace = True)
    df = df[df.columns.intersection([*NREL_COL_MAPPING.values()])]
    return df


def sigmoid(x, L, k, x0):
    # Sigmoid function for end-uses
    return L / (1 + np.exp(-k*(x-x0)))

def loadshape_analysis(df):
    # Loadshape analysis -- *state wide*
    # Current peak value and timing
    current_peak = df[df['State Electricity Total'] == df['State Electricity Total'].max()]
    val = current_peak['State Electricity Total'].values/1e3 *(60/15)
    current_peak_time = str(current_peak.hour.values[0]) + ':00'

    # New peak value and timing
    new_peak = df[df['State New Electricity Total'] == df['State New Electricity Total'].max()]
    new_val = new_peak['State New Electricity Total'].values/1e3 *(60/15)
    new_peak_time = str(new_peak.hour.values[0]) + ':00'
    load_growth = new_peak['State Load Growth'].values[0]*100

    # Greatest New Supply value and timing
    new_supply_peak = df[df['State New Supply'] == df['State New Supply'].max()]
    supply_val = new_supply_peak['State New Supply'].values/1e3 *(60/15)
    supply_peak_time = str(new_supply_peak.hour.values[0]) + ':00'

    return val, current_peak_time, new_val, new_peak_time, load_growth, supply_val, supply_peak_time