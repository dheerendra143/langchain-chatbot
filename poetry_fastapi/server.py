import uvicorn

def start():
  uvicorn.run("poetry_fastapi.src.app:app", host="0.0.0.0", port=8000, reload=True)