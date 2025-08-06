import pandas as pd
import matplotlib.pyplot as plt

# Data for the chart
data = {
    "Startup": ["Uber", "Airbnb", "Opendoor", "Tesla", "Convoy", "Compass", "Amazon"],
    "Industry": [
        "Taxis & Transport", "Lodging", "Real Estate", "Auto", "Freight/Logistics", "Real Estate", "Retail"
    ],
    "Fragmented Industry": [True, True, True, True, True, True, True],
    "Low NPS": [True, True, True, True, True, True, True],
    "Vertical Integration": [True, True, True, True, True, True, True],
    "Simple, Valuable Product": [True, True, True, True, True, True, True],
}

df = pd.DataFrame(data)

# Display table for better visual context
import caas_jupyter_tools as tools; tools.display_dataframe_to_user(name="Startup Success Formula", dataframe=df)

# Create a chart to visualize it
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')
table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    cellLoc='center',
    loc='center'
)
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)
plt.title("Startups That Followed the Success Formula", fontsize=14, pad=20)
plt.tight_layout()
plt.show()
