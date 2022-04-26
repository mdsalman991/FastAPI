from fastapi import FastAPI, Path

app = FastAPI() 

students = {
    1 : {
        "name" : "salman",
        "age" : 22,
        "class" : "year 12",   
        "sex" : "male"
    }
}
@app.get("/")

def index():
    return {"name":"first data"}
    
@app.get("/get-student/{student_id}")

def get_student(student_id: int = Path(None, description = "The ID of the Student you want to view") ):
    return students[student_id]
    
@app.get("/get-by-name")

def get_by_name(*, name: str = None, test : int ):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data" : "Not Found"}
