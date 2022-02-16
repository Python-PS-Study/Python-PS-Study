import java.io.*;
import java.util.StringTokenizer;

/**
 * 실행시간: 80 ms
 * 메모리: 11612 KB
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

        int arrWidth = (int) Math.pow(2, N);
        answer = zSearch(0, 0, arrWidth, 0);

        bw.write(String.valueOf(answer));
        bw.flush();
    }


    static int zSearch(int r, int c, int width, int visitOrder) {
        if (r == keyR && c == keyC) return visitOrder;
        else {
            int nextWidth = width / 2; // 다음 재귀 level 에서 탐색하는 배열의 너비
            if (keyR >= r && keyR < r + nextWidth && keyC >= c && keyC < c + nextWidth)  // 왼쪽 위 영역안에 들어가는 위치라면
                return zSearch(r, c, nextWidth, visitOrder + 0 * nextWidth * nextWidth); // 왼쪽 위 탐색
            else if (keyR >= r && keyR < r + nextWidth && keyC >= c + nextWidth && keyC < c + 2 * nextWidth) // 오른쪽 위 영역안에 들어가는 위치라면
                return zSearch(r, c + nextWidth, nextWidth, visitOrder + nextWidth * nextWidth * 1); // 오른쪽 위 탐색
            else if (keyR >= r + nextWidth && keyR < r + 2 * nextWidth && keyC >= c && keyC < c + nextWidth) // 왼쪽 아래 영역안에 들어가는 위치라면
                return zSearch(r + nextWidth, c, nextWidth, visitOrder + nextWidth * nextWidth * 2); // 왼쪽 아래 탐색
            else // 오른쪽 아래 영역안에 들어가는 위치라면
                return zSearch(r + nextWidth, c + nextWidth, nextWidth, visitOrder + nextWidth * nextWidth * 3); // 오른쪽 아래 탐색
        }
    }
}