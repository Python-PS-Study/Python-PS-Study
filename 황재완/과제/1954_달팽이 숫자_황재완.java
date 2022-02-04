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

    public static void main(String args[]) throws Exception {

//        System.setIn(new FileInputStream("input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(in.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            int n = Integer.parseInt(in.readLine());
            int[][] res = new int[n][n];
            int r = 0, c = 0;
            int pastDir = 0; // 이전 방향
            for (int cnt = 1; cnt <= n * n; cnt++) {
                res[r][c] = cnt;
                int nextR, nextC;
                nextR = r + dr[pastDir];
                nextC = c + dc[pastDir];
                if (0 <= nextR && nextR < n && 0 <= nextC && nextC < n && res[nextR][nextC] == 0) {
                    r = nextR;
                    c = nextC;
                    continue;
                } else {
                    for (int l = 0; l < 4; l++) {
                        if (l == pastDir) continue;
                        nextR = r + dr[l];
                        nextC = c + dc[l];
                        if (0 <= nextR && nextR < n && 0 <= nextC && nextC < n && res[nextR][nextC] == 0) {
                            r = nextR;
                            c = nextC;
                            pastDir = l;
                            break;
                        }
                    }
                }

            }
            // 결과 출력
            System.out.println("#" + test_case);
            for (int[] resRow : res) {
                for (int resEl : resRow) {
                    System.out.print(resEl + " ");
                }
                System.out.println();
            }
        }


    }
}