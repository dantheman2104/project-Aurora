class Brain:

    def __init__(self):

        self.name = "Aurora"

    def respond(self, prompt):

        return f"You said: {prompt}"

class Memory:

    def __init__(self):

        self.history = []

    def store(self, user, assistant):

        self.history.append(
            {
                "user": user,
                "assistant": assistant
            }
        )

    def get(self):

        return self.history

#requirements.txt

#end of chunk one



MODEL = "local"

TEMPERATURE = 0.7

MAX_HISTORY = 25

DATABASE = "database/memory.db"

import sqlite3

from .config import DATABASE

