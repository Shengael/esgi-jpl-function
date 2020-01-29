import logging
import azure.functions as func


def main(request: func.HttpRequest, msg: func.Out[str]) -> func.HttpResponse:
    response = "le body n'a pas le format requis. {current_percentage: int (0 - 100)}"
    speed = 90
    try:
        body = request.get_json()

        if body['current_percentage'] > 100 or body['current_percentage'] < 0:
            logging.info(f"salut les amis")
            raise ValueError
        res = {'duration': (100 - body['current_percentage']) * speed, 'percentage': body['current_percentage']}
        response = "le temp restant est de {}\nLa donnée a été ajoutée dans la queue".format(res['duration'])
        msg.set(f"{res}")
    except ValueError:
        response = f"current_percentage doit être compris entre 0 et 100"
    except Exception:
        pass
    return func.HttpResponse(response, status_code=200)
