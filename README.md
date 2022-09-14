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






## *Data Processing*


Nominal character variables, such as the model or the manufacturer, require a transformation called One Hot Encoding. Several dummy variables are created according to the number of these. Where the condition is met, a 1 will be assigned, while the other columns will be filled with a 0.


As results we reach a number of 119 input variables. In addition to having around 50,000 observations. Which the best model that meets these characteristics is the XGBoost. Instead of using a neural network, since using it requires more data sets. XGBoost does not require any kind of scaling, since it applies mathematical inequalities on each estimator.


## *XGBoost*

<img src = "https://miro.medium.com/max/560/1*85QHtH-49U7ozPpmA5cAaw.png">


It is an algorithm that uses other simpler models, generally decision trees. Each tree becomes better according to the proportion of the user's learning rate. A low learning rate allows the greatest use of estimators. 

In addition to preventing the model from overfitting training data.It has the additional advantage that the model can be trained using a GPU, accelerating the training speed.





### *GridSearchCV*

We rely on the GridSearchCV function that searches for the best combination of parameters according to cross validation. Thanks to this tool we ensure that the model generalizes well.

As a final model of the following combination of parameters:

* max_depth = 7
* learning_rate = 0.01
* n_estimators = 1000
* subsample = 0.85
* gamma = 10

### *Feature Importance*

![plot_importance](https://user-images.githubusercontent.com/85312561/190239451-6b37359a-26c4-4814-9a88-db3659250169.jpeg)




## *Production*

Finally, it further develops a practical graphical interface, which allows users to enter new data in a pleasant way. Later, using Streamlit Cloud, we send it to a free server, which allows users to use it.Streamlit is a library that allows you to easily create web applications that deal with working with data.



# *Summary*


We develop all the processes that require a data science project. We clean the data in order to improve the performance of our model.

We opted to use XGBoost as this algorithm works quite well for moderate data sets. In addition, continuous variables do not require any type of preprocessing and as if that were not enough, it allows training through GPU. This translates to much more efficient training than we would with a CPU.


The created model is used to predict new values, to verify its performance. Since I was sure of its performance, I developed an application for the Artificial Intelligence model. With elin that users can enter data in a better way.
