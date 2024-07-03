import random

user_wins = 0
computer_wins = 0
draws = 0
play_again = True

while play_again:
    num = random.randint(1, 3)
    if num == 1:
        com = "가위"
    elif num == 2:
        com = "바위"
    else:
        com = "보"

    while True:
        user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ").strip().lower()
        if user_choice in ['가위', '바위', '보']:
            break
        else:
            print("유효한 입력이 아닙니다.")

    print(f"사용자: {user_choice}, 컴퓨터: {com}")

    if user_choice == com:
        print("무승부!")
        draws += 1
    elif (user_choice == '가위' and com == '보') or \
         (user_choice == '바위' and com == '가위') or \
         (user_choice == '보' and com == '바위'):
        print("사용자 승리!")
        user_wins += 1
    else:
        print("컴퓨터 승리!")
        computer_wins += 1

    while True:
        play_again_input = input("다시 하시겠습니까? (y/n): ").strip().lower()
        if play_again_input == 'y':
            break
        elif play_again_input == 'n':
            print("게임을 종료합니다.")
            play_again = False
            break
        else:
            print("잘못된 입력입니다. 다시 입력해 주세요.")

# 최종 결과 출력
print(f"승: {user_wins} 패: {computer_wins} 무승부: {draws}")