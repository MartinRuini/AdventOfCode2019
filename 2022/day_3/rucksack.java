package day_3;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;

public class rucksack {

	private static final String path = "src/day_3/items";
	
	public static void main(String[] args) {
		
		Map<String,Integer> mapping = new Prioritizer().getMap();
		
		try {
			BufferedReader r = new BufferedReader (new FileReader (path));
			
			//PART 1
			String s = "";
			int sum = 0;
			while ((s=r.readLine()) != null) {
				sum += mapping.get(check_duplicates(half(s)));
			}
			System.out.println("Part 1: " + sum);
						
			r.close();
			r = new BufferedReader (new FileReader (path));
			
			//PART 2
			sum = 0;
			int counter = 0;
			String[] group = new String[3];
			while ((s=r.readLine()) != null) {
				if(counter>2) {
					counter = 0;
					//System.out.println("Reset counter");
					String res =find_badge(group);
					if(res.length()==1) {
						sum += mapping.get(res);
					}
				}
				group[counter] = s;
				//System.out.println("Added elf " + (counter+1) + ": " + s);
				counter++;				
			}
			String res =find_badge(group);
			if(res.length()==1) {
				sum += mapping.get(res);
			}
			
			r.close();
			System.out.println("Part 2: " + sum);
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}		
	}

	private static String[] half (String line) {
		
		String first = line.substring(0, (line.length()+1)/2);
		String second = line.substring((line.length()+1)/2, line.length());
		return new String[] {first, second};
		
	}
	
	private static String check_duplicates (String[] halves) {
		
		String result = "";
		
		for(String c : halves[0].split("")) {
			if(halves[1].contains(c) && !result.contains(c)) {
				result += c;
			}
		}
		
		return result;
		
	}
	
	private static String find_badge(String[] group) {
		
		for(String c : group[0].split("")) {
			if (group[1].contains(c) && group[2].contains(c)) {
				//System.out.println("Found badge: " + c);
				return c; 
			}
		}
		//System.out.println("Error: badge not found");
		return "Error: badge not found";
	}
	
}


