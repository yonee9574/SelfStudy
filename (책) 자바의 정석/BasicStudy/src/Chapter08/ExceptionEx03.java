package Chapter08;

public class ExceptionEx03 {
	
	public static void main(String args[]) {
		int number = 10;
		int result = 0;
		
		for(int i=0; i<10; i++) {
			try {
				result = number / (int)(Math.random() * 10);
				System.out.println(result);
			} catch (ArithmeticException e)		{
				System.out.println("0");			// ArithmeticException 이 발생하면 실행되는 코드
			} // try-catch의 끝
		} // for의 끝
	}
}
