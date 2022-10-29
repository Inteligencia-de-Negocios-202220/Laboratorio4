from pydantic import BaseModel, validator

class DataModel(BaseModel):
# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
    serial_no: float
    gre_score: float
    toefl_score: float
    university_rating: float
    sop: float
    lor: float
    cgpa: float
    research: float

#Esta función retorna los nombres de las columnas correspondientes con el modelo exportado en joblib.
    @staticmethod
    def columns():
        return ["Serial No.","GRE Score","TOEFL Score","University Rating","SOP","LOR ","CGPA","Research"]

    @validator('gre_score')
    def validate_gre_score(cls, value):
        if value < 0 or value > 340:
            raise ValueError('GRE Score must be between 0 and 340')
        return value

    @validator('toefl_score')
    def validate_toefl_score(cls, value):
        if value < 0 or value > 120:
            raise ValueError('TOEFL Score must be between 0 and 120')
        return value

    @validator('university_rating')
    def validate_university_rating(cls, value):
        if value < 0 or value > 5:
            raise ValueError('University Rating must be between 0 and 5')
        return value

    @validator('sop')
    def validate_sop(cls, value):
        if value < 0 or value > 5:
            raise ValueError('SOP must be between 0 and 5')
        return value

    @validator('lor')
    def validate_lor(cls, value):
        if value < 0 or value > 5:
            raise ValueError('LOR must be between 0 and 5')
        return value

    @validator('cgpa')
    def validate_cgpa(cls, value):
        if value < 0 or value > 10:
            raise ValueError('CGPA must be between 0 and 10')
        return value

    @validator('research')
    def validate_research(cls, value):
        if value != 0 and value != 1:
            raise ValueError('Research must be either 0 or 1')
        return value

class DataModelFit(DataModel):
    admission_points: float

    @staticmethod
    def columns():
        return DataModel.columns() + ["Admission Points"]

    @validator('admission_points')
    def validate_admission_points(cls, value):
        if value < 0 or value > 150:
            raise ValueError('Admission Points must be between 0 and 150')
        return value