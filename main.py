from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "L'API fonctionne !"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    return {"received_data": data}
