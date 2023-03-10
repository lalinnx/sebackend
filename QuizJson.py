class QuizGroupJson:
    
    def __init__(self,
                 groupName,         #The name of the question group. 
                 pickCount,         #The number of questions to pick from the group to display to the student.
                 questionPoints,    #The amount of points allotted to each question in the group.
                 assessmentID       #The id of the assessment question bank to pull questions from.
                 ) -> None:
        self.QuizGroup =[]
        self.groupName = groupName
        self.pickCount = pickCount
        self.question_points = 1 
        self.assessment_question_bank_id = 1
    def ToJsonQuizGroup() -> dict:
        return {}
    
class QuizQuestionJson:
    
    def __init__(self,
                 question_name:str,           #The name of the question.
                 question_text:str,           #The text of the question.
                 quiz_group_id:int,           #The id of the quiz group to assign the question to.
                 question_type:str,           #The type of the question.
                 position:int,                #The order in which the question will be displayed in the quiz in relation to other questions.
                 points_possible:int,         #The maximum amount of points possible received for getting this question correct.
                 correct_comments:str,        #The comments to display if the student answers the question correctly.
                 incorrect_comments:str,      #The comments to display if the student answers incorrectly.
                 neutral_comments:str,        #The comments to display regardless of how the student answered.
                 text_after_answers:str,      #Used in missing word questions.  The text to follow the missing word
                 answers:list                  #An array of available answers to display to the student.
                 ) -> None:
        self.QuizQuestion =[]
        self.QuizQuestionID = 1
        self.question_name = question_name
        self.question_text=question_text
        self.quiz_group_id = quiz_group_id
        self.question_type = question_type
        self.position = position
        self.points_possible = points_possible
        self.correct_comments = correct_comments
        self.incorrect_comments = incorrect_comments
        self.neutral_comments = neutral_comments
        self.text_after_answers = text_after_answers
        self.answer = answers
    def addAnswer(self, answer):
        self.answer.append(answer)  
    def ToJsonQuizQuestion() -> dict:
        return {}

class Answer:
    def __init__(self,
                 answer_text:str,   #The text of the answer.
                 answer_weight:int, #An integer to determine correctness of the answer. Incorrect answers should be 0, correct answers should be 100.
                 ):
        self.answer_text = answer_text
        self.answer_weight = answer_weight

    def ToAnswerObject(self) -> dict:
        return {
            "answer_text": self.answer_text,
            "answer_weight": self.answer_weight
        }