def get_fullname(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_fullname(first_name="john", last_name="doe"))

from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get('/items/')
def read_items():
    return {"Items":["Item1,""Item2","Item3" ]}



@app.get('/items/{item_id}')
def get_item(item_id: int):
    return{'item_id': item_id}

@app.get('/items/{user_id}')
def get_user(user_id: int):
    return{'user_id': user_id, 'name': 'John Doe'}

