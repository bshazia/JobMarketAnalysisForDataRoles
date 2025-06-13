import pandas as pd

# Load data
df = pd.read_csv("raw_jobs.csv")

# Drop nulls and duplicates
df = df.dropna(subset=["url"]).drop_duplicates("url")


# Skill extraction
skills = ["Excel", "SQL", "Python", "Tableau", "Power BI", "Pandas", "R", "Git","Azure","AWS","GCP","AI"]
for skill in skills:
    df[skill] = df["description"].str.contains(fr"\b{skill}\b", case=False, na=False)

# Count how many skills appear
df["skill_count"] = df[skills].sum(axis=1)

# Save to new CSV
df.to_csv("clean_jobs.csv", index=False)