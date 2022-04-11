import numpy as np
import pickle 

# loading the saved model
loaded = pickle.load(open("DATA VONCK ET AL 2020.sav", 'rb'))

inputdata = (1,2,0,1)
inputdatasnumpy = np.asarray(inputdata)
inputdatares = inputdatasnumpy.reshape(1, -1)
pred = loaded.predict(inputdatares)
print(pred)

if pred[0]== 1:
    print("the taste of the blueberries is sweet")
elif pred[0] == 2:
     print("the taste of the blueberries is neutral")
elif pred[0] == 3:
     print("the taste of the blueberries is lightly sour")
else: 
     print("the taste of the blueberries is sour")
        