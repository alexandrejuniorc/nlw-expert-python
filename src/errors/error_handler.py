from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntity
from src.views.http_types.http_response import HttpResponse


def handle_errors(error: Exception) -> HttpResponse:
    # enviar para um log
    # enviar um email de notificação
    if isinstance(error, HttpUnprocessableEntity):
        return HttpResponse(
            status_code=error.status_code,
            body={"errors": [{"title": error.name, "detail": error.message}]},
        )

    return HttpResponse(
        status_code=500,
        body={"errors": [{"title": "Internal Server Error", "detail": str(error)}]},
    )
