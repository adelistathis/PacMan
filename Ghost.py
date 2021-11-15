from Player import Player


class Ghost(Player):

    # Change the speed of the ghost
    def change_speed(self, move_list, ghost, turn, steps, l):

      try:
        z = move_list[turn][2]
        if steps < z:
          self.change_x = move_list[turn][0]
          self.change_y = move_list[turn][1]
          steps += 1
        else:
          if turn < l:
            turn += 1
          elif ghost == "clyde":
            turn = 2
          else:
            turn = 0

          self.change_x = move_list[turn][0]
          self.change_y = move_list[turn][1]
          steps = 0
        return [turn, steps]
      except IndexError:
         return [0, 0]