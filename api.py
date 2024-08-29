
from fastapi import FastAPI

app = FastAPI()

@app.get('/speed-test')
def speed_test():
    return {'result', 'ok'}

