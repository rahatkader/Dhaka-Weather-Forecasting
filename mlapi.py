import uvicorn
import pandas as pd
from fastapi import FastAPI
from prophet.serialize import model_from_json

app = FastAPI()


def predict_temp(date):
    '''
    Change string date to YYYY-MM-DD HH:MM:SS format

    Parameters
    -------------
    date (string): date as string
  
    Return:
    -------------
    return YYYY-MM-DD HH:MM:SS format date
    '''
    with open("model.json", "r") as fin:        # loading model
        model = model_from_json(fin.read())

    predict = list()
    predict.append([date])
    predict = pd.DataFrame(predict)
    predict.columns = ["ds"]
    predict["ds"] = pd.to_datetime(predict["ds"])
    forecast = model.predict(pd.DataFrame.from_dict(predict))
    temp = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    mesg = "Predicted temp = %.2f C, lowest = %.2f C, lowest = %.2f C"%(temp['yhat'], temp['yhat_lower'], temp['yhat_upper'])
    return mesg


@app.get('/{date}')
async def message(date: str):
    return predict_temp(date)



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


# uvicorn mlapi:app --reload
# http://127.0.0.1:8000/docs
# predict_temp('2024-01-01 04:00:00')