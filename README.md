# Algorithm
practice of algorithm   
<br/>
## POINT
1. 문제 보고 어떤 유형인지, 어떤 자료구조 쓸지 생각 (heapq, deque, stack, dict, set...) (시뮬, dfs, bfs, 브루트포스, dp, mst, 투포인터, 이분탐색, 위상정렬...)
2. 시간 복잡도 계산
3. 반복문 사용할 때 어떤 순서로 for문 돌지 중요하게 고민
<br/>

### bfs
* 최단거리, 최단시간, 가중치 일정
* 3중 visited 필요할 수도 있으니 조건(방향, level 등) 확인
* deque 말고 heapq 사용해서 최소조건 먼저 방문하는 로직 짜는 문제도 있음
<br/>

### 다익스트라
* 최단거리, 최단시간, 가중치 동적 변화
* 동일한곳 방문 가능하지만 최소/최대일 때만 갱신
* 처음에 시작점을 1개로 두는 것이 보편적이지만 카카오 기출 등산로 문제처럼 여러 출발지 한꺼번에 넣고 어떤 출발지 기준인지 상관없이 최단거리 구하는 문제도 있음
<br/>

### set 메소드
* update()
* union()
* intersection()
* difference()
* A.issubset(B) -> A가 B의 부분 집합인지 아닌지
* A.isdisjoint(B) -> A와 B의 교집합이 공집합인지
<br/>

### set 연산자
* | -> 합집합
* &#45; -> 차집합
* & -> 교집합
* ^ -> 대칭차집합
<br/>

### 문자 메소드
* isalpha()
* isdigit() -> '3/1' 같은 것도 숫자로 봄
* isdecimal() -> '0'~'9' 확인
* isalnum()
* upper()
* lower()
* startswith()
* endswith()
* chr() <-> ord()
* A.zfill(3) -> 왼쪽에 '0' 채워 3글자 만들기
* ''.join()
* split()
<br/>

### 배열(or 문자열) 관련
* [::-1] -> 거꾸로 (배열의 reverse())
* zip(A, B, C...) -> [a[::-1] for a in zip(*graph)] 이렇게 행렬 오른쪽 90도 변환 가능
* map(int, arr) = map(lambda x:int(x), arr) / map(lambda x:x**2, arr)
* filter(lambda x:x>5, arr)
* reduce(lambda a,b:a+b, arr, 초기값(생략가능)) -> from functools import reduce 라이브러리 import 필요
<br/>

### dict 관련
* del map['apple'] 로 key 삭제 = map.pop('apple', key 없을때 반환값)
<br/>

### Counter 메소드, 연산자
* most_common()
* == -> key와 value가 같은지 비교
* & -> 겹치면 작은 값
* | -> 겹치면 큰 값
* &#43; -> 더하기
* &#45; -> 빼기 (0 이하면 key 자동 삭제)
<br/>

### from itertools
* combinations(arr, 3)
* combinations_with_replacement(arr,3) 중복조합
* permutations(arr, 2) 순열
* product(A, B, C...) -> 다중 반복문과 동일
<br/>

### 이진법
* bin() -> 이진수 만들기 (문자열 반환)
* str() -> '0b~~' 문자열 이진수로 변환

