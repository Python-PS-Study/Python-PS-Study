import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 메모리: 18,636 kb
// 실행시간: 106 ms
class Solution {
    public static void main(String args[]) throws Exception {

//        System.setIn(new FileInputStream("input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(in.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            int n, m;
            st = new StringTokenizer(in.readLine(), " ");
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());

            int[][] grid = new int[n][n];

            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(in.readLine(), " ");
                for (int j = 0; j < n; j++) {
                    grid[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int maxSum = 0;
            int tmpSum = 0;
            for (int i = 0; i <= n - m; i++) {
                for (int j = 0; j <= n - m; j++) {
                    tmpSum = 0;
                    for (int k = i; k < i + m; k++) {
                        for (int l = j; l < j + m; l++) {
                            tmpSum += grid[k][l];
                        }
                    }
                    if (maxSum < tmpSum)
                        maxSum = tmpSum;
                }
            }

            System.out.printf("#%d %d%n", test_case, maxSum);
        }

    }
}