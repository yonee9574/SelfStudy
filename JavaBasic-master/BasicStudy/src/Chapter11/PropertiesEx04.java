package Chapter11;

import java.util.*;

public class PropertiesEx04 {
	public static void main(String args[]) {
		Properties sysProp = System.getProperties();
		System.out.println("java.version :" + sysProp.getProperty("java.version"));
		System.out.println("user.launguage :" + sysProp.getProperty("user.launguage"));
		sysProp.list(System.out);
	}
}
