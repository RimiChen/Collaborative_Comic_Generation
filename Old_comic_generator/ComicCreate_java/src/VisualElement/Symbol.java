package VisualElement;

public class Symbol implements VisualElement{
	String currentSymbol = "";
	
	@Override
	public void display() {
		// TODO Auto-generated method stub
		
	}
	public void assignSymbol(String symbolName){
		//read in symbol string, and draw accordingly
		this.currentSymbol = symbolName; 
	}
}
