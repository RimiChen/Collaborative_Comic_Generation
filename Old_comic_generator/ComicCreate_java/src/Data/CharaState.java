package Data;

import java.util.*;

public class CharaState implements State{
	//Set<String> aset = new HashSet<String>();
	//ActionPool action = new ActionPool();
	
	public ArrayList<String> stateString = new ArrayList<String>();
	
	public CharaState(String choseRandomAction) {
		// TODO Auto-generated constructor stub
		stateString.add(choseRandomAction);
	}

}

