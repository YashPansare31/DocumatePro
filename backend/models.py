from pydantic import BaseModel

class ExtractResponse(BaseModel):
    message: str
    excel_path: str
