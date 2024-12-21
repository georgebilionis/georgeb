import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


#2.1
planets = sns.load_dataset('planets')

plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(
    data=planets,
    x='orbital_period', 
    y='mass', 
    hue='method', 
    palette='viridis', 
    alpha=0.7
)

plt.xscale('log')
plt.yscale('log')

plt.title('Orbital Period vs. Mass', fontsize=16)
plt.xlabel('Orbital Period (days) [log scale]', fontsize=12)
plt.ylabel('Mass (Jupiter masses) [log scale]', fontsize=12)
plt.legend(title='Discovery Method', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()


#2.2
planets = sns.load_dataset('planets')

planets_cleaned = planets.dropna(subset=['year', 'method'])

counts = planets_cleaned.groupby(['year', 'method']).size().reset_index(name='count')

pivot_table = counts.pivot(index='year', columns='method', values='count').fillna(0)

pivot_table.plot(
    kind='bar',
    stacked=True,
    figsize=(12, 8),
    colormap='viridis',
    alpha=0.8
)
plt.title('Exoplanet Discoveries by Year and Method', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Exoplanets Discovered', fontsize=12)
plt.legend(title='Discovery Method', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()

plt.show()