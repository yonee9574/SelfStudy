package Chapter09;

public class StringEx06 {
	
	public static void main(String args[]) {
		int iVal = 100;
		String strVa1 = String.valueOf(iVal);	// int�� String���� ��ȯ�Ѵ�.
		
		double dVal = 200.0;
		String strVa12 = dVal + "";		//int�� String���� ��ȯ�ϴ� �� �ٸ� ���
		
		double sum = Integer.parseInt("+"+strVa1) + Double.parseDouble(strVa12);
		double sum2 = Integer.valueOf(strVa1) + Double.parseDouble(strVa12);
		
		System.out.println(String.join("",strVa1,"+",strVa12,"=")+sum);
		System.out.println(strVa1+"+"+strVa12+"="+sum2);
	}

}
