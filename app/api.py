from fastapi import FastAPI,  UploadFile, File, HTTPException
from app.pipeline.router import extract_document_text


app = FastAPI(
    title="Vertex AI Document Intelligence API",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/v1/documents/analyze")
async def analyze_document(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(('.pdf')):
        raise HTTPException(
            status_code=400, 
            detail="Invalid file type. Only PDF files are supported."
        )

    content: bytes = await file.read()

    if not content:
        raise HTTPException(
            status_code=400,
            detail = "Empty file uploaded. Please provide a valid PDF document."
        )
    
    text = extract_document_text(content)

    if not text.strip():
        raise HTTPException(
            status_code=422,
            detail="Unable to extract readable text from document"
        )

    return {
        "status": "TEXT_EXTRACTED",
        "filename": file.filename,
        "text_length": len(text)
    }

    
