package test;

//인터페이스 선언
import java.rmi.*;
import java.util.Vector;

//Vector->배열과 같이 객체 저장가능 클래스
public interface ShapeList extends Remote {
	//method 선언
	Shape newShape(GraphicalObject g) throws RemoteException;
	Vector allShapes() throws RemoteException;
	int getVersion() throws RemoteException;
	//메소드 추가 후 ShapeListServant에서 해당 메소드 구현
	String test() throws RemoteException;
	}