import uvicorn
from bson import ObjectId
from fastapi import FastAPI, HTTPException
from app.management import Management

app = FastAPI()

@app.get("/get_data_processed")
def get_data():
    try:
        manager = Management()
        df = manager.get_data_processed()
        records = df.to_dict(orient="records")

        for rec in records:
            for k, v in rec.items():
                if isinstance(v, ObjectId):
                    rec[k] = str(v)
        return records
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)











