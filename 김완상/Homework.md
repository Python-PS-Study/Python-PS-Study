# Java

## 🎴Homework

### 22-02-06(월) 괄호 짝짓기

SW, D4 1218. 괄호 짝짓기

```java
import java.io.FileInputStream;
import java.util.Scanner;
import java.util.Stack;

class CheckBracket {

    static int T, N, answer;
    static StringBuilder sb = new StringBuilder();
    static Stack<Character> stack = new Stack<Character>();

    public static void main(String args[]) throws Exception {

        System.setIn(new FileInputStream("input.txt"));
        Scanner sc = new Scanner(System.in);
        T = 10;

        for (int test_case = 1; test_case <= T; test_case++) {
            answer = 1;
            stack.clear();
            sb.setLength(0);
            N = Integer.parseInt(sc.nextLine());
            sb.append(sc.nextLine());
//            System.out.println(N);
//            System.out.println(sb);
            for (char c : sb.toString().toCharArray()) {
                if (c == '(' || c == '[' || c == '{' || c == '<') {
                    stack.push(c);
                } else if (c == ')') {
                    if (!stack.isEmpty() && stack.pop() == '(') {
                        continue;
                    } else {
                        answer = 0;
                        break;
                    }
                } else if (c == ']') {
                    if (!stack.isEmpty() && stack.pop() == '[') {
                        continue;
                    } else {
                        answer = 0;
                        break;
                    }
                } else if (c == '}') {
                    if (!stack.isEmpty() && stack.pop() == '{') {
                        continue;
                    } else {
                        answer = 0;
                        break;
                    }
                } else if (c == '>') {
                    if (!stack.isEmpty() && stack.pop() == '<') {
                        continue;
                    } else {
                        answer = 0;
                        break;
                    }
                }
            }

            if (!stack.isEmpty()) {
                answer = 0;
            }

            System.out.printf("#%d %d\n", test_case, answer);
        }

        sc.close();
    }

}
```

### 22-02-04(금) 파리 퇴치

SW, D2 2001. 파리 퇴치

```java
import java.util.Scanner;
import java.io.FileInputStream;

class CatchFlies {
    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("input.txt"));
        Scanner sc = new Scanner(System.in);
        int T, N, M, temp, answer;
        int[][] arr;
        T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            N = sc.nextInt();
            M = sc.nextInt();
            arr = new int[N][N];
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                    arr[r][c] = sc.nextInt();
                }
            }
            answer = 0;
            for (int r = 0; r < N - M + 1; r++) {
                for (int c = 0; c < N - M + 1; c++) {
                    temp = 0;
                    for (int i = 0; i < M; i++) {
                        for (int j = 0; j < M; j++) {
                            temp += arr[r + i][c + j];
                        }
                    }
                    if (temp > answer) {
                        answer = temp;
                    }
                }
            }

            System.out.printf("#%d %d\n", test_case, answer);

//            for (int r = 0; r < N; r++) {
//                for (int c = 0; c < N; c++) {
//                    System.out.print(arr[r][c] + " ");
//                }
//                System.out.println();
//            }
        }
        sc.close();
    }
}
```

### 22-02-03(목) 달팽이 숫자

SW, D2 1954. 달팽이 숫자

```java
package Homework;

import java.util.Scanner;
import java.io.FileInputStream;

class SnailNumber {
    public static void main(String args[]) throws Exception {

        System.setIn(new FileInputStream("input.txt"));
        Scanner sc = new Scanner(System.in);

        int T, N, now, r, c, d;
        int[][] arr;
        int[] dr = { 0, 1, 0, -1 };
        int[] dc = { 1, 0, -1, 0 };
        T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            N = sc.nextInt();
            arr = new int[N][N];
            now = 1;
            r = 0;
            c = 0;
            d = 0;
            arr[r][c] = now;
            while (now < N * N) {
                r += dr[d];
                c += dc[d];
                if (r < 0 || c < 0 || c >= N || r >= N || arr[r][c] != 0) {
                    r -= dr[d];
                    c -= dc[d];
                    d = (d + 1) % 4;
                    continue;
                }
                arr[r][c] = ++now;
            }

            System.out.println("#" + test_case);
            for (int[] line : arr) {
                for (int i : line) {
                    System.out.printf("%d ", i);
                }
                System.out.println();
            }

        }
        sc.close();
    }
}
```

## 🎴Exercise

### 22-02-06(월) 햄버거 그냥 먹자

SW, D3 5215. 햄버거 다이어트

```java
import java.util.Scanner;
import java.io.FileInputStream;

class HamburgerDiet {

    static int bestScore = 0;
    static int T, N, L;
    static int arr[][];

    public static void main(String args[]) throws Exception {

        System.setIn(new FileInputStream("input.txt"));
        Scanner sc = new Scanner(System.in);
        T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            N = sc.nextInt();
            L = sc.nextInt();
            arr = new int[N][2];

            for (int i = 0; i < arr.length; i++) {
                arr[i][0] = sc.nextInt();
                arr[i][1] = sc.nextInt();
            }

            bestScore = 0;


//          for (int i = 0; i < N; i++) {
//              for (int j = 0; j < 2; j++) {
//                  System.out.print(arr[i][j] + " ");
//              }
//              System.out.println();
//          }

            getBestHamburger(0, 0, 0);

            System.out.printf("#%d %d\n", test_case, bestScore);
        }
        
        sc.close();
        
    }
        
    public static void getBestHamburger(int cur, int score, int calorie) {
        if (calorie > L || cur >= N) {
            return;
        }

        int newScore = score + arr[cur][0];
        int newCalorie = calorie + arr[cur][1];
        if (newCalorie <= L && newScore > bestScore) {
            bestScore = newScore;
        }

        getBestHamburger(cur+1, score, calorie);
        getBestHamburger(cur+1, newScore, newCalorie);

    }

}
```

