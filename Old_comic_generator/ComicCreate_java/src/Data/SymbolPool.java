package Data;

import java.util.Map;
import java.util.TreeMap;

import BasicElement.Vector2D;
import processing.core.PApplet;
import processing.core.PImage;

/*
 * This class contains images for symbols
 */
public class SymbolPool {
	///PApplet P;
	// save image in <symbol name, img>
	Map<String, PImage> imagePool;
	Map<String, Vector2D> imageShift;
	Map<String, Float> imageSize; 
	PImage tempImage;
	
	public SymbolPool(){
		//this.P = P;
		imagePool = new TreeMap<String, PImage>();
		imageShift = new TreeMap<String, Vector2D>();
		imageSize = new TreeMap<String, Float>();
/*
		actionCategory.put("stand"	, "EIR");
		actionCategory.put("walk"	, "IL");
		actionCategory.put("run"	, "IL");
		actionCategory.put("jumpUp"	, "IL");
		actionCategory.put("fall"	, "PL");
		actionCategory.put("roll"	, "PL");
		actionCategory.put("collis"	, "P");
		actionCategory.put("dizzy"	, "R");
*/		
		
		//load images
		
		//Note: use same picture to check whether the function work
	}
	public PImage getImage(String action){
		PImage resultImage = imagePool.get(action);
		if(resultImage == null){
			return null;
		}
		else{
			return resultImage;
		}
	}
	public void putImage(String action, PImage image, float shift_x, float shift_y, float size){
		//System.out.println("in SP, "+image);
		imagePool.put(action,  image);
		imageShift.put(action, new Vector2D(shift_x, shift_y));
		imageSize.put(action, size);
		//System.out.println("in SP, "+imagePool.size());
		//showAllImage();
	}
	public void showAllImage(){
		for(String actionKey : imagePool.keySet()){
			System.out.println("in SP, "+actionKey+" : "+imagePool.get(actionKey));
		}
	}
	public Vector2D getShift(String action){
		Vector2D shift = imageShift.get(action);
		if(shift == null){
			return null;
		}
		else{
			return shift;
		}		
	}
	public float getSize(String action){
		Float symbolSize = imageSize.get(action);
		if(symbolSize == null){
			symbolSize = 1.0f;
			return 1.0f;
		}
		else{
			return symbolSize;
		}		
	}	
}
