package Chapter09;

public class StringEx06 {
	
	public static void main(String args[]) {
		int iVal = 100;
		String strVa1 = String.valueOf(iVal);	// int를 String으로 변환한다.
		
		double dVal = 200.0;
		String strVa12 = dVal + "";		//int를 String으로 변환하는 또 다른 방법
		
		double sum = Integer.parseInt("+"+strVa1) + Double.parseDouble(strVa12);
		double sum2 = Integer.valueOf(strVa1) + Double.parseDouble(strVa12);
		
		System.out.println(String.join("",strVa1,"+",strVa12,"=")+sum);
		System.out.println(strVa1+"+"+strVa12+"="+sum2);
	}

}
