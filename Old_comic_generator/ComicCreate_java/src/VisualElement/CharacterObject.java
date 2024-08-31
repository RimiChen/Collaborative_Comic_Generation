package VisualElement;


import java.util.ArrayList;
import java.util.Set;

import BasicElement.GlobalSettings;
import BasicElement.PositionInPanel;
import BasicElement.RGBA;
import BasicElement.Vector2D;
import Data.ActionPool;
import Data.CharaState;
import Data.State;
import processing.core.PApplet;

public class CharacterObject implements VisualElement{
	//display
	PApplet p;
	ActionPool pool;
	RGBA color;
	public PositionInPanel pos;
	public CharaState currentState;
	/*
	 * data structure
	 */
	// the current state of this character, with position direction
	
	
	public CharacterObject(PApplet p, ActionPool pool, CharaState currentState, RGBA color, PositionInPanel pos){
		this.p = p;
		this.pool = pool;
		//need initialize, but now empty
		this.currentState = currentState;
		this.color = color;
		this.pos = pos;
	}
	/*
	 * match currentState with Action's state, where the Actions are in the ActionPool
	 * return: action category, which action was matched. 
	 */
	public String matchActionState(CharaState currentState, ActionPool pool){
		String actionCategory = "";
		
		//match action state with current state
		//actionCategory = pool.findMatchedAction(currentState);
		return actionCategory;
	}
	public void updateState(String category){
		String newAction = pool.nextAction(currentState.stateString.get(0), category);		
		currentState.stateString.clear();
		currentState.stateString.add(newAction);
		System.out.println(category + ": " + newAction);
		
		//change position
		if (newAction.equals("jumpUp") || newAction.equals("fly") ){
			pos.vertical = GlobalSettings.HIGH;
		}
		else if (newAction.equals("fall")){
			pos.vertical = GlobalSettings.LOW;
		}
		else if (newAction.equals("walk") || newAction.equals("run") || newAction.equals("roll")){
			if (pos.horizontal != GlobalSettings.RIGHT){
				pos.horizontal ++;
			}
		}
	}
	
	public void globalChecking(ArrayList<PositionInPanel> allPos, int selfNumber){
		for (int i = 0; i < allPos.size(); i++){
			if ( (i != selfNumber) && pos.isOverlapping(allPos.get(i)) ){
				currentState.stateString.clear();
				currentState.stateString.add("collis");
				break;
			}
		}
	}
	public int positionExchange(ArrayList<PositionInPanel> allPos, int selfNumber){
		for (int i = 0; i < allPos.size(); i++){
			if ( (i != selfNumber) && pos.isOverlapping(allPos.get(i)) ){
				//currentState.stateString.clear();
				//currentState.stateString.add("collis");
				//PositionInPanel tempPos = pos;
				//pos = allPos.get(i);
				
				return i;
				//break;
			}
		}
		return 0;
	}	
	@Override
	public void display() {
		
		p.fill(color.r, color.g, color.b, color.a);
		Vector2D realpos = pos.transform2Real();
		p.pushMatrix();
		p.translate(realpos.x, realpos.y);
		p.ellipse(0, 0, GlobalSettings.CHARA_SIZE/2, GlobalSettings.CHARA_SIZE/2);
		// load symbol if symbol allowed
		if(GlobalSettings.SYMBOL_ALLOW == true){
			//System.out.println(GlobalSettings.SP.getImage(currentState.stateString.get(0)));
			if(GlobalSettings.SP.getImage(currentState.stateString.get(0)) != null){
				//p.text("Show Symbol", 0, 0);
				Vector2D symbolShift = GlobalSettings.SP.getShift(currentState.stateString.get(0));
				float symbolSize = GlobalSettings.SP.getSize(currentState.stateString.get(0));
				p.image(GlobalSettings.SP.getImage(currentState.stateString.get(0)), symbolShift.x, symbolShift.y, GlobalSettings.BLOCK_WIDTH*symbolSize, GlobalSettings.BLOCK_HEIGHT*symbolSize);
			}
		}
		p.text(currentState.stateString.get(0), -GlobalSettings.CHARA_SIZE/2, GlobalSettings.CHARA_SIZE/2);
		p.popMatrix();
		
		
		/*
		// TODO Auto-generated method stub
		//transform position in panel to real position, suppose it is center point
		Vector2D currenPos = pos.transform2Real();
		Vector2D origin = new Vector2D(0, 0);
		int halfPanelWidth = GlobalSettings.PANEL_WIDTH / 2;
		int halfPanelHeight = GlobalSettings.PANEL_HEIGHT / 2;
		
		//triangle
		p.pushMatrix();
		p.translate(currenPos.x, currenPos.y);
		//p.rotate(currentOrientation);
		//by default set stroke black
		p.stroke(0);
		p.fill(color.r, color.g, color.b, color.a);
			p.pushMatrix();		
			p.triangle(
					origin.x-halfPanelWidth, origin.y-halfPanelHeight,
					origin.x+halfPanelWidth, origin.y,
					origin.x-halfPanelWidth, origin.y+halfPanelHeight
			);
			p.popMatrix();
		p.popMatrix();				
		*/
		
	}//end of display

	
}
