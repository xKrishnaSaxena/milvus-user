from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crud import MilvusUserAgent
from pymilvus import MilvusException

app = FastAPI()
milvus_agent = MilvusUserAgent()
print(milvus_agent.create_user_db())
class User(BaseModel):
    username: str
    email: str
    password: str
    vector: list[float]

@app.post("/register")
async def register_user(user: User):
    try:
        user_id = 1
        result = milvus_agent.insert_user("user_collection", user_id, user.username, user.email, user.password, user.vector)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/update/{user_id}")
async def update_user(user_id: int, user: User):
    try:
        result = milvus_agent.update_user("user_collection", user_id, username=user.username, email=user.email, password=user.password, vector=user.vector)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from fastapi import HTTPException
from pymilvus import MilvusException

@app.post("/search")
async def search_user(user_vector: list[float]):
    try:
       
        results = milvus_agent.search_user_by_vector("user_collection", user_vector)
        
       
        serialized_results = []
        
        for hits in results:
            for hit in hits: 
                serialized_hit = {
                    "id": hit.id,  
                    "distance": hit.distance,
                }
                serialized_results.append(serialized_hit)

        
        full_user_data = []
        for result in serialized_results:
            user_id = result["id"]
            user_data = milvus_agent.retrieve_user("user_collection", user_id)
            result.update(user_data[0])  
            full_user_data.append(result)
        
        
        return {"results": full_user_data}

    except MilvusException as e:
        raise HTTPException(status_code=500, detail=f"Milvus Error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/retrieve/{user_id}")
async def retrieve_user(user_id: int):
    try:
        result = milvus_agent.retrieve_user("user_collection", user_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete/{user_id}")
async def delete_user(user_id: int):
    try:
        result = milvus_agent.delete_user("user_collection", user_id)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


