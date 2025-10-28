import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from FiinQuantX import FiinSession

client = FiinSession(
    username="DSTC_13@fiinquant.vn",
    password="Fiinquant0606",
).login()

fi = client.FiinIndicator()

benchmark = client.Fetch_Trading_Data(
    realtime=False,
    tickers=["VNINDEX", "VN30", "HNXINDEX", "UPCOMINDEX"],
    fields=["close"],
    adjusted=True,
    by="1d",
    from_date="2023-01-01"
).get_data()

benchmark.to_csv('benchmark.csv', index=True)