
class Scorecard:

    firstscore = 0

    secondscore = 0

    def __init__(self, sequence):
        self.sequence = sequence

    def second(self, newseq):


            n = newseq[0]

            print(self.sequence)

            Scorecard.secondscore += newseq[0]

            self.sequence.remove(newseq[0])

            #
            if n % 2 == 0:
                self.sequence = self.sequence[::-1]


    def first(self,sequence):

            n  = sequence[0]

            Scorecard.firstscore += sequence[0]

            if len(self.sequence) !=1 :

                self.sequence.remove(sequence[0])

                if n%2 == 0:

                    self.sequence = self.sequence[::-1]

                Scorecard.second(self,self.sequence)
            else:
                Scorecard.firstscore = Scorecard.firstscore



    def score(self):

        print("main: ", self.sequence)

        if(len(self.sequence) % 2 == 0):   #if length of list is even

            for i in range((len(self.sequence) // 2)):
                f = Scorecard.first(self, self.sequence)

        else:                       #for list of length is odd
            for i in range((len(self.sequence)//2)+1):
                f = Scorecard.first(self,self.sequence)

        result = Scorecard.firstscore - Scorecard.secondscore
        print(self.sequence, "\nfirstscore: ", Scorecard.firstscore, "secondscore: ", Scorecard.secondscore, "Result: ",result)

        return result


l = 6

numseq = [3, 6, 2, 3, 5]
# numseq = [1, 6, 8, 7, 3, 9, 5]  #for testing purpose

game  = Scorecard(numseq)
print(game.score())