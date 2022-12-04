import uvicorn

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from .routers import products, categories


app = FastAPI(
    # title=config.PROJECT_NAME,
    description='Study project using FastAPI + Elasticsearch',
    docs_url='/api/docs',
    openapi_url='/api/docs.json',
    default_response_class=ORJSONResponse,
)


# @app.on_event('startup')
# async def startup():
#     pass

# @app.on_event('shutdown')
# async def shutdown():
#     pass

# to do: get api prefix/version from config
api_prefix = '/api/v1'

app.include_router(products.router, prefix=api_prefix)
app.include_router(categories.router, prefix=api_prefix)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        reload=True
    )