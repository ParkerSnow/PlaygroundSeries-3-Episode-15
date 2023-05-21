import numpy as np
from sklearn import model_selection, linear_model, metrics, tree, impute
import numpy
import pandas as pd

data = pd.read_csv('Data/data.csv',index_col='id')
#print(data)

model = impute.KNNImputer(missing_values=np.NAN)

trainData = data[['pressure [MPa]','mass_flux [kg/m2-s]','x_e_out [-]']]

#print(trainData)

model.fit(trainData)
model.set_output(transform='pandas')
finalData = model.transform(trainData)

sample = pd.read_csv('Data/sample_submission.csv')

values = []
ids = []

for i in sample['id']:
    value = finalData.iloc[i]['x_e_out [-]']

    values.append(value)
    ids.append(i)

submission = pd.DataFrame(index=ids,data=values,columns=['x_e_out [-]'])

print(submission)

submission.to_csv('Data/submission.csv',index_label='id')