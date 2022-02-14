import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 시간 : 108 ms
// 메모리 : 18,312 kb
class Test {
	static int n, m;
	static int[][] arr;
	static int sum;
	static int answer;

	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int TC = Integer.parseInt(in.readLine());

		for (int tc = 1; tc <= TC; tc++) {
			st = new StringTokenizer(in.readLine(), " ");
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());

			arr = new int[n][n];

			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(in.readLine(), " ");
				for (int j = 0; j < n; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}

			answer = 0;

			for (int i = 0; i <= n - m; i++) {
				for (int j = 0; j <= n - m; j++) {
					sum = 0;
					for (int r = 0; r < m; r++) {
						for (int c = 0; c < m; c++) {
							sum += arr[i + r][j + c];
						}
					}
					answer = sum > answer ? sum : answer;
				}
			}

			System.out.printf("#%d %d\n", tc, answer);
		}
		in.close();

	}

}
