import sys
import secrets
from random import shuffle
from time import sleep

candidates_filename = 'candidates.txt'

if len(sys.argv) > 1:
    candidates_filename = sys.argv[1]

def dot_every(sec, times):
    for _ in range(times):
        dot_and_wait(sec)

def dot_and_wait(sec):
    print('.', end='', flush=True)
    sleep(sec)

def main():
    while True:
        print('1. 발표자 명단 확인')
        print('2. 발표자 순서뽑기')
        print('3. 발표자 뽑기')
        print('4. 종료')
        choice = input('실행할 작업을 선택하세요: ')
        print(choice)

        if choice == '1':
            try:
                with open('candidates.txt', 'r', encoding='utf-8') as f:
                    candidates = [line.rstrip('\n') for line in f]
                    print('[발표자 명단 - 총원 {}명]'.format(len(candidates)))
                    print(str(', '.join(candidates)))
            except FileNotFoundError:
                print('candidates.txt 파일이 존재하지 않습니다.')

        elif choice == '2':
            try:
                with open('candidates.txt', 'r', encoding='utf-8') as f:
                    candidates = [line.rstrip('\n') for line in f]

                    print('[발표자 명단 - 총원 {}명]'.format(len(candidates)))
                    print(str(', '.join(candidates)))
                    print()

                    shuffle(candidates)

                    input('Enter를 눌러 진행하세요.')
                    print()

                    for i in range(len(candidates)):
                        print('다음 발표자는...', end='', flush=True)
                        input()
                        print('"{}"님 입니다!'.format(candidates[i]))
                        print()
            except FileNotFoundError:
                print('Candidates file specified not found: {}'.format(candidates_filename))
                sys.exit(1)

        elif choice == '3':
            try:
                with open('candidates.txt', 'r', encoding='utf-8') as f:
                    candidates = [line.rstrip('\n') for line in f]

                    print('[발표자 명단 - 총원 {}명]'.format(len(candidates)))
                    print(str(', '.join(candidates)))
                    print()

                    input('Enter를 눌러 진행하세요.')
                    print()

                    print('발표자는', end='', flush=True)
                    dot_every(0.5, 5)

                    input()

                    rand = secrets.randbelow(len(candidates))
                    print('"{}"님 입니다!'.format(candidates[rand]))
            except FileNotFoundError:
                print('Candidates file specified not found: {}'.format(candidates_filename))
                sys.exit(1)

        elif choice == '4':
            break

        else:
            print('잘못된 입력입니다. 다시 시도해주세요.')

if __name__ == '__main__':
    main()