package Structure;
import java.util.ArrayList;
import java.util.List;
import java.util.Vector;

import BasicElement.GlobalSettings;
import BasicElement.PositionInPanel;
import BasicElement.RGBA;
import BasicElement.Vector2D;
import Data.ActionPool;
import Data.CharaState;
import VisualElement.CharacterObject;
import processing.core.PApplet;
/*
 * Each node is belongs to a narrative category.
 * A structure tree is composed by structure nodes, and the leaf node are panels.
 * so, this node should also contains the information about content in the panels
 */
public class StructureNode {
	// I: Initial, E: Establisher, L: Prolongation, P: Peak, R: Release
	public String category;
	public List<StructureNode> childList;
	public boolean isWentThrough = false;
	public int currentLevel = 0;//tree layer
	public PApplet p;
	public ArrayList<CharacterObject> characters = new ArrayList<CharacterObject>();
	
	
	//character name, should be string
	public Vector characterSet;
	
	
	public StructureNode(PApplet p){
		this.p = p;
		childList = new ArrayList<StructureNode>();
	}
	
	/*
	 * check if this is a leaf node
	 */
	public boolean checkLeaf(){
		boolean isLeaf = false;
		if(childList.size() == 0){
			isLeaf = true;
		}
		return isLeaf;
	}
	/*
	 * get structure list
	 */
	public void getStructureByIndex(int index, StructureMap map){
		Vector targetV = map.phaseMap.get(index);
		for(int i =0; i < targetV.size(); i++){
			StructureNode newNode = new StructureNode(p);
			newNode.category = (String) targetV.get(i);
			childList.add(newNode);
		}
	}
	/*
	 * print all node in childList
	 */
	public void showAllChild(){
		
		System.out.print("( level "+currentLevel+" , " +category+",");
		for(int i =0; i < childList.size(); i++){
			System.out.print(childList.get(i).category+" ");
		}
		System.out.println(")");

	}
	/*
	 * try to expand structures
	 */
	public int expandStructure(int level, int maxPanelNumber, int currentPanelNumber, StructureMap map){
		//ignore all seen nodes
		if(isWentThrough != true){
			//System.out.println("#: "+level +", "+category);
		}
		
		isWentThrough = true;
		currentLevel = level;
		int count = 0;
		if(childList.size() == 0){
			//expandable
			boolean willExpand = shouldExpand(GlobalSettings.EXPAND_FRACTION);
			if(willExpand == true){
				//choose a structure, and compute panel numbers
				if(currentPanelNumber < maxPanelNumber){
					//assign a structure, and add current Panel number
					int random = (int )(Math.random() * map.phaseMap.size() + 0);
					getStructureByIndex(random, map);
					showAllChild();
					int expandRefer = (int )(Math.random() * 2 + 0);
					// add child nodes, minus parent node
					//recursively expand nodes
					currentPanelNumber = currentPanelNumber+map.phaseMap.get(random).size()-1;
					currentPanelNumber = expandStructure(level, maxPanelNumber, currentPanelNumber, map);
				}
			}
			else{
				// should return
			}
		}
		else{
			//check whether the child need to be expand
			//see whether the child node was seen
			while(count < childList.size()){
				if(childList.get(count).isWentThrough != true){
					//recursively expand nodes
					currentPanelNumber = childList.get(count).expandStructure(level+1, maxPanelNumber, currentPanelNumber, map);
				}
				count++;
			}
		}
		return currentPanelNumber;
	}	
	public boolean shouldExpand(int fraction){
		boolean should = false;
		int random = (int )(Math.random() * fraction + 0);
		if(random % fraction == 0){
			should = true;
		}
		else{
			should = false;
		}
		return should;
	}
	/*
	 * print whole structure
	 */
	public List<StructureNode> getLeafStructure(int currentChildCount, List<StructureNode> structureList){
		if(childList.size() == 0){
			//if no child -> leaf node
			System.out.println("$: "+currentLevel+", "+category);
			structureList.add(this);
		}
		else{
			//check count didn't exceed child index
			while(currentChildCount<childList.size()){
				childList.get(currentChildCount).getLeafStructure(0, structureList);
				currentChildCount = currentChildCount+1;
			}
		}
		return structureList;
	}
	public void initializePanel(){
		//assign characters
		int numberOfCharacter = (int )(Math.random() * GlobalSettings.MAX_CHARACTER + 1);
		for(int i =0; i <numberOfCharacter; i++){
			RGBA tempColor = getRandomColor();
			String action = ActionPool.choseRandomAction(category);
			CharaState initialState = new CharaState(action);
			PositionInPanel pos;
			if (action.equals("jumpUp")){
				pos = new PositionInPanel( i+1, GlobalSettings.HIGH, GlobalSettings.FACE_RIGHT);
			}else{
				pos = new PositionInPanel( i+1, GlobalSettings.LOW, GlobalSettings.FACE_RIGHT);
			}
			characters.add( new CharacterObject(p, GlobalSettings.AP, initialState, tempColor, pos));
		}
	}
	public void followUpdate(StructureNode previous){
		//copy previous characters
		characters = previous.characters;
		
		ArrayList<PositionInPanel> allPos = new ArrayList<PositionInPanel>();	
		int collisShift = 0;
		
		//update each character's new state
		for (int i = 0; i < characters.size(); i++){		
			 // reassign position after collision (even separate)
			if (previous.category.equals("P") && previous.characters.get(i).currentState.stateString.get(0).equals("collis") ){
				characters.get(i).pos.horizontal -= collisShift;
				collisShift++;
			}
			
			characters.get(i).updateState(category);		
			allPos.add(characters.get(i).pos);
		}
		
		//global check
		if (category.equals("P")){
			for (int i = 0; i < characters.size(); i++){
				characters.get(i).globalChecking(allPos, i);		
			}
		}
/*		
		else{
			for (int i = 0; i < characters.size(); i++){
				int exchangeChara = 0;
				exchangeChara = characters.get(i).positionExchange(allPos, i);
				if(exchangeChara != 0){
					characters.get(i).pos.horizontal = characters.get(i).pos.horizontal +1;
					characters.get(exchangeChara).pos.horizontal =  characters.get(exchangeChara).pos.horizontal -1;
				}
			}
			
			
		}
*/		
		/*
		//maintain, add, sub
		int n = (int)p.random(3);
		switch(n){
		case 0:
			break;
		case 1:
			if (characters.size()<GlobalSettings.MAX_CHARACTER){
				RGBA tempColor = getRandomColor();
				CharaState initialState = new CharaState(category, ActionPool.choseRandomAction(category));
				//PositionInPanel pos = new PositionInPanel(GlobalSettings.LEFT, GlobalSettings.LOW, GlobalSettings.FACE_RIGHT);
				PositionInPanel pos = new PositionInPanel(GlobalSettings.LEFT , GlobalSettings.HIGH, GlobalSettings.FACE_RIGHT);
				characters.add( new CharacterObject(p, GlobalSettings.AP, initialState, tempColor, pos));
			}
			break;
		case 2:
			if (characters.size() > 1){
				characters.remove((int)p.random(characters.size()));
			}
			break;
		default:
			System.out.println("out of bound:" + n);
		}
		*/
	}
	
	
	public void drawPanel(){
		//draw canvas
		p.pushMatrix();
		p.fill(255);
		p.rect(0,0,GlobalSettings.PANEL_WIDTH, GlobalSettings.PANEL_HEIGHT);
		//p.line(GlobalSettings.BLOCK_WIDTH, 0, GlobalSettings.BLOCK_WIDTH, GlobalSettings.PANEL_HEIGHT);
		//p.line(GlobalSettings.BLOCK_WIDTH*2, 0, GlobalSettings.BLOCK_WIDTH*2, GlobalSettings.PANEL_HEIGHT);
		//p.line(0, GlobalSettings.BLOCK_HEIGHT, GlobalSettings.PANEL_WIDTH, GlobalSettings.BLOCK_HEIGHT);
		p.textSize(14);
		p.text(category, 10, GlobalSettings.PANEL_HEIGHT+15);
		
		//draw characters
		for (int i = 0; i< characters.size(); i++){
			characters.get(i).display();
		}
		p.popMatrix();
	}//end of drawPanel
	
	public RGBA getRandomColor(){
		// generate a random color with random RGB
		RGBA newColor = new RGBA((int)p.random(256), (int)p.random(256), (int)p.random(256), 255);
		return newColor;
	}
	
	
}
