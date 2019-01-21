# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.DataFrame()
data = pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace=True)
#print(data)
gender_count = (data['Gender'].value_counts())
#plt.bar(gender_count)
gender_count.plot.barh()

#path of the data file- path

#Code starts here 




# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
l='Character Alignment'
plt.pie(alignment)


# --------------
#Code starts here
import numpy as np

# creating subset of data
sc_df = data[['Strength','Combat']]

sc_covariance = (np.cov(sc_df['Strength'],sc_df['Combat']))[0][1]

sc_strength = np.std(sc_df['Strength'],ddof=1)
print(sc_strength)

sc_combat = np.std(sc_df['Combat'],ddof=1)

sc_pearson = (sc_covariance)/((sc_strength)*(sc_combat))

ic_df = data[['Intelligence','Combat']]

ic_covariance = (np.cov(ic_df['Intelligence'],ic_df['Combat']))[0][1]

ic_intelligence = np.std(ic_df['Intelligence'],ddof=1)
ic_combat = np.std(sc_df['Combat'],ddof=1)

ic_pearson = (ic_covariance)/((ic_intelligence)*(sc_combat))


# --------------
#Code starts here

# calculating toal high
total_high = np.quantile(data['Total'],0.99)

#calculating super_best
super_best = data.loc[data['Total']>total_high]

#identifying super_best_names
super_best_names = list(super_best['Name'])

print(super_best_names)


# --------------
#Code starts here

#Setting up the subplots
fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(20,8))

#Plotting box plot
ax_1.boxplot(super_best['Intelligence'])

#Setting the subplot axis title
ax_1.set(title='Intelligence')


#Plotting box plot
ax_2.boxplot(super_best['Speed'])

#Setting the subplot axis title
ax_2.set(title='Speed')


#Plotting box plot
ax_3.boxplot(super_best['Power'])

#Setting the subplot axis title
ax_3.set(title='Power')

#Code ends here   


