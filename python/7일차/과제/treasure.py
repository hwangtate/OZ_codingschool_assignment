import random

def initialize_game(board_size) -> None:
    """
    보물찾기 게임 초깃값 설정 (플레이어, 보물 위치 무작위 생성)

    :param board_size: 보드판 크기
    """
    print("=" * 50)
    print("보물을 찾으세요.")
    
    #플레이어 위치 무작위 생성
    player_position = (random.randint(0, board_size - 1), random.randint(0, board_size - 1))
    print(f"플레이어 위치: {player_position}")
    print("=" * 50)

    #보물 위치 무작위 생성(단 플레이어와 보물의 위치가 같지 않을때까지)
    while True:
        treasure_position = (random.randint(0, board_size - 1), random.randint(0, board_size - 1))
        if player_position != treasure_position:
            break
    
    #보물과의 거리 힌트 함수 호출
    calculate_distance(treasure_position, player_position)
    #플레이어 움직이는 함수 호출
    move_player(board_size, player_position, treasure_position)

def calculate_distance(treasure_position, player_position) -> None:
    """
    보물과 플레이어의 위치를 힌트로 나타내는 함수

    :param treasure_position: 보물 위치
    :param player_position: 플레이어 위치
    """
    left_distance = abs(treasure_position[0] - player_position[0])
    right_distance = abs(treasure_position[1] - player_position[1])

    print(f"힌트 보물과의 거리: ({left_distance}, {right_distance})")

def move_player(board_size, player_position, treasure_position) -> None:
    """
    플레이어 w,a,s,d로 이동하는 함수

    :param board_size: 보드판 크기
    :param player_position: 플레이어 현재 위치
    :param treasure_position: 보물 현재 위치
    """
    #이동획수 카운트 변수
    count = 0

    #플레이어 이동 반복문
    while True:
        if player_position == treasure_position:
            print("=" * 50)
            print(f"보물을 찾았습니다!\n이동횟수: {count}\n게임을 종료합니다.")
            print("=" * 50)
            break

        input_value = input("w, a, s, d를 입력하여 플레이어의 위치를 이동하세요: ").lower()
        new_player_position = list(player_position)

        if input_value == "w":
            new_player_position[0] += 1
        elif input_value == "a":
            new_player_position[1] -= 1
        elif input_value == "s":
            new_player_position[0] -= 1
        elif input_value == "d":
            new_player_position[1] += 1
        elif input_value == "종료":
            print("게임을 종료합니다.")
            break
        else:
            print("w, a, s, d를 입력해주세요.")
            continue
        
        #플레이어 보드판 넘어가기 방지 조건문
        if 0 <= new_player_position[0] < board_size and 0 <= new_player_position[1] < board_size:
            player_position = tuple(new_player_position)
            count += 1
            print(f"플레이어 위치: {player_position}")
            calculate_distance(treasure_position, player_position)
        else:
            print("보드판을 넘어갈 수 없습니다. 다시 입력해주세요.")

def play_game():
    """
    보물찾기 게임 실행
    """
    print("<보물 찾기 게임>")

    board_size = 5

    initialize_game(board_size)

# 게임 시작
if __name__ == "__main__":
    play_game()
