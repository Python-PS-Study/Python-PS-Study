import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 소요시간 : 104ms
// 메모리사용량 : 18,660 kb
class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(in.readLine());

		for (int tc = 1; tc <= TC; tc++) {
			String bin = in.readLine();

			int count = 0;
			char isOn = '0';
			for (char bit : bin.toCharArray()) {
				if (bit != isOn) {
					count++;
					isOn = isOn == '1' ? '0' : '1';
				}
			}
			System.out.printf("#%d %d\n", tc, count);
		}
		in.close();

	}

}
