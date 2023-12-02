import azure.functions as func
from code_to_import import helper_code
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.function_name("ExampleFunction")
@app.route(route="examplefunction")
def example_function_http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logging.info("Your example function was successfully triggered.")

    # do something with the req argument
    events = req.get_json()
    logger.info(f"Request body:\n{events}")

    # execute imported functions
    helper_code()

    # put your own code here ...


    # finish execution
    logger.info("Finished execution.")
    return func.HttpResponse()

@app.function_name("AnotherExampleFunction")
@app.route(route="anotherexamplefunction")
def another_example_function_http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logging.info("Another example function was successfully triggered.")

    # do something with the req argument
    events = req.get_json()
    logger.info(f"Request body:\n{events}")

    # execute imported functions
    helper_code()

    # put your own code here ...

    # finish execution
    logger.info("Finished execution.")
    return func.HttpResponse()
