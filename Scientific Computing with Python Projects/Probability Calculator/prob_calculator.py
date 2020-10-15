import copy
import random


# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, val in kwargs.items():
            for num in range(val):
                self.contents.append(key)

    def draw(self, num):
        if num > len(self.contents):
            return self.contents
        picked_balls = []
        for i in range(num):
            pick = random.choice(self.contents)
            self.contents.remove(pick)
            picked_balls.append(pick)
        return picked_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    correct_picks = 0
    found = False
    for i in range(num_experiments):
        temp_hat = copy.deepcopy(hat)
        drawn_balls = temp_hat.draw(num_balls_drawn)
        drawn_balls = {key: drawn_balls.count(key) for key in drawn_balls}
        for key, val in expected_balls.items():
            if key in drawn_balls and expected_balls[key] <= drawn_balls[key]:
                found = True
            else:
                found = False
                break
        if found:
            correct_picks += 1
    return correct_picks/num_experiments

