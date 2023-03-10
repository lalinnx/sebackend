class QuizGroupJson:

    def __init__(self,
                 groupName:str,  # The name of the question group.
                 # The number of questions to pick from the group to display to the student.
                 pickCount:int,
                 # The amount of points allotted to each question in the group.
                 questionPoints:int,
                 # The id of the assessment question bank to pull questions from.
                 assessmentID:int
                 ) -> None:
        self.QuizGroup = []
        self.groupName = groupName
        self.pickCount = pickCount
        self.question_points = 1
        # Dont know the meaning of this parameter
        self.assessment_question_bank_id = 1

    def ToJsonQuizGroup(self) -> None:
        self.QuizGroup.append({
            "name": self.groupName,
            "pick_count": self.pickCount,
            "question_points": self.question_points,
            "assessment_question_bank_id": self.assessment_question_bank_id
        })


class QuizQuestionJson:

    def __init__(self,
                 question_name: str,  # The name of the question.
                 question_text: str,  # The text of the question.
                 # The id of the quiz group to assign the question to.
                 quiz_group_id: int,
                 # The order in which the question will be displayed in the quiz in relation to other questions.
                 position: int,
                 # The maximum amount of points possible received for getting this question correct.
                 points_possible: int,
                 # The comments to display if the student answers the question correctly.
                 correct_comments: str,
                 # The comments to display if the student answers incorrectly.
                 incorrect_comments: str,
                 # The comments to display regardless of how the student answered.
                 neutral_comments: str,
                 # Used in missing word questions.  The text to follow the missing word
                 text_after_answers: str,
                 # An array of available answers to display to the student.
                 answers: list
                 ) -> None:
        self.QuizQuestion = []  # An array of Quiz
        self.QuizQuestionID = 1
        self.question_name = question_name
        self.question_text = question_text
        self.quiz_group_id = quiz_group_id
        # The type of the question.
        self.question_type = "multiple_choice_question"
        self.position = position
        self.points_possible = points_possible
        self.correct_comments = correct_comments
        self.incorrect_comments = incorrect_comments
        self.neutral_comments = neutral_comments
        self.text_after_answers = text_after_answers
        self.answer = answers

    def addQuizQuestion(self) -> None:
        self.QuizQuestion.append(
            {
                "question_name": self.question_name,
                "question_text": self.question_text,
                "quiz_group_id": self.quiz_group_id,
                "question_type": self.question_type,
                "position": self.position,
                "points_possible": self.points_possible,
                "correct_comments": self.correct_comments,
                "incorrect_comments": self.incorrect_comments,
                "neutral_comments": self.neutral_comments,
                "text_after_answers": self.text_after_answers,
                "answer": self.answer
            }
        )

    def getQuizQuestion(self) -> list: #Returns a list of QuizQuestion *** Only Create a single quiz question, So use loop to call canvas api ***
        return self.QuizQuestion


class Answer:
    def __init__(self,
                 answer_text: str,  # The text of the answer.
                 # An integer to determine correctness of the answer. Incorrect answers should be 0, correct answers should be 100.
                 answer_weight: int,
                 ) -> None:
        self.answer = []
        self.answer_text = answer_text
        self.answer_weight = answer_weight

    def addAnswer(self) -> None:  # Preparing list of answer
        self.answer.append({
            "answer_text": self.answer_text,
            "answer_weight": self.answer_weight
        })

    def getAnswer(self) -> list:  # Return an list of answer
        return self.answer
