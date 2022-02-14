import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_3040_백설_공주와_일곱_난쟁이_민상규 {
	static final int size = 9;
	static int[] input, dwarf;

	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		input = new int[size];
		dwarf = new int[7];
		for (int i = 0; i < size; i++) {
			input[i] = Integer.parseInt(in.readLine());
		}

		combination(0, 0);
	}

	public static void combination(int cnt, int start) {
		if (cnt == 7) {
			if (sum() == 100) {
				StringBuilder sb = new StringBuilder();
				for (int i : dwarf) {
					sb.append(i).append("\n");
				}
				System.out.println(sb);
			}
			return;
		}
		for (int i = start; i < size; i++) {
			dwarf[cnt] = input[i];
			combination(cnt + 1, i + 1);
		}
	}

	public static int sum() {
		int s = 0;
		for (int i : dwarf) {
			s += i;
		}
		return s;
	}
}
