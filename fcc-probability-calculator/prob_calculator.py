import copy
import random

# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):

        self.contents = []
        for ballColor in kwargs:
            self.contents = self.contents + [ballColor]*kwargs[ballColor]


    def draw(self, number):
        removed = []
        if number >= len(self.contents):
            removed = self.contents
            self.contents = []
        else:
            for x in range(number):
                removed.append(self.contents.pop(random.randrange(0, len(self.contents))))
        return removed




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_contents = []
    for ballColor in expected_balls:
        expected_balls_contents = expected_balls_contents + [ballColor]*expected_balls[ballColor]

    M = 0
    for x in range(num_experiments):
        hatCopy = copy.deepcopy(hat)
        drawn = hatCopy.draw(num_balls_drawn)
        flag = True

        for ball in expected_balls_contents:


            if ball in drawn:
                drawn.remove(ball)

            else:
                flag = False

        if flag == True:
            M= M+1


    return M/num_experiments
