import uvicorn
startup_module = "app.api:app"
host = "0.0.0.0"

if __name__ == "__main__":
    uvicorn.run(startup_module, host=host, port=8080, reload=True)