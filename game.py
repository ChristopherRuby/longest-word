import random
import string

class Game:
    def __init__(self):

        self.grid = []
        for i in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))
        print("init")
        #self.grid = ["L","A","A","E","R","I","C","C"]
        #print(self.grid)
        #print(self.grid)


    def create_grid_validation(self, list):
        self.grid_validation = {}
        for l in list:
            try:
                self.grid_validation[l]
            except KeyError:
                self.grid_validation[l] = 1
            else:
                self.grid_validation[l] = self.grid_validation[l] + 1

        return self.grid_validation

    def is_valid(self, word):

        boolean = False
        message = "EMPTY"
        flag_has_all_key = 0
        list_of_result = []
        self.grid_word = []
        self.grid_for_validate = self.create_grid_validation(self.grid)
        print(self.grid_for_validate)
        # construct list for the word
        for l in word:
            self.grid_word += l.upper()
        print(self.grid_word)

        # update the grid validation base on the grid word.
        # in order to decrease some count to go to 0
        for i in self.grid_word:
            if i in self.grid_for_validate:
                if self.grid_for_validate[i] != 0:
                    self.grid_for_validate[i] = self.grid_for_validate[i]-1
            else:
                flag_has_all_key = 1



        print(set(self.grid_for_validate.values()))
        # get the list of distinct values of count.
        for i in set(self.grid_for_validate.values()):
            list_of_result.append(i)

        # verify we have just the 0 values
        # so we are checking the size of the list and his value
        if len(list_of_result) == 1 and list_of_result[0] == 0:
            message = "Well done"
            boolean = True
        else:
            message = "Not all letters were used wisely"
            boolean = False

        return boolean

# if __name__ == "__main__":
#     inst = Game()
#     print(inst.is_valid("calcaire"))
