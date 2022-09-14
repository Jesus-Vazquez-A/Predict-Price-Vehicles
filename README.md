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



* If the vehicle has a Manual transmission, the price of the vehicle generally decreases, it is less expensive with an automatic or semi-automatic transmission.
The engine size is a variable that has a lot of weight. Since the greater the capacity, the greater the technical capacity of the car.



* The year of manufacture includes in the price, since if a vehicle of the same model. It will make the price of the car more expensive, since it will be a more recent model.




* Other variables that complement the predictions well is the vehicle brand, since for example it is well known that Mercedes-benz vehicles belong to high-end manufacturers, which means that the price per car is much higher. Also the number of miles traveled, since generally a vehicle with higher mileage has more wear, which causes a devaluation of the car.


## *Production*

Finally, it further develops a practical graphical interface, which allows users to enter new data in a pleasant way. Later, using Streamlit Cloud, we send it to a free server, which allows users to use it.Streamlit is a library that allows you to easily create web applications that deal with working with data.



# *Summary*


We develop all the processes that require a data science project. We clean the data in order to improve the performance of our model.

We opted to use XGBoost as this algorithm works quite well for moderate data sets. In addition, continuous variables do not require any type of preprocessing and as if that were not enough, it allows training through GPU. This translates to much more efficient training than we would with a CPU.


The created model is used to predict new values, to verify its performance. Since I was sure of its performance, I developed an application for the Artificial Intelligence model. With elin that users can enter data in a better way.
