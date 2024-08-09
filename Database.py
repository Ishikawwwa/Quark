from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

URI = "neo4j+s://a29346fc.databases.neo4j.io"
AUTH = (os.getenv("GraphDB_username"), os.getenv("GraphDB_password"))

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()