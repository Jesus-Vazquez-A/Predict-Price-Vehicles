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


It makes sense that hybrid vehicles have an MPG. Since they rely on their electric motors.

