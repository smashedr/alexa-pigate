import os
from alexa import alexa_resp
from pigate import open_gate


def lambda_handler(event, context):
    try:
        return LambdaHandler.process_intent(event)
    except Exception as error:
        return alexa_resp('Error. {}'.format(error), 'Error')


class LambdaHandler(object):
    gate_code = os.environ.get('gate_code')

    @classmethod
    def process_intent(cls, event):
        return getattr(cls, event['request']['intent']['name'])()

    @classmethod
    def open_gate(cls):
        try:
            open_gate(cls.gate_code)
            return alexa_resp('Ok, I opened the gate.', 'Open Gate')
        except Exception as error:
            return alexa_resp('Error opening the gate. {}.'.format(error), 'Error')
