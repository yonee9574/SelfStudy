package Chapter08;

public class FinallyTest03 {
	
	public static void main(String args[]) {
		// Method1 () �� static �޼����̹Ƿ� �ν��Ͻ� �������� ���� ȣ���� �����ϴ�.
		FinallyTest03.method1();
		System.out.println("method1()�� ������ ��ġ�� main �޼���� ���ƿԽ��ϴ�.");
	} 	// main �޼����� ��
	
	static void method1() {
		try {
			System.out.println("method1() �� ȣ��Ǿ����ϴ�.");
			return;		// ���� ���� ���� �޼��带 �����Ѵ�.
		} catch (Exception e)		{
			e.printStackTrace();
		} finally {
			System.out.println("method1 ()dml finally ���� ����Ǿ����ϴ�.");
		}
	} // method1 �޼����� ��

}
