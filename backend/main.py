import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from text_extractor import extract_text
from excel_writer import write_text_to_excel
from models import ExtractResponse

app = FastAPI()

OUTPUT_DIR = "generated_excels"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/extract", response_model=ExtractResponse)
async def extract_document(file: UploadFile = File(...)):

    file_ext = file.filename.split(".")[-1].lower()
    temp_file = f"temp_input.{file_ext}"

    with open(temp_file, "wb") as f:
        f.write(await file.read())

    extracted_text = extract_text(temp_file, file_ext)

    excel_path = os.path.join(
        OUTPUT_DIR,
        file.filename.rsplit(".",1)[0] + ".xlsx"
    )

    write_text_to_excel(extracted_text, excel_path)

    return ExtractResponse(
        message="Text extracted successfully",
        excel_path=excel_path
    )

@app.get("/download")
def download_excel(path: str):
    return FileResponse(path, media_type="application/vnd.ms-excel")
