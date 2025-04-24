# db.py
from pymongo import MongoClient

# Conexión a MongoDB Atlas o local
MONGO_URI = "mongodb+srv://myAtlasDBUser:qwX9pqzhveRmwD8T@avicoladb.rkhdtqs.mongodb.net/?retryWrites=true&w=majority&appName=avicoladb"  
client = MongoClient(MONGO_URI)

# Selección de la base de datos
db = client['avicoladb']

# Colecciones (tablas en NoSQL)
stock_collection = db['stock']

