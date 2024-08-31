package BasicElement;

import Data.ActionPool;
import Data.SymbolPool;
import processing.core.PApplet;

public class GlobalSettings {
	/*
	 * constants
	 */
	
	static PApplet P;
	
	public GlobalSettings(PApplet P){
		this.P = P;
	}
	//block representation
	public static final int LEFT = 1;
	public static final int MIDDLE = 2;
	public static final int RIGHT = 3;
	public static final int LOW = 2;
	public static final int HIGH = 1;
	
	public static final int FACE_RIGHT = 1;
	public static final int FACE_LEFT = -1;
	public static final int NO_DIRECTION = 0;
	
	/*
	 * environment settings
	 */
	public static final int SCREEN_WIDTH = 700;
	public static final int SCREEN_HEIGHT = 500;
	
	public static final int BLOCK_WIDTH = 50;
	public static final int BLOCK_HEIGHT = 50;
	
	public static final int PANEL_WIDTH = BLOCK_WIDTH*3;
	public static final int PANEL_HEIGHT = BLOCK_HEIGHT*2;
	
	public static final int CHARA_SIZE = BLOCK_WIDTH;
	public static final int MAX_CHARACTER = 1;
	
	public static final int EXPAND_FRACTION = 5;
	
	public static final int PANEL_ONE_LINE = (int)(SCREEN_WIDTH/PANEL_WIDTH);
	
	public static final boolean SYMBOL_ALLOW = true;
	
	public static final boolean STRUCTURE_ALLOW = true;
	public static final boolean RELATION_ALLOW = true;
	//Global variables
	public static ActionPool AP = new ActionPool();

	public static SymbolPool SP = new SymbolPool();
}
