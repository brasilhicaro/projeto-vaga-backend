from fastapi import FastAPI

from src.presentation.controllers import department, employee


def create_application() -> FastAPI:
    application = FastAPI(
        title="Projeto do Hicaro",
        summary="Projeto para vaga de backend",
        contact={
            "name": "Hicaro Brasil",
            "email": "hicaro.brasil@hotmail.com",
            "url": "https://github.com/brasilhicaro",
        },
    )
    application.include_router(department.router, prefix="/department")
    application.include_router(employee.router, prefix="/employee")
    return application


app = create_application()


@app.get("/")
async def root():
    return {"message": "Projeto do Hicaro"}