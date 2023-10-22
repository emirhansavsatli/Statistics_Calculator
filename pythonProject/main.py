import pandas as pd
import matplotlib.pyplot as plt
import statistics

data = {
    'Number of sales': ['0-2', '2-4', '4-6', '6-8', '8-10'],
    'Number of real estate brokers': [16, 25, 13, 4, 2]
}

df = pd.DataFrame(data)

print(df)

mean = statistics.mean(df["Number of real estate brokers"])

mode = statistics.mode(df["Number of real estate brokers"])

median = statistics.median(df["Number of real estate brokers"])

std_dev = statistics.stdev(df['Number of real estate brokers'])


print(f"Mean: {mean}")
print(f"Mode: {mode}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")


import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Number of sales': ['0-2', '2-4', '4-6', '6-8', '8-10'],
    'Number of real estate brokers': [16, 25, 13, 4, 2]
}

df = pd.DataFrame(data)

# Sınıf sınırlarını
df['Lower Bound'] = df['Number of sales'].apply(lambda x: int(x.split('-')[0]))
df['Upper Bound'] = df['Number of sales'].apply(lambda x: int(x.split('-')[1]))

# Göreceli frekansları
frequency_distribution = df[['Number of sales', 'Number of real estate brokers']].copy()
frequency_distribution.columns = ['Interval', 'Frequency']

total_count = frequency_distribution['Frequency'].sum()
frequency_distribution['Relative Frequency'] = frequency_distribution['Frequency'] / total_count

# Subplot
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Frequency
axes[0].bar(frequency_distribution['Interval'], frequency_distribution['Frequency'], width=1.5)
axes[0].set_xlabel('Sınıf Aralığı')
axes[0].set_ylabel('Frekans')
axes[0].set_title('Frequency Distribution')

# Relative Frequency
axes[1].bar(frequency_distribution['Interval'], frequency_distribution['Relative Frequency'], width=1.5)
axes[1].set_xlabel('Sınıf Aralığı')
axes[1].set_ylabel('Göreceli Frekans')
axes[1].set_title('Relative Frequency Histogram')

# Relative Cumulative Frequency
cumulative_frequency = frequency_distribution['Frequency'].cumsum()
relative_cumulative_frequency = cumulative_frequency / total_count

axes[2].plot(frequency_distribution['Interval'], relative_cumulative_frequency, marker='o')
axes[2].set_xlabel('Sınıf Aralığı')
axes[2].set_ylabel('Göreceli Kumulatif Frekans')
axes[2].set_title('Relative Cumulative Frequency Curve')

plt.tight_layout()
plt.show()

