package test;

//�������̽� ����
import java.rmi.*;
import java.util.Vector;

//Vector->�迭�� ���� ��ü ���尡�� Ŭ����
public interface ShapeList extends Remote {
	//method ����
	Shape newShape(GraphicalObject g) throws RemoteException;
	Vector allShapes() throws RemoteException;
	int getVersion() throws RemoteException;
	//�޼ҵ� �߰� �� ShapeListServant���� �ش� �޼ҵ� ����
	String test() throws RemoteException;
	}