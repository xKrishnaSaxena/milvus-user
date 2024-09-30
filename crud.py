import hashlib
from pymilvus import Collection, FieldSchema, CollectionSchema, DataType, connections, utility

class MilvusUserAgent:
    def __init__(self):
     
        connections.connect("default", host="127.0.0.1", port="19530")

    def create_user_db(self, collection_name="user_collection"):
      
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True),  
            FieldSchema(name="username", dtype=DataType.VARCHAR, max_length=100),  
            FieldSchema(name="email", dtype=DataType.VARCHAR, max_length=100),  
            FieldSchema(name="password", dtype=DataType.VARCHAR, max_length=64), 
            FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=128)  
        ]
        schema = CollectionSchema(fields)
        collection = Collection(name=collection_name, schema=schema)
        index_params = {
        "index_type": "IVF_FLAT",
        "metric_type": "L2",
        "params": {"nlist": 128}
    }
        collection.create_index("vector", index_params)
        return f"User collection {collection_name} created."

    def insert_user(self, collection_name, user_id, username, email, password, vector):
       
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

      
        collection = Collection(name=collection_name)

      
        user_data = [
            [user_id],     
            [username],        
            [email],           
            [hashed_password], 
            [vector]          
        ]
        collection.insert(user_data)
        return f"User {username} inserted into {collection_name}."

    def update_user(self, collection_name, user_id, username=None, email=None, password=None, vector=None):
        collection = Collection(name=collection_name)

 
        expr = f"id == {user_id}"
        collection.delete(expr)

    
        updated_user = {
        'id': user_id,
        'username': username or '', 
        'email': email or '',
        'password': hashlib.sha256(password.encode()).hexdigest() if password else '',
        'vector': vector if vector else [0] * 128
    }

        collection.insert([
        [updated_user['id']],
        [updated_user['username']],
        [updated_user['email']],
        [updated_user['password']],
        [updated_user['vector']]
    ])
        return f"User {user_id} updated in {collection_name}."


    def search_user_by_vector(self, collection_name, vector):
      
        collection = Collection(name=collection_name)
        collection.load()

        search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
        results = collection.search([vector], "vector", search_params, limit=5)
        return results

    def delete_user(self, collection_name, user_id):
      
        collection = Collection(name=collection_name)
        expr = f"id == {user_id}"
        collection.delete(expr)
        return f"User with id {user_id} deleted from {collection_name}."

    def list_collections(self):
      
        collections = utility.list_collections()
        return collections

    def retrieve_user(self, collection_name, user_id):
     
        collection = Collection(name=collection_name)
        collection.load()
        expr = f"id == {user_id}"
        results = collection.query(expr=expr)
        return results
