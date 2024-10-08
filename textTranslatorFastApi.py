from fastapi import FastAPI
from routes.text_translate import router as text_translater

app = FastAPI()

# 라우트 등록
app.include_router(text_translater)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("textTransloter:app", host="0.0.0.0", port=4444, reload=True)
# uvicorn textTranslatorFastApi:app --host 0.0.0.0 --port 4444 --reload