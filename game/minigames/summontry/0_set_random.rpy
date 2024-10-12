init python:
    import random
    import time
    random.seed(time.time())

    def chance(percent):
        c = random.randint(0, 100)
        if c < percent:
            return True
        else:
            return False