import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------------------
# Load Data
# ---------------------------------------
df = pd.read_csv("road_accidents.csv")

# ---------------------------------------
# GRAPH 1: Year-wise Accidents Trend
# ---------------------------------------
yearly = df.groupby("Year")["Accidents"].sum()

print("- Fig: 1 shows Road accidents are increasing over years.")
plt.figure()
plt.plot(yearly.index, yearly.values, marker='o', linewidth=3)
plt.title("Fig:1 - Year-wise Road Accident Trend in India", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Number of Accidents")
plt.grid(True)
plt.show()


# ---------------------------------------
# GRAPH 2: Accident vs Death Comparison
# ---------------------------------------
comparison = df.groupby("Year")[["Accidents", "Persons_Killed"]].sum()

comparison.plot(kind="bar", width=0.8)
plt.title("Comparison of Accidents vs Deaths (India)", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

# ---------------------------------------
# GRAPH 3: Top 5 Accident Prone States
# ---------------------------------------
top_states = df.groupby("State")["Accidents"].sum().sort_values(ascending=False).head(5)

print("- Fig:2 shows States contributing major accident in India.")
plt.figure()
sns.barplot(y=top_states.values, x=top_states.index)
plt.title("Fig:2 - Accident Prone States in India", fontsize=14)
plt.xlabel("Total Accidents")
plt.ylabel("State")
plt.show()

# ---------------------------------------
# GRAPH 4: Death Proportion by Vehicle Type
# ---------------------------------------
vehicle_deaths = df.groupby("Vehicle_Type")["Persons_Killed"].sum()

print("- Fig:3 shows Two-wheelers have highest fatality rate.")
plt.figure()
plt.pie(vehicle_deaths, labels=vehicle_deaths.index, autopct='%1.1f%%', startangle=140)
plt.title("Proportion of Deaths by Vehicle Type", fontsize=14)
plt.show()

# ---------------------------------------
# GRAPH 5: Cause-wise Accident Distribution
# ---------------------------------------
cause_data = df["Cause"].value_counts()

print("- Fig:4 shows Speeding is the dominant cause of accidents.")
plt.figure()
sns.barplot(x=cause_data.index, y=cause_data.values)
plt.title("Cause-wise Road Accidents in India", fontsize=14)
plt.xlabel("Cause")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=0)
plt.show()


# ---------------------------------------
# GRAPH 6: Fatality Rate Analysis
# ---------------------------------------
df["Fatality_Rate"] = (df["Persons_Killed"] / df["Accidents"]) * 100

fatality_state = df.groupby("State")["Fatality_Rate"].mean().sort_values(ascending=False)

plt.figure()
sns.barplot(y=fatality_state.values, x=fatality_state.index)
plt.title("Average Fatality Rate (%) by State", fontsize=14)
plt.xlabel("Fatality Rate (%)")
plt.ylabel("State")
plt.show()
