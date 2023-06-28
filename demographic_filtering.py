import numpy as np
import pandas as pd

shared = pd.read_csv('shared_articles.csv')
output = shared[['eventType','contentId','title']].sort_values('eventType',ascending=True)
print(shared.head(20))