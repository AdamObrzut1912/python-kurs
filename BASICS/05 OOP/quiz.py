import requests
import html

class Question:
    def __init__(self,category, questionStr, correctAnwserFlag):
        self.category = category
        self.questionStr = questionStr
        self.correctAnwserFlag = correctAnwserFlag

class Quiz:
    def __init__(self, numQuestions):
        self.apiUrl = apiUrl = "https://opentdb.com/api.php?type=boolean&amount="
        self.nuQuestion = numQuestions
        self.questionList = []
        self.loadQuestions(numQuestions)

    def loadQuestions(self,numQuestions):
        response = requests.get(self.apiUrl + str(numQuestions))

        if response.ok:
            # print(response.json())
            data = response.json()
            results = data["results"]

            for q in results:
                category = (q["category"])
                questionType = q["type"]
                difficulty = q["difficulty"]
                questionStr = html.unescape(q["question"])
                print(questionStr)
                correctAnwserFlag = q["correct_answer"].lower() in ['true', '1', "yes", "True"]

                qObj = Question(category, questionStr, correctAnwserFlag)
                self.questionList.append(qObj)

    def startQuiz(self):
        print("\nWelocome in quiz")
        numCorrectUserAnwsers = 0

        n = 0
        numQuestions = len(self.questionList)

        while n < numQuestions:
            q = self.questionList[n]
            print("Question number" + str(n) + ": ",q.questionStr)
            print("Anser flag: ", q.correctAnwserFlag)

            anwser = input("give correct anwser as y/n")

            anweserBool = False
            if anwser == "y":
                anweserBool = True
            
            if anweserBool == q.correctAnwserFlag:
                print("Correct!")
                numCorrectUserAnwsers += 1
            else:
                print("Not correct!")
            n += 1

        print("Number of correct anwsers: ",numCorrectUserAnwsers, "from: ", len(self.questionList))

quiz = Quiz(10)
quiz.startQuiz()