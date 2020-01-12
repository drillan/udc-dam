# Import required libraries
import copy
import datetime as dt
import math
import pathlib
import pickle

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import ClientsideFunction, Input, Output, State

# Multi-dropdown options
from controls import COUNTIES, WELL_COLORS, WELL_STATUSES, WELL_TYPES

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server
