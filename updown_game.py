import random


def game():
    print("업다운숫자게임")
    play_again = True
    best_attempt = None

    while play_again:
        target_number = random.randint(1, 100)
        attempts = 0
        print(f"이전 게임 플레이어 최고 시도 횟수: {best_attempt if best_attempt else '없음'}")

        while True:
            try:
                user_number = int(input("1에서 100 사이 숫자를 입력하세요: "))
                if user_number < 1 or user_number > 100:
                    print("유효한 범위 내의 숫자를 입력하세요.")
                    continue

                attempts += 1

                if user_number < target_number:
                    print("업")
                elif user_number > target_number:
                    print("다운")
                else:
                    print("맞았습니다!")
                    print(f"시도한 횟수: {attempts}")

                    if best_attempt is None or attempts < best_attempt:
                        best_attempt = attempts

                    break

            except ValueError:
                print("숫자를 입력해주세요.")

        while True:
            play_again_input = input("다시 하시겠습니까? (y/n): ").strip().lower()
            if play_again_input == 'y':
                break
            elif play_again_input == 'n':
                print("게임종료")
                play_again = False
                break
            else:
                print("잘못된 입력입니다. 다시 입력해 주세요.")


if __name__ == "__main__":
    game()
