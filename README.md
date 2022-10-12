# About Problem

<img src = "https://previews.123rf.com/images/artisticco/artisticco1403/artisticco140300085/26934105-una-ilustraci%C3%B3n-vectorial-de-vendedor-de-coches-dando-la-clave-del-nuevo-coche-al-cliente-en-el-conc.jpg" width = 600>

We collected 6 sets of data from the Kaggle platform on the price of pre-owned or used vehicles. The vehicle manufacturers we collected were the following: Ford,Hyundai,Toyota,Audu,BMW and Mercedez-Benz

## *Features Dataset*

* Manufacturer: Vehicle manufacturers of the respective brands mentioned above.
* Model: Vehicle model.
* Year: Model year of manufacture.
* Mileage : Number of miles traveled by the vehicle.
* EngineSize: Car's Engine Size.



## *What is the price of the vehicle?*

Develop a predictive model that allows estimating the price of brand vehicles: Ford, Toyota, Hyundai, BMW, Audi and Mercedes-Benz.Based on the variables explained above.


## *Important Discoveries*


![mean_price](https://user-images.githubusercontent.com/85312561/190241034-31a3680e-5438-4796-8eea-ca22e077feaf.png)



![mean_price_trasmission](https://user-images.githubusercontent.com/85312561/190241081-3abdc08c-d4e1-406d-a19c-4bbb53572ca3.png)



![matrix_plot](https://user-images.githubusercontent.com/85312561/190241480-67fb4ed6-3a3f-4be8-8750-0ef0ea77d182.png)


### *Conclusion*

The dataset has several outliers for example with the following variables:



* Year: There is a value that has a manufacturing date that is equal to the year 2060. Something that is illogical, it was probably a registry error.


* Mileage: There are vehicles that have a mile traveled, something that is very rare to happen. These observations probably made some modifications to the odometer so that this number of miles traveled would appear. Normally, pre-owned vehicles have at least 3,000 miles of travel with the vehicle as a minimum.



* Those categories that contain a value that is equal to "Other" will have to be eliminated, since they do not add any value to the resolution of the problem.All those categories that present less than 10 times I will choose to eliminate them, since it does not make sense for the model to only learn very specific patterns, it can cause the algorithm to overfit

## Data cleaning



There are vehicle models that are repeated less than 10 times. Therefore, it is better to choose to eliminate them, since they can affect the performance of the model. Since these observations appear very little.



We opted to create several subsets according to the vehicle manufacturer with the purpose of giving a better cleaning to the data, for the price variable. Since it is the variable to estimate.


![unique_values](https://user-images.githubusercontent.com/85312561/187808831-3c54e23e-398b-4c15-8d00-c1b76ad96871.png)



![mileage](https://user-images.githubusercontent.com/85312561/190246548-cd8f83fa-215b-4106-8943-48e3f46490a6.jpeg)


I created a custom Python module that allows me to calculate confidence intervals, in order to remove outliers.

Carry out a similar process for the price variable, with the difference that you use the intervals based on the manufacturer, since the dataset contains high-end car manufacturers.


## *Data Processing*



<img src = "https://forum.huawei.com/enterprise/es/data/attachment/forum/202209/09/233924c426wl254hl4i4a8.png" width = 700>


Nominal character variables, such as the model or the manufacturer, require a transformation called One Hot Encoding. Several dummy variables are created according to the number of these. Where the condition is met, a 1 will be assigned, while the other columns will be filled with a 0.




As results we reach a number of 117 input variables. In addition to having around 86,000 observations. Which the best model that meets these characteristics is the XGBoost. Instead of using a neural network, since using it requires more data sets. XGBoost does not require any kind of scaling, since it applies mathematical inequalities on each estimator.

## *XGBoost*

<img src = "https://miro.medium.com/max/560/1*85QHtH-49U7ozPpmA5cAaw.png">


It is an algorithm that uses other simpler models, generally decision trees. Each tree becomes better according to the proportion of the user's learning rate. A low learning rate allows the greatest use of estimators. 

### *GridSearchCV*

Use GridSearchCV to find the best combination of hyperparameters based on cross-validation, which is a technique that involves doing several random subsamples to find the percentage of generalization.


#### *Final Model*


* max_depth = 10
* n_estimators = 800
* learning_rate = 0.01
* colsample_bytree = 0.7
* subsample = 0.7
* colsample_bynode = 0.8
* reg_alpha = 0.5
* gamma = 20





### *Feature Importance*

![plot_importance](https://user-images.githubusercontent.com/85312561/190239451-6b37359a-26c4-4814-9a88-db3659250169.jpeg)



* If the vehicle has a Manual transmission, the price of the vehicle generally decreases, it is less expensive with an automatic or semi-automatic transmission.
The engine size is a variable that has a lot of weight. Since the greater the capacity, the greater the technical capacity of the car.



* The year of manufacture includes in the price, since if a vehicle of the same model. It will make the price of the car more expensive, since it will be a more recent model.




* Other variables that complement the predictions well is the vehicle brand, since for example it is well known that Mercedes-benz vehicles belong to high-end manufacturers, which means that the price per car is much higher. Also the number of miles traveled, since generally a vehicle with higher mileage has more wear, which causes a devaluation of the car.


## *Production*

Finally, it further develops a practical graphical interface, which allows users to enter new data in a pleasant way. Later, using Streamlit Cloud, we send it to a free server, which allows users to use it,streamlit is a library that allows you to easily create web applications that deal with working with data.

<img src = "https://media.giphy.com/media/Ol4Xhpm6DxlLD4BtKR/giphy.gif" width = 400>

## *Summary*



Apply the data science problem solving methodology, it receives the database with outliers, for which I had to clean it, so that these values do not affect the model.

Later I had to perform the One Hot Encoding transformation for those nominal variables, the resulting dataframe was 117 predictor variables.

Apply the XGBoost model as it works quite well for datasets with many variables and a moderate amount of data instead of applying a neural network.

Apply regularization parameters due to the huge amount of predictor variables, I finally used a tool that allows to search for the best combination of parameters based on cross validation.


Finally save the model and create a web application using Streamlit, with the aim that the user enters data in a comfortable way
