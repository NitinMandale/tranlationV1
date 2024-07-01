import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing incoming call event.')

    try:
        call_event = req.get_json()
        logging.info(f"Received call event: {call_event}")


    except ValueError:
        return func.HttpResponse(
            "Invalid input",
            status_code=400
        )

    # Add your logic to handle the incoming call here
    # For example, log the event, respond with a message, etc.


    return func.HttpResponse("Event received and processed", status_code=200)
