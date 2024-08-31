package Structure;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.Vector;

/*
 * By analyzing panels, we store what we got (narrative structure for existing comic strips in here)
 */
public class StructureMap {
	
	//index, (length, structure string), EX: 0, (3, I|P|R)
	public Map<Integer, Vector> phaseMap;
	
	public StructureMap(){
		phaseMap = new TreeMap<Integer, Vector>();
	}
	/*
	 * store input structure string to list, and add to map
	 */
	public void addStructure(String inputStructure){
		//assume input structure are in this form: C|C|C|C|C, which are separated by |
		String [] categories = inputStructure.split("|");
		List<String> structureList = new ArrayList<String>(Arrays.asList(categories));
		
		Vector structures = new Vector();
		structures.addAll(structureList);
		structures.removeAll(Collections.singleton("|"));;
		
		
		// put this structure into map
		phaseMap.put(phaseMap.size(), structures);
	}
	/*
	 * show all stored structures
	 */
	public void showAllStructure(){
		for (Integer key : phaseMap.keySet()) {
			//get the length of list
			System.out.print("( "+key+" ,");
			
			for(int i = 0; i < phaseMap.get(key).size(); i++){
				System.out.print(phaseMap.get(key).get(i)+" ");
			}
			System.out.println(" )");

		}
	}
	
}
