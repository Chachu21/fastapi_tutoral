from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()

# Create a root endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}