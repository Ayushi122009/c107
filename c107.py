import csv
import pandas as pd
import plotly.graph_objects as go

f = pd.read_csv("data.csv")
student_df = f.loc[f["student_id"]=="TRL_xyz"]
print(student_df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    x= student_df.groupby("level")["attempt"].mean(),
    y= ["Level 1","Level 2", "Level 3", "Level 4"],
    orientation = "h"
))

fig.show()