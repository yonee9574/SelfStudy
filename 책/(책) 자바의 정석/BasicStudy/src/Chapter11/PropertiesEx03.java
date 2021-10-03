package Chapter11;

import java.util.*;
import java.io.*;

public class PropertiesEx03 {
	public static void main(String args[]) {
		Properties prop = new Properties();
		
		prop.setProperty("timeout", "30");
		prop.setProperty("language", "ÇÑ±Û");
		prop.setProperty("size", "10");
		prop.setProperty("capacity", "10");
		
		try {
			prop.store(new FileOutputStream("C:\\IDE\\java\\BasicStudy\\src\\Chapter11\\output.txt"), "Properties Example");
			prop.storeToXML(new FileOutputStream("C:\\IDE\\java\\BasicStudy\\src\\Chapter11\\output.xml"), "Properties Example");
		} catch(IOException e) {
			e.printStackTrace();
		}
	}

}
