from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.post('/teste2')
async def root2():
    return {'message': 'Esta e a rota teste-2',
            'propriedade2': 2,
            'data': datetime.now()
            }
