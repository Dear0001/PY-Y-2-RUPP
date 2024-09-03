from flask import Flask
app = Flask (__name__)
Classes = [
    {
        "Class": "M4",
        "Students": [
            {"name": "Sok", "gender": "Female"},
            {"name": "Sao", "gender": "Male"}
        ]
    }
]

@app.get("/class")
def company():
    return {"class": Classes}
@app.post("/class") 
def createnew():
    new_company = {"name": "PP Bookstore", "items": []}
    Classes.append(new_company)
    return {"msg":"Bravo"}
if __name__ == '__main__': 
    app.run(debug=True)



{
    "Class": "M3",
    "Students": [
        {"name": "Chanda", "gender": "Female"},
        {"name": "Vicheka", "gender": "Male"}
    ]
}