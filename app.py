from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from typing import List, Dict

app = FastAPI()

# List of routes and methods to bypass middleware
EXCLUDED_ROUTES = [
    {"path": "/without-middleware", "methods": ["GET", "POST"]},  # Example: both GET and POST bypass middleware
    {"path": "/another-excluded-route", "methods": ["GET"]}  # Example: GET only
]

# Custom middleware
class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Check if the request path and method match any exclusion in EXCLUDED_ROUTES
        for route in EXCLUDED_ROUTES:
            if request.url.path == route["path"] and request.method in route["methods"]:
                print(f"[Middleware] Skipping middleware for {request.method} {request.url.path}")
                return await call_next(request)
        
        # Middleware processing for monitored requests
        print(f"[Middleware] Processing middleware for {request.method} {request.url.path}")
        response = await call_next(request)
        print(f"[Middleware] Finished processing for {request.method} {request.url.path}")
        return response

# Add middleware to the app
app.add_middleware(CustomMiddleware)

# Define routes
@app.get("/without-middleware")
async def without_middleware():
    print("[Route Handler] Executed without middleware.")
    return {"message": "This route does not use middleware."}

@app.post("/without-middleware")
async def without_middleware_post():
    print("[Route Handler] Executed without middleware (POST).")
    return {"message": "This POST route does not use middleware."}

@app.get("/with-middleware")
async def with_middleware():
    print("[Route Handler] Executed with middleware.")
    return {"message": "This route uses middleware."}

@app.post("/with-middleware")
async def post_with_middleware():
    print("[Route Handler] Executed with middleware (POST).")
    return {"message": "POST request with middleware."}
