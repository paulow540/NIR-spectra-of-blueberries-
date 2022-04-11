import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded = pickle.load(open("DATA VONCK ET AL 2020.sav", 'rb'))


# creating a function for prediction

def data_vonck(input):
    inputdata = (1,2,0,1)
    inputdatasnumpy = np.asarray(inputdata)
    inputdatares = inputdatasnumpy.reshape(1, -1)
    pred = loaded.predict(inputdatares)
    print(pred)

    if pred[0]== 1:
        return "the taste of the blueberries is sweet"
    elif pred[0] == 2:
        return "the taste of the blueberries is neutral"
    elif pred[0] == 3:
        return "the taste of the blueberries is lightly sour"
    else: 
        return "the taste of the blueberries is sour"
            
def main():
    
    # Sample_number	Measuring_side	Device_number	Replicate_number
    #giving a title
    st.title("DATA VONCK ET AL 2020 APP")
    
    # getting the input data
    Sample_number = st.text_input("Number of Sample")
    Measuring_side = st.text_input("Number of Measuring side")
    Device_number = st.text_input("Number of Device ")
    Replicate_number = st.text_input("Number of Replicate")
    
    #code for prediction
    
    data_work = ''
    
    #creating  a button for prediction
    
    if st.button("Data vonck"):
        data_work = data_vonck([Sample_number, Measuring_side, Device_number, Replicate_number])
    
    st.success(data_work)
    

if __name__ == '__main__':
    main()