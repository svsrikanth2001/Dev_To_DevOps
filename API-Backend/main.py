import uvicorn
import os 

if __name__ == "__main__":
    print(f"print cwd:{os.getcwd()}")
    uvicorn.run("app.api:app", host="127.0.0.1", port=8081, reload=True)
