//package Chapter12;
//
//import java.util.ArrayList;
//
//class NewClass {
//	int newField;
//	
//	int getNewField() {
//		return newField;
//	}
//		@Deprecated
//		int oldField;
//		
//		@Deprecated
//		int getOldField() {
//			return oldField;
//		}
//	}
//	
//	class AnnotationEx03 {
//		@SuppressWarnings("deprecation")					// deprecation���� ��� ����
//		public static void main(String args[]) {
//			NewClass nc = new NewClass();
//			
//			nc.oldField = 10;								//@Deprecated�� ���� ����� ���
//			System.out.println(nc.getOldField());			//@Deprecated�� ���� ����� ���
//			
//			@SuppressWarnings("unchecked")					// ���׸��� ���� ��� ����
//			ArrayList<NewClass> list = new ArrayList();		// Ÿ���� �������� ����.
//			list.add(nc);
//		}
//	}
