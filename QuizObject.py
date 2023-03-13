class QuizGroupObject:

    def __init__(self,

                 ) -> None:
        self.QuizGroup = []

    def addQuizGroup(self,
                     groupName: str,  # The name of the question group.
                     # The number of questions to pick from the group to display to the student.
                     pickCount: int,
                     # The amount of points allotted to each question in the group.
                     questionPoints: int,

                     ) -> None:
        self.QuizGroup.append({
            "quiz_groups[][name]": groupName,
            "quiz_groups[][pick_count]": pickCount,
            "quiz_groups[][question_points]": questionPoints,
        })

    def getQuizGroup(self) -> list:
        return self.QuizGroup


class QuizQuestionObject:

    def __init__(self) -> None:
        self.QuizQuestion = []  # An array of Quiz

    def addQuizQuestion(self,
                        preparedQuizQuestion: dict,
                        ) -> None:
        print(preparedQuizQuestion)
        self.QuizQuestion.append(
            preparedQuizQuestion
        )

    # Returns a list of QuizQuestion *** Only Create a single quiz question, So use loop to call canvas api ***
    def getQuizQuestion(self) -> list:
        return self.QuizQuestion
