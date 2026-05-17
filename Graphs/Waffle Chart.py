import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

df_can = pd.read_csv(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv'
)

df_can.set_index('Country', inplace=True)

# create dataframe for three countries
df_dsn = df_can.loc[['Denmark', 'Norway', 'Sweden']]
print("\nNew DataFrame:\n", df_dsn)

# proportions
total_values = df_dsn['Total'].sum()
category_proportions = df_dsn['Total'] / total_values

print(pd.DataFrame({"Category Proportion": category_proportions}))

# waffle dimensions
width = 50
height = 15

total_num_tiles = width * height
print("\nThe total number of tiles is:", total_num_tiles)

# tiles per category
tiles_per_category = (category_proportions * total_num_tiles).round().astype(int)

print("\nThe total number of tiles per category is:\n", tiles_per_category)

# initialize chart
waffle_chart = np.zeros((height, width), dtype=np.uint)

category_index = 0
tile_index = 0

# populate waffle chart
for col in range(width):
    for row in range(height):

        tile_index += 1

        if tile_index > sum(tiles_per_category[0:category_index]):
            category_index += 1

        waffle_chart[row, col] = category_index

print("\nWaffle Chart is populated!\n")

# plot
fig = plt.figure(figsize=(12, 6))
fig.suptitle(
    'Immigration to Canada from Denmark, Norway & Sweden',
    fontsize=18,
)

colormap = plt.cm.coolwarm
plt.matshow(waffle_chart, cmap=colormap, fignum=fig.number)
plt.colorbar()

# axis
ax = plt.gca()

# minor ticks
ax.set_xticks(np.arange(-0.5, width, 1), minor=True)
ax.set_yticks(np.arange(-0.5, height, 1), minor=True)

# gridlines
ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

plt.xticks([])
plt.yticks([])

# legend
values_cumsum = np.cumsum(df_dsn['Total'])
total_values = values_cumsum.iloc[-1]

legend_handles = [
    mpatches.Patch(
        color=colormap(float(cumsum) / total_values),
        label=f"{cat} ({total})"
    )
    for cat, total, cumsum in zip(
        df_dsn.index,
        df_dsn['Total'],
        values_cumsum
    )
]

plt.legend(
    handles=legend_handles,
    loc='lower center',
    ncol=len(df_dsn.index.values),
    bbox_to_anchor=(0., -0.2, 1, .1)
)
plt.show()