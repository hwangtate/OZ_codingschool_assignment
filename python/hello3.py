arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

result = [] #리스트 none값 주기
for i in range(len(arr1)): #2번 반복하라 i = 0, i = 1
    row = [] #리스트 none값 주기 , 행이라 초기화 작업
    for j in range(len(arr1[0])): #2번 반복 j = 0, j =1
        row.append(arr1[i][j] + arr2[i][j])#각 리스트 마다 첫 번쨰, 두 번쨰 열 꺼내서 더해서 행으로 만들기
    result.append(row) #열 더해서 행으로 만든 값 결과에 넣어주기

print(result)