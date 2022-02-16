
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
	static int N, a, b;
	static int paper[][] = new int[100][100];

	public static void main(String args[]) throws Exception {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		N = Integer.parseInt(in.readLine());

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(in.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			for (int j = a; j < a + 10; j++) {
				for (int j2 = b; j2 < b + 10; j2++) {
					paper[j][j2] = 1;
				}
			}
		}

		int cnt = 0;
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				cnt += paper[i][j];
			}
		}

		System.out.println(cnt);
	}

}