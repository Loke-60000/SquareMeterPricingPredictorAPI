from fastapi.responses import JSONResponse

async def internal_error_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )
