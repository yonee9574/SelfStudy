//package Chapter11;
//
//import java.util.*;
//
//public class MyVector02 extends Myvector implements Iterator {
//	int cursor = 0;
//	int lastRet = -1;
//	
//	public MyVector2(int capacity) {
//		super(capacity);
//	}
//	
//	public Myvector02() {
//		this(10);
//	}
//	
//	public String toString() {
//		String tmp = "";
//		Iterator it = iterator();
//		
//		for(int i=0; it.hasNext(); i++) {
//			if(i!=0) tmp+=", ";
//			tmp += it.next();
//		}
//		return "["+ tmp +"]";
//	}
//	
//	public Iterator iterator() {
//		cursor = 0;		// cursor와 lastRet를 초기화한다.
//		lastRet = -1;
//		return this;
//	}
//	
//	public boolean hasNext() {
//		return cursor != size();
//	}
//	
//	public Object next() {
//		Object next = get(cursor);
//		lastRet = cursor++;
//		return next;
//	}
//	
//	public void remove() {
//		// 더이상 삭제할 것이 없으면 IllegalStateException을 발생시킨다.
//		if(lastRet==-1) {
//			throw new IllegalStateException();
//		} else {
//			remove(lastRet);
//			cursor--;				// 삭제 후에 cursor의 위치를 감소시킨
//			lastRet = -1;			// lastRet의 값을 초기화 한다.
//		}
//	}
//} // class
