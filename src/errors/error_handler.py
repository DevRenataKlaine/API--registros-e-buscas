from src.views.http_types.http_response import HttpResponse
from .error_types.http_not_found import HttpNotFoundError

def handle_errors(error: HttpNotFoundError) -> HttpResponse:
    if isinstance(error, HttpNotFoundError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "tittle": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "tittle": error.name,
                    "detail": str(error)
                }]
            }
        )
