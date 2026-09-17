#Lets go
#OMID MOHAMMADI     

from fastapi import FastAPI, status, Path, HTTPException
app = FastAPI()

expenses = [
    {"id":1, "description":"laptop", "amount":float(23)},
    {"id":2, "description":"mobile", "amount":float(10.5)}
]


@app.post("/add-amount", status_code=status.HTTP_201_CREATED)
def add_amount(description:str, amount):
    new_id = len(expenses) + 1
    new_expense = {"id":new_id, "description":description, "amount":float(amount)}
    expenses.append(new_expense)
    return new_expense



@app.get("/amounts", status_code=status.HTTP_200_OK)
def all_amounts():
    return expenses


@app.get("/amounts/{amount_id}", status_code=status.HTTP_200_OK)
def spesific_amount(amount_id:int = Path()):
    for expense in expenses:
        if expense["id"]==amount_id:
            return expense

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"detail":"amount not found"})


@app.put("/edit-amount/{amount_id}", status_code=status.HTTP_202_ACCEPTED)
def edit_amount(amount_id:int=Path(), new_amount:float=None):
    for expense in expenses:
        if expense["id"]==amount_id:
            expense["amount"]=new_amount
            return expense

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"detail":"amount not found"})


@app.delete("/delete-amount/{amount_id}", status_code=status.HTTP_200_OK)
def delete_amount(amount_id:int=Path()):
    for expense in expenses:
        if expense["id"]==amount_id:
            expenses.remove(expense)
            return {"detail": f"amount with id {amount_id} is deleted"}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"detail":"amount not found"})

