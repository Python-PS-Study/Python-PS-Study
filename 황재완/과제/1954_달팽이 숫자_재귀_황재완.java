import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;

/*
실행시간: 129ms
메모리: 20,232 kb
*/
class Solution {
    private static int[] dr = {0, 1, 0, -1};
    private static int[] dc = {1, 0, -1, 0};
    private static int[][] grid;
    private static int n;

    private static void printSnail(int cnt, int r, int c, int dir) {
        // basis part
        if (cnt > n * n) return;

        // inductive part
        grid[r][c] = cnt;
        if (r + dr[dir] < 0 || r + dr[dir] >= n || c + dc[dir] < 0 || c + dc[dir] >= n || grid[r + dr[dir]][c + dc[dir]] != 0) {
            dir = (dir + 1) % 4;
        }
        printSnail(cnt + 1, r + dr[dir], c + dc[dir], dir);
    }

    public static void main(String args[]) throws Exception {

        System.setIn(new FileInputStream("input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(in.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            n = Integer.parseInt(in.readLine());
            grid = new int[n][n];
            printSnail(1, 0, 0, 0);

            // 결과 출력
            System.out.println("#" + test_case);
            for (int[] resRow : grid) {
                for (int resEl : resRow) {
                    System.out.print(resEl + " ");
                }
                System.out.println();
            }
        }
    }
}