# Dhaka Weather Forcasting

Using the Weather API I am collecting data from 01 Jan 2023 to 31 May 2023. Here only temperature data is collecting at 120 meters above ground. The website can be found [here.](https://open-meteo.com/en/docs#latitude=23.71&longitude=90.41&hourly=temperature_2m)


Here I used a famous forecasting model named prophet. Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend, and typically handles outliers well.

Prophet is open source software released by Facebook's Core Data Science team. It is available for download on CRAN and PyPI. The models documentation can be found [here.](https://facebook.github.io/prophet/)