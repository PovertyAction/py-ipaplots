"""
Demo script showing all ipaplots style capabilities.
Recreates the plots from the original Stata test file using the actual test data.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path
import sys

# Add parent directory to path to import ipaplots
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
import ipaplots

# Use the ipaplots style
plt.style.use("ipaplots")

# Create output directory
output_dir = Path(__file__).parent / "output"
output_dir.mkdir(exist_ok=True)

# Load the actual Stata test data
data_path = Path(__file__).parent / "data" / "ipaplots_test_data.dta"
df = pd.read_stata(data_path)

# Extract variables from the dataframe
var1 = df["var1"].values
var2 = df["var2"].values
var3 = df["var3"].values
var4 = df["var4"].values
var5 = df["var5"].values
group = df["group"]  # Keep as pandas Series for easier handling
date = pd.to_datetime(df["date"])

# Extract density variables if they exist
if "den1x" in df.columns:
    den1x = df["den1x"].values
    den1d = df["den1d"].values
    gen2x = df["gen2x"].values
    gen2d = df["gen2d"].values
    gen3x = df["gen3x"].values
    gen3d = df["gen3d"].values
else:
    # Generate density data if not in dataset
    x1 = np.linspace(-4, 4, 100)
    den1x = x1
    den1d = np.exp(-(x1**2) / 2) / np.sqrt(2 * np.pi)
    gen2x = x1
    gen2d = np.exp(-((x1 - 1) ** 2) / 2) / np.sqrt(2 * np.pi)
    gen3x = x1
    gen3d = np.exp(-((x1 + 1) ** 2) / 2) / np.sqrt(2 * np.pi)

# 1. Scatter plot
plt.figure(figsize=(6, 4))
plt.scatter(var5, var2)
plt.title("Scatter plot")
plt.xlabel("var5")
plt.ylabel("var2")
plt.text(
    0.5,
    -0.15,
    "Elaboration: Innovations for Poverty Action (IPA)",
    ha="center",
    va="top",
    transform=plt.gca().transAxes,
    fontsize=8,
)
plt.tight_layout()
plt.savefig(output_dir / "scatter_plot.png", dpi=150, bbox_inches="tight")
plt.close()

# 2. Line graph
plt.figure(figsize=(6, 4))
# Use first 5 groups
for i, g in enumerate(["Group1", "Group2", "Group3", "Group4", "Group5"]):
    mask = group == g
    if mask.any():
        # Sort by date for proper line plotting
        date_masked = date[mask]
        var2_masked = var2[mask]
        sorted_idx = date_masked.argsort()
        plt.plot(
            date_masked.iloc[sorted_idx], var2_masked[sorted_idx], label=f"group{i + 1}"
        )
plt.title("Line plot")
plt.xlabel("Date")
plt.ylabel("var2")
plt.legend()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(rotation=45)
plt.text(
    0.5,
    -0.25,
    "Elaboration: Innovations for Poverty Action (IPA)",
    ha="center",
    va="top",
    transform=plt.gca().transAxes,
    fontsize=8,
)
plt.tight_layout()
plt.savefig(output_dir / "line_graph.png", dpi=150, bbox_inches="tight")
plt.close()

# 3. Pie chart
plt.figure(figsize=(6, 4))
# Use first 5 groups
first_five_groups = ["Group1", "Group2", "Group3", "Group4", "Group5"]
mask = group.isin(first_five_groups)
# Sum of var1 for each group (as per Stata code)
pie_data = []
for g in first_five_groups:
    pie_data.append(df[df["group"] == g]["var1"].sum())
plt.pie(
    pie_data,
    labels=["group1", "group2", "group3", "group4", "group5"],
    autopct="%1.1f%%",
    startangle=90,
)
plt.title("Pie plot")
plt.text(
    0.5,
    -0.15,
    "Elaboration: Innovations for Poverty Action (IPA)",
    ha="center",
    va="top",
    transform=plt.gca().transAxes,
    fontsize=8,
)
plt.tight_layout()
plt.savefig(output_dir / "pie_chart.png", dpi=150, bbox_inches="tight")
plt.close()

# 4. Box plot
plt.figure(figsize=(6, 4))
data_box = [
    var1[~np.isnan(var1)],
    var2[~np.isnan(var2)],
    var3[~np.isnan(var3)],
    var4[~np.isnan(var4)],
    var5[~np.isnan(var5)],
]
plt.boxplot(data_box, tick_labels=["var1", "var2", "var3", "var4", "var5"])
plt.title("Box plot")
plt.ylabel("Values")
plt.text(
    0.5,
    -0.15,
    "Elaboration: Innovations for Poverty Action (IPA)",
    ha="center",
    va="top",
    transform=plt.gca().transAxes,
    fontsize=8,
)
plt.tight_layout()
plt.savefig(output_dir / "box_plot.png", dpi=150, bbox_inches="tight")
plt.close()

# 5. Histogram
plt.figure(figsize=(6, 4))
var3_clean = var3[~np.isnan(var3)]
plt.hist(
    var3_clean,
    bins=20,
    edgecolor="white",
    weights=np.ones_like(var3_clean) / len(var3_clean) * 100,
)
plt.title("Histogram")
plt.xlabel("var3")
plt.ylabel("Percent")
plt.text(
    0.5,
    -0.15,
    "Elaboration: Innovations for Poverty Action (IPA)",
    ha="center",
    va="top",
    transform=plt.gca().transAxes,
    fontsize=8,
)
plt.tight_layout()
plt.savefig(output_dir / "histogram.png", dpi=150, bbox_inches="tight")
plt.close()

# 6. Horizontal bar graph
plt.figure(figsize=(6, 4))
means = [
    np.nanmean(var1),
    np.nanmean(var2),
    np.nanmean(var3),
    np.nanmean(var4),
    np.nanmean(var5),
]
y_pos = np.arange(len(means))
bars = plt.barh(y_pos, means)
plt.yticks(y_pos, ["var1", "var2", "var3", "var4", "var5"])
plt.xlabel("Values")
plt.title("Bar graph")
# Add value labels on bars
for i, (bar, value) in enumerate(zip(bars, means)):
    plt.text(
        bar.get_width() + 10,
        bar.get_y() + bar.get_height() / 2,
        f"{value:.2f}",
        va="center",
    )
max_mean = max(means) if means else 1000
plt.xlim(0, max_mean * 1.2)  # Dynamic xlim based on data
plt.text(
    0.5,
    -0.15,
    "Elaboration: Innovations for Poverty Action (IPA)",
    ha="center",
    va="top",
    transform=plt.gca().transAxes,
    fontsize=8,
)
plt.tight_layout()
plt.savefig(output_dir / "hbar.png", dpi=150, bbox_inches="tight")
plt.close()

# 7. Density plot (area plots)
plt.figure(figsize=(6, 4))
plt.fill_between(den1x, den1d, alpha=0.5, label="density1")
plt.fill_between(gen2x, gen2d, alpha=0.5, label="density2")
plt.fill_between(gen3x, gen3d, alpha=0.5, label="density3")
plt.title("Density plots")
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.text(
    0.5,
    -0.15,
    "Elaboration: Innovations for Poverty Action (IPA)",
    ha="center",
    va="top",
    transform=plt.gca().transAxes,
    fontsize=8,
)
plt.tight_layout()
plt.savefig(output_dir / "density.png", dpi=150, bbox_inches="tight")
plt.close()

# 8. Range graphs (error bars)
plt.figure(figsize=(6, 4))
for i, g in enumerate(["Group1", "Group2"]):
    mask = group == g
    if mask.any():
        # Get sorted subset for clarity
        sorted_idx = date[mask].argsort()
        dates_g = date[mask].iloc[sorted_idx][:20]
        var2_g = var2[mask][sorted_idx][:20]
        var3_g = var3[mask][sorted_idx][:20]
        lower = np.minimum(var2_g, var3_g)
        upper = np.maximum(var2_g, var3_g)
        plt.errorbar(
            dates_g,
            (lower + upper) / 2,
            yerr=(upper - lower) / 2,
            fmt="o-",
            capsize=5,
            label=f"group{i + 1}",
        )
plt.title("Range plots")
plt.xlabel("Date")
plt.ylabel("Values")
plt.legend()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(rotation=45)
plt.text(
    0.5,
    -0.25,
    "Elaboration: Innovations for Poverty Action (IPA)",
    ha="center",
    va="top",
    transform=plt.gca().transAxes,
    fontsize=8,
)
plt.tight_layout()
plt.savefig(output_dir / "range_graphs.png", dpi=150, bbox_inches="tight")
plt.close()

# 9. By graphs (subplots)
fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
fig.suptitle("By graphs")

for i, g in enumerate(["Group1", "Group2"]):
    mask = group == g
    if mask.any():
        axes[i].boxplot([var1[mask]], tick_labels=["var1"])
        axes[i].set_title(f"group = {i + 1}")
        axes[i].set_ylabel("Values" if i == 0 else "")

plt.text(
    0.5,
    -0.05,
    "Elaboration: Innovations for Poverty Action (IPA)",
    ha="center",
    va="top",
    transform=fig.transFigure,
    fontsize=8,
)
plt.tight_layout()
plt.savefig(output_dir / "bygraphs.png", dpi=150, bbox_inches="tight")
plt.close()

print("All plots have been generated in the 'output' directory!")
print("\nPlot types created:")
print("1. scatter_plot.png - Basic scatter plot")
print("2. line_graph.png - Multi-group line plot")
print("3. pie_chart.png - Pie chart with percentages")
print("4. box_plot.png - Box plot for multiple variables")
print("5. histogram.png - Histogram with percentage scale")
print("6. hbar.png - Horizontal bar chart with value labels")
print("7. density.png - Overlapping density plots")
print("8. range_graphs.png - Range plots with error bars")
print("9. bygraphs.png - Grouped box plots (by graphs)")
