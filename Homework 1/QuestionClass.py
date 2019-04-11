class Question():
    def __init__(self,answer, player1,player2):
        self.__answer=answer
        self.__player1=player1
        self.__player2=player2
    def getAnswer(self):
        if self.__answer not in range(1,5):
            print("Error: your answer has to be a value between 1 and 4. Try Again.")
            return False
        else:
            return True
    def getScore(self, player):
        if player == 1:
            return self.__player1
        elif player == 2:
            return self.__player2
    def setScore(self, player):
        if player == 1:
            self.__player1 += 1
        elif player == 2:
            self.__player2 += 1
        