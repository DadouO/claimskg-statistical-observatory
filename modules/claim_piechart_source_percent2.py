#!/usr/bin/env python
# import matplotlib.pyplot as plt
import json
from pathlib import Path

import pandas as pd
import plotly
import plotly.graph_objs as go


# pd.set_option('display.max_colwidth', -1)
# pd.set_option('display.max_columns', None)

def create_piechart_source():
    ##########################load df
    # df_complete = pd.read_csv('df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
    base_path = Path(__file__).parent
    file_path = (base_path / "df_complete.csv").resolve()
    df_complete = pd.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)
    # df_complete = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)

    #########################prepare data
    source_notna = df_complete['source'].notna()
    sources_ids = df_complete[source_notna]

    id_unique =  sources_ids.drop_duplicates(subset='id1')
    # print(len(id_unique))
    # print(id_unique)

    claim_by_sources_id_unique = id_unique.groupby(['source'])['id1'].size().reset_index(name='counts')
    sizes = []
    labels = []

    for i in range(len(claim_by_sources_id_unique['counts'])):
        sizes.append(claim_by_sources_id_unique['counts'][i])
        labels.append(claim_by_sources_id_unique['source'][i])
    # print(sizes)
    # print(labels)


    ###########################graph to json
    trace = [go.Pie(labels=labels, values=sizes,
                    hoverinfo='label+percent', textinfo='percent',
                    textfont=dict(size=20))]

    piechart_sources_JSON = json.dumps(trace, cls=plotly.utils.PlotlyJSONEncoder)

    # print(piechart_sources_JSON)
    return piechart_sources_JSON
# create_piechart_source()