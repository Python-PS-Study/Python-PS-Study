import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
/*
 * 실행시간 : 131 ms
 * 메모리: 20,820 kb
 * */

public class swea1954 {

	static int[] dx = { 0, 1, 0, -1 };
	static int[] dy = { 1, 0, -1, 0 };

	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(in.readLine());

		for (int tc = 1; tc <= TC; tc++) {
			int n = Integer.parseInt(in.readLine());
			int[][] arr = new int[n][n];

			int num = 1;
			int snail = 0;
			int x = 0, y = 0;
			int nx, ny;
			
			System.out.println("#"+tc);

			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					arr[x][y] = num++;
					nx = x + dx[snail];
					ny = y + dy[snail];
					if (nx < 0 || nx >= n || ny < 0 || ny >= n || arr[nx][ny] != 0)
						snail = snail == 3 ? 0 : ++snail;
					x += dx[snail];
					y += dy[snail];
				}
			}

			for (int[] is : arr) {
				for (int is2 : is) {
					System.out.print(is2 + " ");
				}
				System.out.println();
			}

		}
		in.close();
	}

}
