# -*- coding: UTF-8 -*-
def read_item_bank(file_name):
    q = open(file_name, 'r', encoding='utf-8')
    item_bank = []
    d = {'question': '', 'choice': '', 'answer': '\n', 'familiarity': '0\n'}

    while True:
        new_line = q.readline()

        if not new_line:
            break

        if new_line[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            item_bank.append(d)
            d = {}
            d['question'] = new_line
            d['answer'] = '\n'
            d['choice'] = []
            d['familiarity'] = '0\n'

        if new_line[0] in ['A', 'B', 'C', 'D', 'E']:
            d['choice'].append(new_line)

        if new_line[0] == '!':
            d['answer'] = new_line[1]
        if new_line[0] == '?':
            d['familiarity'] = new_line[1]

    item_bank.append(d)
    q.close()

    return item_bank


def write_item_bank(file_name, item_bank):
    f = open(file_name, 'w', encoding='utf-8')
    for i in item_bank:
        f.write(i['question'])
        f.write('!'+i['answer']+'\n')
        f.write('?'+i['familiarity']+'\n')
        for j in i['choice']:
            f.write(j)
        f.write('\n')
    f.close()


def input_answer(file_name):
    ib = read_item_bank(file_name)
    for i in ib:
        show_one(i)
        i['answer'] = input('please input answer')
    write_item_bank('3.txt', ib)


def show_all(a):
    for i in a:
        print(i['question'])
        for j in i['choice']:
            print(j)


def show_one(a):
    print(a['question'])
    for i in a['choice']:
        print(i)


def show_one_answer(d_question):
    print(d_question['question'])
    for i in d_question['choice']:
        if d_question['choice'].index(i) == int(d_question['answer'])-1:
            print('*'*4+i)
        else:
            print(' '*4+i)


def practice_sequence(ib):
    for i in ib:
        if i['familiarity'] == '100\n':
            continue
        show_one(i)
        print("'1,2,3,4' for 'a,b,c,d' 'delete' to remove")
        answer = input('Your answer:')
        if answer == i['answer']:
            change_failiarity(i, 1)
        elif answer == 'delete':
            change_failiarity(i, 10)
        elif answer == 'exit':
            return ib
        else:
            show_one_answer(i)
            change_failiarity(i, 0)
            input()
    return ib


def change_failiarity(d_question, a):
    if int(d_question['familiarity']) == 0:
        d_question['familiarity'] = '5\n'
    else:  # int(d_question['familiarity']) > 0:
        print(d_question['familiarity'])
        if a == 0:
            d_question['familiarity'] = str(int(d_question['familiarity'])-1)
        elif a == 1:
            d_question['familiarity'] = str(int(d_question['familiarity'])+1)
        elif a == 10:
            d_question['familiarity'] = '10\n'


# a = read_item_bank("企业文化.txt")
# write_item_bank('1.txt', a)
# show_all(a)
# show_one(a[1])
# input_answer('企业文化.txt')
# file_name = input('please input file name:')
file_name = '5.txt'
ib = read_item_bank(file_name)
# write_item_bank('5.txt', ib)
write_item_bank('5.txt', practice_sequence(ib))