### 22-02-04(금) 재귀함수가 뭔가요?

BJ, 실5 17478. 재귀함수가 뭔가요?

```java
// 풀이중
```

### 22-02-04(금) 상호야 배틀필드 캐삭하자

SW, D3 1873. 상호의 배틀필드

```java
package Exercise;

import java.util.Scanner;
import java.io.FileInputStream;

class SanghoBattleField {
    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("input.txt"));
        Scanner sc = new Scanner(System.in);
        int[] dh = { -1, 1, 0, 0 };
        int[] dw = { 0, 0, -1, 1 };
        int T;
        T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            // 맵 다운로드
            int UP = 0, DOWN = 1, LEFT = 2, RIGHT = 3;
            int tankH = 0;
            int tankW = 0;
            int tankDir = 0;

            int H = sc.nextInt();
            int W = sc.nextInt();
            char[][] map = new char[H][W];
            for (int h = 0; h < H; h++) {
                String temp = sc.next();
                for (int w = 0; w < W; w++) {
                    map[h][w] = temp.charAt(w);
                    if (temp.charAt(w) == '<') {
                        tankH = h;
                        tankW = w;
                        tankDir = LEFT;
                    } else if (temp.charAt(w) == '>') {
                        tankH = h;
                        tankW = w;
                        tankDir = RIGHT;
                    } else if (temp.charAt(w) == '^') {
                        tankH = h;
                        tankW = w;
                        tankDir = UP;
                    } else if (temp.charAt(w) == 'v') {
                        tankH = h;
                        tankW = w;
                        tankDir = DOWN;
                    }
                }
            }
//            System.out.println(tankH + " " + tankW + " " + tankDir);
    
            // 액션 횟수 입력
            int N = sc.nextInt();

            // 액션하기
            char[] actions = sc.next().toCharArray();
            for (char c : actions) {
                if (c == 'S') {
                    int firedH = tankH;
                    int firedW = tankW;
                    while (true) {
                        firedH += dh[tankDir];
                        firedW += dw[tankDir];
                        if (firedH < 0 || firedW < 0 || firedH >= H || firedW >= W || map[firedH][firedW] == '#') {
                            break;
                        }
                        if (map[firedH][firedW] == '*') {
                            map[firedH][firedW] = '.';
                            break;
                        }
                    }
                } else {
                    if (c == 'U') {
                        tankDir = UP;
                        map[tankH][tankW] = '^';
                    } else if (c == 'D') {
                        tankDir = DOWN;
                        map[tankH][tankW] = 'v';
                    } else if (c == 'L') {
                        tankDir = LEFT;
                        map[tankH][tankW] = '<';
                    } else if (c == 'R') {
                        tankDir = RIGHT;
                        map[tankH][tankW] = '>';
                    }
                    // 새로운 좌표
                    int nH = tankH + dh[tankDir];
                    int nW = tankW + dw[tankDir];
                    // 이동 불가능하면?(범위를 벗어나거나 평지가 아니면)
                    if (nH < 0 || nW < 0 || nH >= H || nW >= W || map[nH][nW] != '.') {
//                        System.out.println(nh + " " + nw);
                        continue;
                    }
                    // 이동 가능하면? swapping
                    char temp = map[tankH][tankW];
                    map[nH][nW] = temp;
                    map[tankH][tankW] = '.';
                    tankH = nH;
                    tankW = nW;
//                    for (int h = 0; h < H; h++) {
//                        for (int w = 0; w < W; w++) {
//                            System.out.print(map[h][w]);
//                        }
//                        System.out.println();
//                    }

                }

            }

            // 출력
            System.out.printf("#%d ", test_case);
            for (int h = 0; h < H; h++) {
                for (int w = 0; w < W; w++) {
                    System.out.print(map[h][w]);
                }
                System.out.println();
            }
        }
        
        sc.close();
    }
}
```

### 22-02-03(목) 원재야 메모리관리 잘하자

SW, D3 1289. 원재의 메모리 복구하기

```java
import java.io.FileInputStream;
import java.util.Scanner;

class WonjaeRecoveryMemory {
    public static void main(String args[]) throws Exception {

        System.setIn(new FileInputStream("input.txt"));
        Scanner sc = new Scanner(System.in);
        int T, count;
        boolean status;
        T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            count = 0;
            status = true;  // true -> 현재 상태 1, false는 현재 상태 0
            String memory = sc.next();
            for (char c : memory.toCharArray()) {
                // 핵심 알고리즘 
                // if first num is 1 -> count = 1;
                // if toggle -> count++ and toggle status
                if (status == (c == '1')) {
                    count++;
                    status = !status;
                }
            }
            System.out.printf("#%d %d\n", test_case, count);
        }
        sc.close();
    }
}
```
