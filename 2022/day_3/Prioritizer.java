package day_3;

import java.util.HashMap;
import java.util.Map;

public class Prioritizer {

	Map<String,Integer> mapping;
	
	Prioritizer(){
		this.mapping = new HashMap<>();
		
		for(int i=97; i<=122; i++) {
			this.mapping.put(String.valueOf(((char)i)), i-96);
		}
		for(int i=65; i<=90; i++) {
			this.mapping.put(String.valueOf(((char)i)), i-38);
		}
	}
	
	
	public Map<String,Integer> getMap(){
		return this.mapping;
	}
}
