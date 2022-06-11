from typing import Union
from fastapi import FastAPI
from dataclasses import dataclass
# run uvicorn main:app --reload

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/init_board/")
async def read_root(n: int = 2):
    return (init_board(n).dict)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


class init_board:
    def __init__(self, n):
        self.n = n
        self.board = [[False for i in range(n)] for i in range(self.n)]
        self.dict = {'board': self.board}