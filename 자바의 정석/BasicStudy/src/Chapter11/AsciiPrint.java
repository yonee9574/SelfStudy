package Chapter11;

public class AsciiPrint {
	public static void main(String args[]) {
		char ch = ' ';
		// ����(' ')������ ���ڵ��� ����Ѵ�.
		for(int i=0; i < 95; i++)
			System.out.print(ch++);
	}

}
