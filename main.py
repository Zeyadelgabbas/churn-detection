from fastapi import FastAPI , HTTPException , Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
import uvicorn
from utils.config import APP_NAME , VERSION , SECRET_KEY_TOKEN
from utils.prediction import predict_new
from utils.validation import CustomerData

app = FastAPI(title=APP_NAME,version=VERSION)
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

api_key_header = APIKeyHeader(name='X-API-Key')
async def verify_api_key(api_key:str = Depends(api_key_header)):
    if api_key != SECRET_KEY_TOKEN:
        raise HTTPException(status_code=403 , detail='Not authorized !')
    return api_key
@app.get("/",tags=['Home'])
def home():
    return {"message": f"welcome to {APP_NAME} API v: {VERSION}"}

@app.post("/predictions",tags=['Model'])
async def predict_models(data:CustomerData,api_key: str = Depends(verify_api_key)) ->dict:
    try:
        prediction =predict_new(data)
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
    return prediction

if __name__ == "__main__":
    uvicorn.run(
        "main:app",           
        host="0.0.0.0",     
        port=8000,
        reload=True           
    )
