import os
import pickle

def input_scores():
    print('[점수 입력]')
    scores=[]
    n=1
    while True:
        a=int(input(f'#{n}? '))
        if a<0:
            print()
            break
        scores.append(a)
        n+=1
    return scores

def get_average(s):
    a=0
    for n in s:
        a+=n
    return a/len(s)

def show_scores(s):
    print('[점수 출력]\n개인점수: ',end='')
    for n in s:
        print(n,end=' ')
    print(f'\n평균: {get_average(s):.1f}')

if os.path.exists('score.bin'):
    print('[파일 읽기]\n')
    with open('score.bin', 'rb') as file:
        show_scores(pickle.load(file))
else:
    s=input_scores()
    show_scores(s)
    with open('score.bin', 'wb') as file:
        pickle.dump(s,file)
