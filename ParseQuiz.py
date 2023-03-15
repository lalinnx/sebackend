from QuizObject import QuizGroupObject, QuizQuestionObject
from lexer import Lexer
from parser_ import Parser
import node


def parse_quiz(quiz_text):

    # Tokenize the quiz text using the Lexer class
    lexer = Lexer(quiz_text)
    tokens = lexer.generate_tokens()

    # Parse the tokens using the Parser class
    parser = Parser(tokens)
    parse_tree = parser.parse()

    # Prepare the quiz group and question objects
    quiz_group = QuizGroupObject()
    quiz_question = QuizQuestionObject()
    order_id = 0

    # Loop through each group in the parse tree
    for parse_q in parse_tree:
        if type(parse_q) is node.Group:
            order_id += 1
            question_list = parse_q.Question
            # Add the quiz group object to the prepared_quizGroup
            quiz_group.addQuizGroup(
                groupName=parse_q.name,
                pickCount=len(question_list),
                questionPoints=int(float(parse_q.point))
            )

            # Loop through each question in the group
            for question in question_list:
                count = 0
                choices = question.choice.choice
                preparedQuizQuestion = {}
                # The name of the question.
                preparedQuizQuestion['question[question_name]'] = question.name
                # The text of the question.
                preparedQuizQuestion['question[question_text]'] = question.ques
                
                # The id of the quiz group to assign the question to.
                preparedQuizQuestion['question[quiz_group_id]'] = 0
                # Because we dont know the group id, we need to check with the name of group name.
                preparedQuizQuestion['group_belong_to'] = parse_q.name
                
                    

                # The type of question. Multiple optional fields depend upon the type of question to be used.
                # always multiple_choice_question
                preparedQuizQuestion['question[question_type]'] = 'multiple_choice_question'
                
                # Loop through each choice in the question
                for choice in choices:
                    if choice == question.choice.Ans:
                        print("answer choice: ", choice)
                        preparedQuizQuestion[f'question[answers][{count}][answer_text]'] = choice
                        preparedQuizQuestion[f'question[answers][{count}][answer_weight]'] = 100
                    else:
                        print("choice: ", choice)
                        preparedQuizQuestion[f'question[answers][{count}][answer_text]'] = choice
                        preparedQuizQuestion[f'question[answers][{count}][answer_weight]'] = 0
                    count += 1
                # Add the quiz question object to the prepared_quizQuestion
                quiz_question.addQuizQuestion(
                    preparedQuizQuestion=preparedQuizQuestion
                )

               
        else:
            choices = parse_q.choice.choice
            count=0
            preparedQuizQuestion = {}
            # The name of the question.
            preparedQuizQuestion['question[question_name]'] = parse_q.name
            # The text of the question.
            preparedQuizQuestion['question[question_text]'] = parse_q.ques
            preparedQuizQuestion['question[question_type]'] = 'multiple_choice_question'
            # The maximum amount of points possible received for getting this question correct.
            preparedQuizQuestion['question[points_possible]'] = int(float(parse_q.point))
            for choice in choices:
                    
                    if choice == parse_q.choice.Ans:
                        print("answer choice: ", choice)
                        preparedQuizQuestion[f'question[answers][{count}][answer_text]'] = choice
                        preparedQuizQuestion[f'question[answers][{count}][answer_weight]'] = 100
                    else:
                        print("choice: ", choice)
                        preparedQuizQuestion[f'question[answers][{count}][answer_text]'] = choice
                        preparedQuizQuestion[f'question[answers][{count}][answer_weight]'] = 0
                    count += 1
                    
            # Add the quiz question object to the prepared_quizQuestion
            quiz_question.addQuizQuestion(
                    preparedQuizQuestion=preparedQuizQuestion
                )
        


    return {"quiz_groups": quiz_group.getQuizGroup(), "quiz_questions": quiz_question.getQuizQuestion()}
