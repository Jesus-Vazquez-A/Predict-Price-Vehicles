# About Problem

<img src = "https://previews.123rf.com/images/artisticco/artisticco1403/artisticco140300085/26934105-una-ilustraci%C3%B3n-vectorial-de-vendedor-de-coches-dando-la-clave-del-nuevo-coche-al-cliente-en-el-conc.jpg" width = 600>

We collected 6 sets of data from the Kaggle platform on the price of pre-owned or used vehicles. The vehicle manufacturers we collected were the following: Ford,Hyundai,Toyota,Audu,BMW and Mercedez-Benz

## *Features Dataset*

* Manufacturer: Vehicle manufacturers of the respective brands mentioned above.
* Model: Vehicle model.
* Year: Model year of manufacture.
* Mileage : Number of miles traveled by the vehicle.
* EngineSize: Car's Engine Size.
* Tax: Amount of tax per vehicle.
* MPG: Fuel cost miles per gallon.


## *What is the price of the vehicle?*

Develop a predictive model that allows estimating the price of brand vehicles: Ford, Toyota, Hyundai, BMW, Audi and Mercedes-Benz.Based on the variables explained above.


## *Important Discoveries*

![mean_price](https://user-images.githubusercontent.com/85312561/187807320-c551598b-4eae-4f27-a781-66e90d4d13ed.png)

As can be seen from brands such as Mercedes-Benz, Audi and BMW. They have a higher average price, since they are manufacturers of high-end vehicles.


![matrix plot](https://user-images.githubusercontent.com/85312561/187807773-39d1df0b-e2a0-408f-b1f2-f186d695380e.png)


* Generally between the model is more recent, the price will increase. Since the vehicles are improved over time.
* The more miles the vehicle travels, the price decreases, since the model wears out. As long as it is the same model.
* The engine size positively influences the price of the vehicle. Since the technical section of the vehicles increases.



## Data cleaning

![unique_values](https://user-images.githubusercontent.com/85312561/187808831-3c54e23e-398b-4c15-8d00-c1b76ad96871.png)

There are vehicle models that are repeated less than 10 times. Therefore, it is better to choose to eliminate them, since they can affect the performance of the model. Since these observations appear very little.



We opted to create several subsets according to the vehicle manufacturer with the purpose of giving a better cleaning to the data, for the price variable. Since it is the variable to estimate.



![mpg](https://user-images.githubusercontent.com/85312561/187809290-6a363bdd-e9c4-41ed-98c0-5d7669950e30.png)


We create an upper range for the MPG variable. To find a more exact interval. We decided to calculate it according to the fuel type of the vehicle.
It makes sense that hybrid vehicles have an MPG. Since they rely on their electric motors.We take the largest interval to select all those values that are less than that amount.



## *Data Processing*


Nominal character variables, such as the model or the manufacturer, require a transformation called One Hot Encoding. Several dummy variables are created according to the number of these. Where the condition is met, a 1 will be assigned, while the other columns will be filled with a 0.


As results we reach a number of 119 input variables. In addition to having around 50,000 observations. Which the best model that meets these characteristics is the XGBoost. Instead of using a neural network, since using it requires more data sets. XGBoost does not require any kind of scaling, since it applies mathematical inequalities on each estimator.


## *XGBoost*

<img src = "https://miro.medium.com/max/560/1*85QHtH-49U7ozPpmA5cAaw.png">


It is an algorithm that uses other simpler models, generally decision trees. Each tree becomes better according to the proportion of the user's learning rate. A low learning rate allows the greatest use of estimators. 

In addition to preventing the model from overfitting training data.It has the additional advantage that the model can be trained using a GPU, accelerating the training speed.




#### *Common Parameters*
* max_depth: Maximum depth of each tree.
* n_estimators: Number of decision trees.
* learning_rate: Room for improvement of each estimator.
* subsample: Number of training samples. Instead of selecting 100% of the data, you can use 80 or 85% of the data. Preventing the model from overfitting the training data

### *Number of Ideal Estimators*

We use the mean square error, which measures the average error between the original value and the predicted one.

We evaluate the MSE according to the number of estimators, taking care that the loss function does not only decrease for the training data.Each model proposal is assigned a learning rate of 0.01. In order for the model to generalize better.

![estimators_plot](https://user-images.githubusercontent.com/85312561/187816326-687aa2ce-8adc-423b-a8c4-d3590b2be2b7.png)


We use 100 to 1000 estimators to find the optimal number of trees. According to the maximum depth of the tree, in this way we ensure that the model does not overfit.

### *GridSearchCV*

We rely on the GridSearchCV function that searches for the best combination of parameters according to cross validation. Thanks to this tool we ensure that the model generalizes well.

As a final model of the following combination of parameters:

* max_depth = 7
* learning_rate = 0.01
* n_estimators = 1000
* subsample = 0.85
* gamma = 10

### *Feature Importance*



![plot_importance](https://user-images.githubusercontent.com/85312561/188053598-d9e75b84-7e25-4ce4-8929-8f80722e0c9b.jpeg)


* If the vehicle has a Manual transmission, the price of the vehicle generally decreases, it is less expensive with an automatic or semi-automatic transmission.
The engine size is a variable that has a lot of weight. Since the greater the capacity, the greater the technical capacity of the car.


* The MPG in some countries is the main producer, for the purchase of a vehicle. Since there will be people looking for an economical car in terms of fuel consumption.


* The year of manufacture includes in the price, since if a vehicle of the same model. It will make the price of the car more expensive, since it will be a more recent model.

These are the variables that most influence the model. The other variables can help complement the result.

For example, in this list of the most important variables, the mileage variable does not appear. It is well known that generally a vehicle with more mileage tends to lower the price.


## *Production*

Finally, it further develops a practical graphical interface, which allows users to enter new data in a pleasant way. Later, using Streamlit Cloud, we send it to a free server, which allows users to use it.Streamlit is a library that allows you to easily create web applications that deal with working with data.



# *Summary*


We develop all the processes that require a data science project. We clean the data in order to improve the performance of our model.

We opted to use XGBoost as this algorithm works quite well for moderate data sets. In addition, continuous variables do not require any type of preprocessing and as if that were not enough, it allows training through GPU. This translates to much more efficient training than we would with a CPU.


The created model is used to predict new values, to verify its performance. Since I was sure of its performance, I developed an application for the Artificial Intelligence model. With elin that users can enter data in a better way.
