from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.session import get_db   # ✅ FIXED HERE
from app.models.guardian import Guardian
from app.schemas.guardian_schema import GuardianCreate, GuardianResponse

router = APIRouter()


@router.post("/", response_model=GuardianResponse)
def register_guardian(guardian: GuardianCreate, db: Session = Depends(get_db)):
    existing = db.query(Guardian).filter(Guardian.email == guardian.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Guardian already registered with this email")

    new_guardian = Guardian(
        name=guardian.name,
        email=guardian.email
    )

    db.add(new_guardian)
    db.commit()
    db.refresh(new_guardian)

    return new_guardian


@router.get("/", response_model=List[GuardianResponse])
def get_all_guardians(db: Session = Depends(get_db)):
    guardians = db.query(Guardian).all()
    return guardians


@router.get("/{guardian_id}", response_model=GuardianResponse)
def get_guardian(guardian_id: int, db: Session = Depends(get_db)):
    guardian = db.query(Guardian).filter(Guardian.id == guardian_id).first()

    if not guardian:
        raise HTTPException(status_code=404, detail="Guardian not found")

    return guardian


@router.delete("/{guardian_id}")
def delete_guardian(guardian_id: int, db: Session = Depends(get_db)):
    guardian = db.query(Guardian).filter(Guardian.id == guardian_id).first()

    if not guardian:
        raise HTTPException(status_code=404, detail="Guardian not found")

    db.delete(guardian)
    db.commit()

    return {"message": "Guardian deleted successfully"}