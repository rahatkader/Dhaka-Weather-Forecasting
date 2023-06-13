import uvicorn
import pandas as pd
from fastapi import FastAPI
from prophet.serialize import model_to_json, model_from_json
from pydantic import BaseModel


class weather(BaseModel):
    input_date: str


# loading model
with open("model.json", "r") as fin:
    model = model_from_json(fin.read())

app = FastAPI()


@app.post("/")
async def predict_weather(data: weather):
    # future = list()
    # future.append([data])
    # future = pd.DataFrame(future)
    # future.columns = ["ds"]
    # future["ds"] = pd.to_datetime(future["ds"])
    # forecast = model.predict(pd.DataFrame.from_dict(future))
    # prediction = forecast[["yhat"]]
    # temp = float(prediction["yhat"])
    return {"message": data}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


# (mlapi) PS E:\Github\Dhaka-Weather-Forecasting> uvicorn mlapi:app --reload
