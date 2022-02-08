import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
/*
실행시간: 142 ms
메모리: 22,884 kb
*/
class Solution {
    private static int N, M;
    private static int[] weights;
    private static int maxSum;

    private static void DFS(int cnt, int start, int sum) {
        if (cnt == 2) {
            if(sum > maxSum) maxSum = sum;
            return;
        }
        for (int i = start; i < N; i++) {
            if(sum+weights[i] <= M) {
                sum += weights[i];
                DFS(cnt+1, i+1, sum);
                sum -= weights[i];
            }
        }
    }

    public static void main(String args[]) throws Exception {

//        System.setIn(new FileInputStream("input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(in.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            st = new StringTokenizer(in.readLine(), " ");
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(in.readLine(), " ");
            weights = new int[N];
            for (int i = 0; i < N; i++) {
                weights[i] = Integer.parseInt(st.nextToken());
            }
            maxSum = -1; // 들고갈 방법이 없을때는 -1을 출력하므로 테스트 케이스 마다 -1로 초기화
            DFS(0, 0, 0);
            sb.append("#" + test_case + " ").append(maxSum).append('\n');
        }
        System.out.print(sb);
    }
}