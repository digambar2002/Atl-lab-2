1. Closing price of companies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
# Assuming your dataset is stored in a CSV file named 'your_dataset.csv'
df = pd.read_csv('/content/portfolio_data.csv', parse_dates=True, index_col='Date')

# Set up the style for plots
sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")
%matplotlib inline

# Plot the closing prices of each company
plt.figure(figsize=(14, 7))

for company in df.columns:
    plt.plot(df.index, df[company], label=company)

plt.title('Closing Prices of Tech Companies')
plt.xlabel('Date')
plt.ylabel('Closing Price ($)')
plt.legend()
plt.show()

#2. printing dataset info    (https://www.kaggle.com/datasets/aakarkale/sf-salaries-dataset)
import pandas as pd
salaries = pd.read_csv('/content/SalariesInSanFranciscoDataSet.csv')
salaries.info()

#3. 
import matplotlib.pyplot as plt

# Assuming pays_arrangement is defined here
pays_arrangement = [['BasePay', 'OvertimePay', 'OtherPay'],
                    ['Benefits', 'TotalPay', 'TotalPayBenefits']]

fig, axes = plt.subplots(2, 3)
fig.set_figheight(5)
fig.set_figwidth(12)

for i in range(len(pays_arrangement)):
    for j in range(len(pays_arrangement[i])):
        # pass in axes to pandas hist
        salaries[pays_arrangement[i][j]].hist(ax=axes[i, j])
        axes[i, j].set_title(pays_arrangement[i][j])

# add a row of emptiness between the two rows
plt.subplots_adjust(hspace=1)
# add a row of emptiness between the cols
plt.subplots_adjust(wspace=1)

plt.show()
plt.show()


#4

