# About Problem

We collected 6 sets of data from the Kaggle platform on the price of pre-owned or used vehicles. The vehicle manufacturers we collected were the following: Ford,Hyundai,Toyota,Audu,BMW and Mercedez-Benz

## *Features Dataset*

* Manufacturer: Vehicle manufacturers of the respective brands mentioned above.
* Model: Vehicle model.
* Year: Model year of manufacture.
* Mileage : Number of miles traveled by the vehicle.
* EngineSize: Car's Engine Size
* Tax: Amount of tax per vehicle.
* MPG: Fuel cost miles per gallon


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

It is an algorithm that uses other simpler models, generally decision trees. Each tree becomes better according to the proportion of the user's learning rate. A low learning rate allows the greatest use of estimators. In addition to preventing the model from overfitting training data.It has the additional advantage that the model can be trained using a GPU, accelerating the training speed.




#### *Common Parameters*
* max_depth: Maximum depth of each tree.
* n_estimators: Number of decision trees.
* learning_rate: Room for improvement of each estimator.
* subsample: Number of training samples. Instead of selecting 100% of the data, you can use 80 or 85% of the data. Preventing the model from overfitting the training data

### *Number of Ideal Estimators*

We use the mean square error, which measures the average error between the original value and the predicted one. We evaluate the MSE according to the number of estimators, taking care that the loss function does not only decrease for the training data.Each model proposal is assigned a learning rate of 0.01. In order for the model to generalize better.

![estimators_plot](https://user-images.githubusercontent.com/85312561/187816326-687aa2ce-8adc-423b-a8c4-d3590b2be2b7.png)

Because this last model we assign fewer estimators, because we provide a depth of each tree we use a range of 100 to 500 trees. The training and testing MSE almost go hand in hand. Therefore we can use the maximum amount that we assign to this model. Later we use a function called GridSearchCV that consists of searching for the best combination of parameters based on cross validation. We add the subassembly parameter to the equation where we assign 3 values: [0.80,0.85,0.9].


As a final model of the following combination of parameters:

* max_depth = 8
* learning_rate = 0.01
* n_estimators = 500
* subsample = 0.85

