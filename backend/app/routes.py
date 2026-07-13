from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.ai import graph, extract_edit_fields
 

from app.database import get_db
from app.schemas import InteractionCreate, InteractionResponse,ChatRequest,EditRequest
from app import crud

router = APIRouter(prefix="/interaction", tags=["Interaction"])

# router to post the interaction data to the database
@router.post("/log", response_model=InteractionResponse)
def log_interaction(
    request: ChatRequest,
    db: Session = Depends(get_db),
):
    # Run the LangGraph workflow
    data = graph.invoke(
        {
            "message": request.message
        }
    )["interaction"]

    # Convert AI response to Pydantic model
    interaction = InteractionCreate(**data)

    # Save to PostgreSQL
    saved = crud.create_interaction(db, interaction)

    return saved

# router to get the latest interaction from the database
@router.get("/latest", response_model=InteractionResponse)
def latest_interaction(
    db: Session = Depends(get_db),
):
    interaction = crud.get_latest_interaction(db)

    if not interaction:
        raise HTTPException(
            status_code=404,
            detail="No interaction found",
        )

    return interaction


# router to edit the latest interaction in the database
@router.put("/edit", response_model=InteractionResponse)
def edit_interaction(
    request: EditRequest,
    db: Session = Depends(get_db),
):

    updates = extract_edit_fields(request.message)
    print("Updates from AI:", updates)

    updated = crud.edit_latest_interaction(db, updates)

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="No interaction found"
        )

    return updated