
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
 * 실행시간 : 193 ms
 * 메모리 : 27,580 kb
*/
class Solution {
	static int N, M, snack[];
	static int score;

	public static void main(String args[]) throws Exception {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T;
		T = Integer.parseInt(in.readLine());

		for (int test_case = 1; test_case <= T; test_case++) {
			score = -1;

			st = new StringTokenizer(in.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());

			snack = new int[N];

			st = new StringTokenizer(in.readLine());

			for (int i = 0; i < N; i++) {
				snack[i] = Integer.parseInt(st.nextToken());
			}

			f(0, 0, 0);

			System.out.printf("#%d %d\n", test_case, score);
		}
	}

	public static void f(int start, int sum, int cnt) {
		if (cnt == 2) {
			if (sum <= M)
				score = Math.max(score, sum);
			return;
		}
		for (int i = start; i < N; i++) {
			f(i + 1, sum + snack[i], cnt + 1);
		}
	}

}