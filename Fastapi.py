from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse
import json
import logging
app = FastAPI()

def load_data():
    try:
        with open("Score.json", 'r') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Error reading JSON file: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/")
def read_root():
    return{"Hello": "shafi"}

@app.get("/score/{user_name}")
def get_score(user_name: str):
    data = load_data()
    for player in data['players']:
        if player['name'] == user_name:
            score = player['score']
            html_content = f"""
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>The score of {user_name} is <div id="score">{score}</div></h1>
                </body>
            </html>
            """
            return HTMLResponse(content=html_content)
    error = "User not found"
    html_not_found = f"""
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1><div id="score" style="color:red">{error}</div></h1>
        </body>
    </html>"""
    return HTMLResponse(content=html_not_found)