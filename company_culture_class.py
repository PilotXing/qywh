# -*- coding: UTF-8 -*-

class Question:
    """
    docstring
    """

    def __init__(self, question='', choice=[], answer=[], familiarity=[]):
        """
        docstring
        """
        self.question = question
        self.choice = choice
        self.answer = answer
        self.familiarity = familiarity

    def show(self, ):
        """
        显示本题
        """
        print('='*30)
        print(self.question)
        for i in self.choice:
            print(i)
        print('='*30)

    def show_answer(self, ):
        """
        显示答案
        """
        print('='*30)
        print(self.question)
        for i in q.choice:
            if q.choice.index(i) == int(q.answer):
                print(' '*5+i+' '*5)
            else:
                print('X'*5+i+'X'*5)
        print('='*30)

    def show_random(self, parameter_list):
        """
        打乱顺序
        """
        pass

    def change_familiarity(self, ):
        """
        更改熟练度
        """
        pass


if __name__ == '__main__':
    q = Question('question', ['choice 1', 'choice 2', 'choice 3'], '2', '1')
    # print(q.question)
    # print(q.answer)
    # print(q.choice[int(q.answer)])
    q.show()
    q.show_answer()
