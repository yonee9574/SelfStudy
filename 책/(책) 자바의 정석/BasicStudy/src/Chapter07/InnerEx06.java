package Chapter07;

public class InnerEx06 {
	Object iv = new Object() { void method() {} };		  // �͸�Ŭ����
	static Object cv = new Object() { void method() {} };  // �͸�Ŭ����
	
	void myMethod() {
		Object lv = new Object() { void method() {} };	  // �͸�Ŭ����
	}
}
