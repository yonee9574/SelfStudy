//package Chapter07;
//
//import Chapter06.Card;
//
//public class CastingTest01 {
//	
//	public static void main(String args[]) {
//		Car car = null;
//		FireEngine fe = new FireEngine();
//		FireEngine fe2 = null;
//		
//		fe.water();
//		car = fe;	// car = (car)fe; ���� ����ȯ�� ������ �����̴�.
////		car.water(); �����Ͽ���!!! CarŸ���� ���������δ� Water()�� ȣ���� �� ����. 
//		fe2 = (FireEngine)car; // �ڼ�Ÿ�� <- ����Ÿ��
//		fe2.water();
//	}
//}
//
//class Car {
//	String color;
//	int door;
//	
//	void drive() {		// �����ϴ� ���
//		System.out.println("drive, Brrrr~");
//	}
//	
//	void stop() {		// ���ߴ� ���
//		System.out.println("stop!!!");
//	}
//}
//
//class FireEngine extends Car {	// �ҹ���
//	
//	void water() {		// ���� �Ѹ��� ���
//		System.out.println("water!!!");
//	}
//}
