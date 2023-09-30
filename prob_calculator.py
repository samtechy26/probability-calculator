import copy
import random


class Hat:

  def __init__(self, **kwargs):
    self.contents = []  # initialize list to contain the elements

    if len(kwargs) == 0:
      return "at least one argument needed"

    for k, v in kwargs.items():
      for i in range(v):
        self.contents.append(k)

  def draw(self, num):
    selected_balls = []

    if num > len(self.contents):
      return self.contents

    tl = random.sample(range(len(self.contents)), k=num)
    for i in tl:
      selected_balls.append(self.contents[i])

    tmp = [self.contents[i] for i in range(len(self.contents)) if not i in tl]
    self.contents = tmp
    return selected_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  expected = []
  print(expected_balls)
  for k, v in expected_balls.items():
    for i in range(v):
      expected.append(k)

  hit = 0
  for ne in range(num_experiments):
    ch = copy.deepcopy(hat)
    drawn = ch.draw(num_balls_drawn)

    chk = False
    for e in expected:
      if e in drawn:
        chk = True
        drawn.remove(e)
      else:
        chk = False
        break  # failed if one element is not found in num_balls_drawn

    if chk:
      hit += 1

  return hit / num_experiments
