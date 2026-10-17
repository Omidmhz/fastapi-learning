#Lets go
#OMID MOHAMMADI     

from fastapi import FastAPI, status, Path, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class ExpenseCreate(BaseModel):
    description: str = Field(min_length=2, max_length=100)
    amount: float = Field(gt=0)

class ExpenseUpdate(BaseModel):
    amount: float = Field(gt=0)

class ExpenseOut(BaseModel):
    id: int = Field(gt=0)
    description: str
    amount: float = Field(gt=0)

class DeleteResponse(BaseModel):
    detail: str


expenses = [
    {"id":1, "description":"laptop", "amount":float(23)},
    {"id":2, "description":"mobile", "amount":float(10.5)}
]


@app.post("/add-amount", status_code=status.HTTP_201_CREATED, response_model=ExpenseOut)
def add_amount(expense: ExpenseCreate):
    new_id = len(expenses) + 1
    new_expense = {
        "id": new_id,
        "description": expense.description,
        "amount": expense.amount
    }

    expenses.append(new_expense)
    return new_expense


@app.get("/amounts", status_code=status.HTTP_200_OK, response_model=list[ExpenseOut])
def all_amounts():
    return expenses


@app.get("/amounts/{amount_id}", status_code=status.HTTP_200_OK, response_model=ExpenseOut)
def spesific_amount(amount_id: int = Path(gt=0)):
    for expense in expenses:
        if expense["id"] == amount_id:
            return expense

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="amount not found")


@app.put("/edit-amount/{amount_id}", status_code=status.HTTP_202_ACCEPTED, response_model=ExpenseOut)
def edit_amount(amount_id: int = Path(gt=0), expense_update: ExpenseUpdate = ...):
    for expense in expenses:
        if expense["id"] == amount_id:
            expense["amount"] = expense_update.amount
            return expense

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="amount not found")


@app.delete("/delete-amount/{amount_id}", status_code=status.HTTP_200_OK, response_model=DeleteResponse)
def delete_amount(amount_id: int = Path(gt=0)):
    for expense in expenses:
        if expense["id"] == amount_id:
            expenses.remove(expense)
            return {
                "detail": f"amount with id {amount_id} is deleted"
            }

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="amount not found")

