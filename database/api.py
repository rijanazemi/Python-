from fastapi import FastAPI

app= FastAPI ()

@app.get("/items/")
def get_items():
    return {"items":["item 1","item 2","item3"]}

@app.get("/items/")
def get_items(name: str, price: float):
    return {"item_name": name , "item_price": price}