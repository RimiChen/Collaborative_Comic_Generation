package Data;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Random;
import java.util.Set;
import java.util.Vector;

import BasicElement.GlobalSettings;

public class ActionPool {
	Vector actionSet;
	
	static HashMap<String, String[]> actionNet = new HashMap<String, String[]>();
	{
		// put("name", new String[] 		  {"stand", "walk", "run",  "jumpUp", "fall", "trip", "dizzy"}
		// put("name", new String[] 		  {"stand", "walk", "run",  "jumpUp", "fall","roll", "dizzy"}
		actionNet.put("stand"	, new String[]{"stand", "walk", "run",	"jumpUp", "roll", "sit",	"think", "eat", "drink"	});
		actionNet.put("walk"	, new String[]{"stand", "walk", "run",	"jumpUp",  "roll", "think"});
		actionNet.put("run"		, new String[]{"stand", "walk", "run",	"jumpUp", "roll"});
		actionNet.put("jumpUp"	, new String[]{"fall"});
		actionNet.put("fall"	, new String[]{"stand",	"roll", "dizzy" });
		actionNet.put("roll"	, new String[]{"stand", "walk", "roll", "dizzy" });
		actionNet.put("collis"	, new String[]{"jumpUp", "fall","dizzy", "angry", "sad", "happy" });
		actionNet.put("dizzy"	, new String[]{"stand", "sit", "happy", "sad", "angry" });
		
		actionNet.put("sit"		, new String[]{"stand", "think", "eat", "drink"});
		
		actionNet.put("think"	, new String[]{"stand", "eat", "drink" });  // == wake
		actionNet.put("eat"		, new String[]{"drink", "shock", "spit","happy", "sad"	});
		actionNet.put("drink"	, new String[]{"eat"  , "shock", "spit","happy", "sad"	});
		actionNet.put("spit"	, new String[]{ "stand", "sit", "sad", "drink", "angry"});
		actionNet.put("happy"	, new String[]{"stand", "sit"});
		actionNet.put("sad"		, new String[]{"stand", "sit"});
		
		actionNet.put("fly"		, new String[]{"fly", "fall"});
		actionNet.put("sleep"	, new String[]{"think", "shock"});
		actionNet.put("shock"	, new String[]{"sad", "angry", "happy"});// == choke
		actionNet.put("angry"	, new String[]{"stand", "sit"});
	
	}
	
	static HashMap<String, String> actionCategory = new HashMap<String, String>();
	{
		actionCategory.put("stand"	, "EILR");
		actionCategory.put("walk"	, "IL");
		actionCategory.put("run"	, "IL");
		actionCategory.put("jumpUp"	, "IL");
		actionCategory.put("fall"	, "IPLR");
		actionCategory.put("roll"	, "PL");
		actionCategory.put("collis"	, "P");
		actionCategory.put("dizzy"	, "R");
		
		actionCategory.put("sit"	, "EILR");
		
		actionCategory.put("think"	, "IL");
		actionCategory.put("eat"	, "IP");
		actionCategory.put("drink"	, "IP");
		actionCategory.put("spit"	, "PR");
		actionCategory.put("happy"	, "R");
		actionCategory.put("sad"	, "R");
		
		actionCategory.put("fly"	, "LP");
		actionCategory.put("sleep"	, "ILR");
		actionCategory.put("shock"	, "P");
		actionCategory.put("angry"	, "PR");
	}
	
	static void ActionPool(){	
	}
	
	public void findMatchedAction(CharaState currentState){
		//by default if empty
		//String actionCategory = "";
		//for each( action in actionSet ){find matched state with currentState, actionCategory = matched}
		//return actionCategory;
		
	}
	
	public Set<String> getAllAction(){
		return actionCategory.keySet();
	}
	
	public String nextAction(String previousAction, String category){
		if (!GlobalSettings.RELATION_ALLOW ){
			Set<String> candidate = actionCategory.keySet();
			String randomPick = pickFromSet(candidate);
			return randomPick;
		}
		
	    //find candidate action
	    Set<String> candidate = getAvailableActions(previousAction);
	    //Picking a random element from a set
	    String randomPick = pickFromSet(candidate);
	    //check is picked fit it's category  
		if(GlobalSettings.STRUCTURE_ALLOW == true){
	    	while(actionCategory.get(randomPick).contains(category)==false && candidate.size()>=2){
		    	candidate.remove(randomPick);
		    	randomPick = pickFromSet(candidate);
		    }
		    //prevent actionNet error
		    if(candidate.size() == 1 && actionCategory.get(randomPick).contains(category)==false){
		    	System.out.println("net fail,  \"" + previousAction + "\" candidate can't find match category to " + category);
		    	randomPick = choseRandomAction(category);
		    }
	    }

	    return randomPick;      
	  }
	
	private Set<String> getAvailableActions(String action){
		Set<String> available = new HashSet<String>();
		String[] tmp = actionNet.get(action);
		for(int i = 0 ; i < tmp.length; i++){
			if (tmp[i] != "-"){
				available.add(tmp[i]);
			}
		}
		if(available.size()==0){
			System.out.println("getAvailableAction error");
		}
		return available;
	} 
	
	public static String pickFromSet(Set<String> myHashSet){
		int size = myHashSet.size();
		//System.out.println("size: " + size);
		int item = new Random().nextInt(size); // In real life, the Random object should be rather more shared than this
		int i = 0;
		for(String obj : myHashSet)
		{
		    if (i == item)
		        return obj;
		    i++;
		}
		System.out.println("pickFromSet error");
		return "";
	}
	
	public static String choseRandomAction(String category){
		String tmp = "";
		Set<String> contains = new HashSet<String>();
		for (String action: actionCategory.keySet()){
			  if(actionCategory.get(action).contains(category)){
				  contains.add(action);
			  }
		}
		tmp = pickFromSet(contains);
		if (tmp=="")
			System.out.println("choseRandomAction = null");
		return tmp;
	}
	
}
