from fastapi import FastAPI # type: ignore

app = FastAPI(
    title="InterviewIQ API",
    description="AI Interview & Career Copilot backend",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "InterviewIQ API is running",
        "version": "0.1.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }