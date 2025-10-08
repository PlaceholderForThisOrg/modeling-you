from fastapi import FastAPI

from modeling_you.routes import public

app = FastAPI(
    title="Modeling you service",
    description="Simple learner modeling service",
    version="1.0.0",
    docs_url="/docs",
    contact={"name": "Le Bui Trung Dung", "email": "trungdunglebui17112004@gmail.com"},
)

app.include_router(router=public.router)
