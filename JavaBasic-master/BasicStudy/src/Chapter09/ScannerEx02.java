package Chapter09;

import java.util.Scanner;
import java.io.File;

public class ScannerEx02 {
	public static void main(String args[]) throws Exception {
		Scanner sc = new Scanner(new File("C:\\IDE\\java\\BasicStudy\\src\\Chapter09\\data2.txt"));
		int sum = 0;
		int cnt = 0;
		
		while (sc.hasNextInt()) {
			sum += sc.nextInt();
			cnt++;
		}
		
		System.out.println("sum="+sum);
		System.out.println("average="+ (double)sum/cnt);
	}
}
