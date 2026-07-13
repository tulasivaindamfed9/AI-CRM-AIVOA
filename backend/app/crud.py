from sqlalchemy.orm import Session
from app.models import Interaction
from app.schemas import InteractionCreate


def create_interaction(db: Session, interaction: InteractionCreate):
    db_interaction = Interaction(**interaction.model_dump())

    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)

    return db_interaction


def get_latest_interaction(db: Session):
    return (
        db.query(Interaction)
        .order_by(Interaction.id.desc())
        .first()
    )


def update_interaction(db: Session, interaction_id: int, data: dict):
    interaction = (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )

    if not interaction:
        return None

    for key, value in data.items():
        setattr(interaction, key, value)

    db.commit()
    db.refresh(interaction)

    return interaction


def edit_latest_interaction(db: Session, updates: dict):

    interaction = (
        db.query(Interaction)
        .order_by(Interaction.id.desc())
        .first()
    )

    if not interaction:
        return None

    for key, value in updates.items():
        if hasattr(interaction, key) and value:
            setattr(interaction, key, value)

    db.commit()
    db.refresh(interaction)

    return interaction