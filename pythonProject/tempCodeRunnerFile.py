    if data.iloc[i,'B8']<1970:
        line.add_yaxis(series_name="y1线",y_axis=data.iloc[4,2:10], is_smooth=True,symbol_size=1,color='red')
    if data.iloc[i,'B8']>1970 and data.iloc[i,'B8']<1980:
        line.add_yaxis(series_name="y1线",y_axis=data.iloc[4,2:10], is_smooth=True,symbol_size=1,color='black')