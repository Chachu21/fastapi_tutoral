from fastapi import FastAPI

# create an instance of the fastapi application
app = FastAPI()

items=[]

@app.get("/")
async def read_root():
    return {"Hello": "World", "message": "Welcome to the FastAPI application!"}

#get all items
@app.get("/items/")
async def read_items():
    return items

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str = None):
    print(f"Received item_id: {item_id}, query: {q}")
    return {
        "item_id": item_id,
        "q": q
    }

@app.post("/items/")
async def create_item(item: dict):
    print(f"creating item : {item}")
    items.append(item)
    print(f"Current items: {items}")
    return  item

# update the item by id
@app.put("items/{item_d}")
async def update_item(item_id: int, item: dict):
    print(f"updating item id: {item_id} with data: {item}")
    if 0<= item_id < len(items):
        items[item_id] = item
        print(f"Item updated. Current items: {items}")
        return item
    
    return {"error": "Item not found"}
