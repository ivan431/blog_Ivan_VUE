from fastapi import FastAPI
import uvicorn 
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import sqlite3
from typing import List

app = FastAPI()

app.mount("/static", StaticFiles(directory="dist"), name="static")

# posts = [
#     {
# 					'id': 1,
# 					'title': 'Post 1',
# 					'content': 'First post',
# 					'comments': [
# 						{
# 							'id': 1, 'content': 'Comment 1', 'author': 'Джони'
# 						},
# 						{
# 							'id': 2, 'content': 'Comment 2', 'author': 'Ноксвелл'
# 						},
#                         {
# 							'id': 3,
# 							'content': 'Comment 3',
# 							'author': 'Новый пост'
# 						},

# 					]
# 				},
# 				{
# 					'id': 2,
# 					'title': 'Post 2',
# 					'content': 'Второй пост',
# 					'comments': [
# 						{
# 							'id': 1,
# 							'content': 'Comment 1',
# 							'author': 'Джони'
# 						},
# 						{
# 							'id': 2,
# 							'content': 'Comment 2',
# 							'author': 'Ноксвелл'
# 						},
# 					]
# 				},
# ]

#_________работа с базой данных


class Post:
    def __init__(self, id: int, title: str, content: str):
        self.id = id
        self.title = title
        self.content = content

def fetch_posts() -> List[Post]:
    conn = sqlite3.connect('db_rogov.sqlite')  
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")  
    results = cursor.fetchall()
    return [Post(id=row[0], title=row[1], content=row[2]) for row in results]


#_________________________



@app.get("/")
def get_index():
    return FileResponse("dist/index.html")


#добавляем точку доступа fastapi
@app.get("/api/posts")
def get_posts():
    return fetch_posts()
   # return posts

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=4767, reload=True)