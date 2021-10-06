package test;

import java.rmi.*;
import java.rmi.server.UnicastRemoteObject;

public class ShapeListServer {
	public static void main(String args[]){
		System.setSecurityManager(new SecurityManager());
		System.out.println("Main OK");
        	try{ShapeList aShapelist = new ShapeListServant();
            System.out.println("After create");
            Naming.rebind("ShapeList", aShapelist);
            System.out.println("ShapeList server ready");
            }catch(Exception e) {
            	System.out.println("ShapeList server main " + 
        				e.getMessage());   } 
   }
}