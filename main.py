from ml_model import Model
from fastapi import FastAPI
from data_model import DataModel
import pandas as pd
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
   return {"Hello": "World"}

@app.post("/fit")
def fit(data: list[DataModel]):
   data = pd.DataFrame(data)
   model = Model()
   result = model.fit(data)
   return result

@app.post("/predict")
def make_predictions(dataModel: list[DataModel]):
   model = Model()
   resultList = list()
   for element in dataModel:
      df = pd.DataFrame(element.dict(), columns=element.dict().keys(), index=[0])
      df.columns = element.columns()
      result = model.predict(df)
      resultList.append(result[0])
   return {"results": resultList }

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=6969)