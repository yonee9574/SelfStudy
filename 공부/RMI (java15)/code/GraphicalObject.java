package test;

import java.awt.Rectangle;
import java.awt.Color;
import java.io.Serializable;	//Serializable->동시사용자를 위한 직렬화

public class GraphicalObject implements Serializable{
	public String type;
	public Rectangle enclosing;
    public Color line;
    public Color fill;
	public boolean isFilled;
	public GraphicalObject() { }
	public GraphicalObject(String aType, Rectangle anEnclosing, Color aLine,Color aFill, boolean anIsFilled) {
		type = aType;
		enclosing = anEnclosing;
		line = aLine;
		fill = aFill;
		isFilled = anIsFilled;
		}
	public void print(){
		System.out.println("도형 : "+type);
		System.out.print("속성 : "+enclosing.x + " , " + enclosing.y 
				+ " , " + enclosing.width + " , "  + enclosing.height);
		if(isFilled)
			System.out.println("- filled");
		else 
			System.out.println("not filled");
		}
	}