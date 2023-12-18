import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

click_source_count = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(click_source_count)



ad_clicks['is_click'] = ~ad_clicks\
   .ad_click_timestamp.isnull()

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click'])['user_id'].count().reset_index()

print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
).reset_index()

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot)

AB_count = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(AB_count)

AB_click_compare = ad_clicks.groupby(['experimental_group', 'is_click'])['user_id'].count().reset_index()
print(AB_click_compare)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
print(a_clicks.head())
print(b_clicks.head())

a_clicks_by_day = a_clicks.groupby(['is_click', 'day'])['user_id'].count().reset_index().pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()

b_clicks_by_day = b_clicks.groupby(['is_click', 'day'])['user_id'].count().reset_index().pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
)

a_clicks_by_day['percent_clicked'] = a_clicks_by_day[True] / (a_clicks_by_day[True] + a_clicks_by_day[False])

b_clicks_by_day['percent_clicked'] = b_clicks_by_day[True] / (b_clicks_by_day[True] + b_clicks_by_day[False])

print(a_clicks_by_day)
print(b_clicks_by_day)


print(ad_clicks.head(10))




