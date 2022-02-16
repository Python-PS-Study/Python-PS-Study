import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 실행시간: 80 ms
 * 메모리: 11612 KB
 */
public class Main {
    static int N, total_area;
    static int[][] canvas = new int[100][100];
    public static void main(String args[]) throws Exception {

//        System.setIn(new FileInputStream("input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(in.readLine());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(in.readLine(), " ");
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            for (int r = y; r < y + 10; r++) {
                for (int c = x; c < x + 10; c++) {
                    canvas[r][c] = 1;
                }
            }
        }

        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                total_area += canvas[i][j];
            }
        }
        System.out.println(total_area);
    }
}