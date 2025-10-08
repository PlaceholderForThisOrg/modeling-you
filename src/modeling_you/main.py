from modeling_you.configs import app


def main():
    import uvicorn

    app_loc = "modeling_you.app:app"
    uvicorn.run(app_loc, host=app.HOST, port=app.PORT, reload=True)


if __name__ == "__main__":
    main()
