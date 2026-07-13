from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.models import Interaction
from app.routes import router
from app.ai import llm, extract_interaction,graph

from app.schemas import ChatRequest



Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI First CRM HCP")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "AI First CRM Backend Running"}



@app.get("/test-groq")
def test_groq():
    response = llm.invoke("Say Hello")
    return {
        "response": response.content
    }


# @app.post("/test-ai")
# def test_ai(request: ChatRequest):

#     result = graph.invoke(
#         {
#             "message": request.message
#         }
#     )

#     return result["interaction"]

app.include_router(router)
