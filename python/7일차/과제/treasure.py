import random

# 게임 초기화
def initialize_game(n):
    print("=" * 50)
    #보드크기 출력
    board = (n, n)
    print(f"보물을 찾으세요.")

    #플레이어 위치 무작위 생성
    player_left = random.randint(0, n) #n이 보드판
    player_right = random.randint(0, n)
    player_position = (player_left, player_right)
    print(f"플레이어 위치 : {player_position}")

    #보물 위치 무작위 생성
    treasure_left = random.randint(0,n)
    treasure_right = random.randint(0,n)
    treasure_position = (treasure_left, treasure_right)
    
    print("=" * 50)
    #플레이어와 보물의 위치가 같을때 게임 재시작
    if player_position == treasure_position:
        print(f"플레이어와 보물의 위치가 같은 곳에 생성되어 게임을 재시작 합니다.")
        play_game(board_size)

    calculate_distance(treasure_position, player_position)
    move_player(board_size, player_position, treasure_position)
    
# 거리 계산
def calculate_distance(treasure_position, player_position):
    
    left_distance = abs(treasure_position[0] - player_position[0])
    right_distance = abs(treasure_position[1] - player_position[1])

    print(f"힌트 보물과의 거리 : {left_distance, right_distance}")

# 플레이어 이동
def move_player(board_size, player_position, treasure_position):

    #보드판 넘어가기 방지 함수
    def not_board(board_size, player_position):
        if player_position[0] > (board_size):
            print("보드판을 넘어갈 수 없습니다.")
            print("게임을 종료합니다.")
            return True

        elif player_position[0] < (0):
            print("보드판을 넘어갈 수 없습니다.")
            print("게임을 종료합니다.")
            return True
        
        elif player_position[1] > (board_size):
            print("보드판을 넘어갈 수 없습니다.")
            print("게임을 종료합니다.")
            return True
        
        elif player_position[1] < (0):
            print("보드판을 넘어갈 수 없습니다.")
            print("게임을 종료합니다.")
            return True
        
        else:
            return False

    count = 0

    while True:

        if player_position != treasure_position:

            if not not_board(board_size, player_position):

                input_value = input("w, a, s, d 를 입력해여 플레이어의 위치를 이동하세요. : ").lower() 
                
                player_position = list(player_position)

                if input_value == "w":
                    player_position[0] += 1
                    count += 1
                    player_position = tuple(player_position)
                    print(f"플레이어 위치 : {player_position}")
                    calculate_distance(treasure_position, player_position)

                elif input_value == "a":
                    player_position[1] -= 1
                    count += 1
                    player_position = tuple(player_position)
                    print(f"플레이어 위치 : {player_position}")
                    calculate_distance(treasure_position, player_position)

                elif input_value == "s":
                    player_position[0] -= 1
                    count += 1
                    player_position = tuple(player_position)
                    print(f"플레이어 위치 : {player_position}")
                    calculate_distance(treasure_position, player_position)

                elif input_value == "d":
                    player_position[1] += 1
                    count += 1
                    player_position = tuple(player_position)
                    print(f"플레이어 위치 : {player_position}")
                    calculate_distance(treasure_position, player_position)

                elif input_value == "종료":
                    print("게임을 종료합니다.")
                    break

                else:
                    print("w, a, s, d를 입력해주세요.")
            else:
                break

        elif player_position == treasure_position:
            print("=" * 50)
            print(f"보물을 찾았습니다!\n이동횟수 : {count}\n게임을 종료합니다.")
            print("=" * 50)
            break


# 게임 실행
def play_game(board_size):

    print("<보물 찾기 게임>")

    initialize_game(board_size)

# 게임 보드 크기 설정 및 게임 시작
if __name__ == "__main__":
    board_size = 5  # 보드 크기를 5x5로 설정
    play_game(board_size)



"""
아쉬운점 : 보드판을 넘어갔을때의 방지함수를 if문이 아닌 각 개별의 조건문에다 넣었으면 보드판을 넘어갔을때 이동횟수도 카운트 하지 않고 플레이어 위치도 이동되지 않게 할 수 있지만
지금 제 실력으로는 그렇게 한다면 코드가 길어지고 더 보기 어려워져서 그렇게 까진 안했음
"""