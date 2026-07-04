class Aurora:

    def __init__(self):

        self.brain = Brain()

        self.memory = Memory()

def run(self):

    print("Aurora AI v0.2")

    while True:

        prompt = input("> ")

        if prompt.lower() == "exit":

            break

        response = self.brain.respond(prompt, self.memory)

        self.memory.store(prompt, response)

        print("\n"+response+"\n")
