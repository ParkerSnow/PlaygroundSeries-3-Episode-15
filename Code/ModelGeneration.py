import numpy as np
from sklearn import model_selection, linear_model, metrics, tree, impute
import numpy
import pandas as pd

data = pd.read_csv('Data/data.csv',index_col='id')
#print(data)

model = impute.SimpleImputer(missing_values=np.NAN, strategy='mean')

trainData = data[['pressure [MPa]','mass_flux [kg/m2-s]','x_e_out [-]']]

#print(trainData)

model.fit(trainData)
model.set_output(transform='pandas')
finalData = model.transform(trainData)
print(finalData)
sample = pd.read_csv('Data/sample_submission.csv')

for i in sample['id']:
    #print(i)
    row = finalData.iloc(i)
    print(row['mass_flux [kg/m2-s]'])
sumbission = pd.DataFrame(index=sample['id'])



