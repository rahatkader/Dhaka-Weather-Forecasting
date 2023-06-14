# Dhaka Weather Forcasting

## **Introduction**

In this repository, a forecasting model is trained using facebook prophet and also the model's API is created using fastapi. The model can predict temperature of Dhaka, Bangladesh for given date.


## **Dataset**

Using the Weather API I am collecting data from 01 Jan 2023 to 31 May 2023. Here only temperature data is collecting at 120 meters above ground. The website can be found [here.](https://open-meteo.com/en/docs#latitude=23.71&longitude=90.41&hourly=temperature_2m)


## **Model**

Here I used a famous forecasting model named prophet. Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend, and typically handles outliers well.


Prophet is open source software released by Facebook's Core Data Science team. It is available for download on CRAN and PyPI. The models documentation can be found [here.](https://facebook.github.io/prophet/)


## **Environment Setup**

First clone the github repo in your local or server machine by following:

```
git clone https://github.com/rahatkader/Dhaka-Weather-Forecasting.git
```

Change the working directory to project root directory. Use Pip to create a new environment and install dependency from `requirement.txt` file. The following command will install the packages according to the configuration file `requirement.txt`.

```
pip install -r requirements.txt
```

Now run mlapi.py

```
python mlapi.py
```

After that open your browser and go to  http://127.0.0.1:8000/docs link. Then follow the below steps:


![Alternate text](/readme/step1.png)
![Alternate text](/readme/step2.png)
![Alternate text](/readme/step3.png)
![Alternate text](/readme/step4.png)

