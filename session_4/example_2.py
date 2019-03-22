""" 
This is the header of the python file
company name: pythoncourse
"""

import pandas as pd

counts_dict = {}

# Iterate over the file chunk by chunk
for chunk in pd.read_csv("iris.csv", chunksize=10):
    # Iterate over the "species" column in DataFrame
    for entry in chunk["species"]:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

    # for entry in chunk.values:
    #     for item in entry:
    #         print(item)
