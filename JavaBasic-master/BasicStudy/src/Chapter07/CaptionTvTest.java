//package Chapter07;

//public class CaptionTvTest {
//	
//	public static void main(String args[]) {
//		CaptionTv ctv = new CaptionTv();
//		ctv.channel = 10;						// ���� Ŭ������ ���� ��ӹ��� ���
//		ctv.channelUp();						// ���� Ŭ������ ���� ��ӹ��� ���
//		System.out.println(ctv.channel);
//		ctv.displayCaption("Hello, world");
//		ctv.caption = true;			// ĸ��(�ڸ�) ����� �Ҵ�.
//		ctv.displayCaption("Hello, World");
//	}
//}
//
//class Tv {
//	boolean power;	// �������� (on / off)
//	int channel;	// ä��
//	
//	void power()		{	power = !power;	}
//	void channelUp()	{	++channel;		}
//	void channelDown()	{	--channel;		}
//}
//
//class CaptionTv extends Tv	{
//	boolean caption;		// ĸ�ǻ��� (on / off)
//	void displayCaption(String text)	{
//		if (caption) {	// ĸ�� ���°� on(true) �� ���� text�� �����ش�.
//			System.out.println(text);
//		}
//	}
//}
