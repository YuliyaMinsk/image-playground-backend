from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from src.providers.stub import generate_stub_image

class GenerateImageRequest(BaseModel):
    prompt: str
    style: str = None
    mode: str = "stub"

class GenerateImageResponse(BaseModel):
    image_base64: str


app = FastAPI()

# When I will know the frontend origins, I will replace "*" with them
# origins = [
#     "http://localhost.tiangolo.com"
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    return {"status":"ok"}


@app.post("/api/generate-image", response_model=GenerateImageResponse)
async def generate_image(request: GenerateImageRequest):
    image_base64 = generate_stub_image()
    return {"image_base64": image_base64}
