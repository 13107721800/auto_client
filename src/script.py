from src.client import Agent
from lib.config.settings import settings


def run():
    mode = settings.MODE
    if mode == 'agent':
        obj = Agent()
    else:
        obj = Agent()
    obj.collect()
