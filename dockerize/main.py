from fastapi import FastAPI, HTTPException, Header, Body
from typing import Dict

app = FastAPI()
global_list = []

@app.get("/sum1n/{n}")
async def sum1n(n: int):
    result = sum(range(1, n+1))
    return {"result": result}

@app.get("/fibo")
async def fibo(n: int):
    if n <= 0:
        raise HTTPException(status_code=400, detail="Invalid value of n. n should be a positive integer.")
    if n == 1:
        return {"result": 0}
    elif n == 2:
        return {"result": 1}
    a, b = 0, 1
    for _ in range(n-2):
        a, b = b, a + b
    return {"result": b}

@app.post("/reverse")
async def reverse(string: str = Header(None)):
    if string is None:
        raise HTTPException(status_code=400, detail="Header 'string' is missing.")
    return {"result": string[::-1]}

@app.put("/list")
async def add_to_list(element: dict):
    global_list.append(element["element"])
    return {"result": global_list}

@app.get("/list")
async def get_list():
    return {"result": global_list}

@app.post("/calculator")
async def calculator(expr: str = Body(...)):
    num1, operator, num2 = expr.split(",")
    num1, num2 = float(num1), float(num2)
    if operator == "+":
        return {"result": num1 + num2}
    elif operator == "-":
        return {"result": num1 - num2}
    elif operator == "*":
        return {"result": num1 * num2}
    elif operator == "/":
        if num2 == 0:
            raise HTTPException(status_code=403, detail="Division by zero.")
        return {"result": num1 / num2}
    else:
        raise HTTPException(status_code=400, detail="Invalid expression format.")

