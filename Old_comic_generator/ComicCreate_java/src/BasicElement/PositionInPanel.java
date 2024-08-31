package BasicElement;

public class PositionInPanel {
	public int horizontal;
	public int vertical;
	public int direction;
	
	public static GlobalSettings G;
	
	public PositionInPanel(int horizontal, int vertical, int direction){
		this.horizontal = horizontal;
		this.vertical = vertical;
		this.direction = direction;
	}
	public Vector2D transform2Real(){
		Vector2D realPos = new Vector2D(horizontal*GlobalSettings.BLOCK_WIDTH - GlobalSettings.BLOCK_WIDTH/2, 
				vertical*GlobalSettings.BLOCK_HEIGHT - GlobalSettings.BLOCK_HEIGHT/2);
		//Vector2D realPos = new Vector2D(horizontal*GlobalSettings.BLOCK_WIDTH, vertical*GlobalSettings.BLOCK_HEIGHT);
		//transform position in panel to real position on the screen
		
		return realPos;
	}
	public boolean isOverlapping(PositionInPanel pos){
		if( (pos.horizontal == horizontal) && (pos.vertical == vertical)){
			System.out.println("overlap in " + horizontal + ", " +vertical );
			return true;
		}
		return false;
	}
}
