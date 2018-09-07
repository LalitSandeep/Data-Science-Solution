
The initial part of the problem which includes data visualization, selection of model, finding accuracy etc. is in the Initial_Model Python Notebook. This Notebook creates a classification model which is stored as saved_model.sav .  

The Python file model_module.py is the module containing  the model and functions required to predict Kickstarter projects' state. This module contains the code for loading the saved model and transforming the test data. This module contains the test() method which is going to be accessed by the external python file testing.py . This module creates a csv file called as kickstarter-predictions which contains IDs and their corresponding 'state' predictions. 

The testing.py gives us an example of how to import and use the module. It calls the test() method of the model_module file. The filename of the test data is stored as test_data.csv . This csv file consists of the test data. Please open it and see to understand the format. It is similar to data.csv file. 

So, in order to test the model, we need to run testing.py to perform testing of data.
















