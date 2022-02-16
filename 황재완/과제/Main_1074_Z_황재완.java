import java.io.*;
import java.util.StringTokenizer;

/**
 * 실행시간: 76 ms
 * 메모리: 11652 KB
 */
public class Main {
    static int N, answer;
    static int keyR, keyC; // 문제에서 찾으려는 R행 C열

    public static void main(String args[]) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        keyR = Integer.parseInt(st.nextToken());
        keyC = Integer.parseInt(st.nextToken());

        answer = zSearch(0, N, 0, 0);

        bw.write(String.valueOf(answer));
        bw.flush();
    }


    // 재귀적으로 사분탐색을 수행, 타겟 위치의 방문 순서를 리턴
    // visit: 현재 방문하는 위치의 탐색 순서
    // level: 재귀 레벨
    // r, c: 현재 위치
    static int zSearch(int visit, int level, int r, int c) {
        // 현재 탐색하는 원소가 타겟 위치라면
        // 문제에서 요구하는 행과 열의 원소에 대한 방문 횟수 저장
        if (r == keyR && c == keyC) return visit;
        else {
            int nextLevel = level - 1; // 다음 재귀 level
            int l = (int) Math.pow(2, nextLevel); // 다음 재귀 level 에서 탐색하는 배열의 너비

            if (keyR >= r && keyR < r + l && keyC >= c && keyC < c + l)  // 왼쪽 위 영역안에 들어가는 위치라면
                return zSearch(visit + 0 * l * l, nextLevel, r, c); // 왼쪽 위 탐색
            else if (keyR >= r && keyR < r + l && keyC >= c + l && keyC < c + 2 * l) // 오른쪽 위 영역안에 들어가는 위치라면
                return zSearch(visit + 1 * l * l, nextLevel, r, l + c); // 오른쪽 위 탐색
            else if (keyR >= r + l && keyR < r + 2 * l && keyC >= c && keyC < c + l) // 왼쪽 아래 영역안에 들어가는 위치라면
                return zSearch(visit + 2 * l * l, nextLevel, r + l, c); // 왼쪽 아래 탐색
            else // 오른쪽 아래 영역안에 들어가는 위치라면
                return zSearch(visit + 3 * l * l, nextLevel, r + l, l + c); // 오른쪽 아래 탐색
        }
    }
}