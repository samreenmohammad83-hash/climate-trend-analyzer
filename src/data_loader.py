import pandas as pd
import numpy as np

def load_data():
    dates = pd.date_range(start="2000-01-01", periods=500)

    data = pd.DataFrame({
        "date": dates,
        "temperature": np.random.normal(25, 5, len(dates)).cumsum()/50 + 25,
        "rainfall": np.random.normal(5, 2, len(dates)),
        "humidity": np.random.normal(60, 10, len(dates))
    })

    return data