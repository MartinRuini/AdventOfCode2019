package day_4;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;

public class day_4 {

	private static final String path = "2022/day_4/input";
	
	public static void main(String[] args) {
		
		
		try {
			BufferedReader r = new BufferedReader (new FileReader (path));
			
			//PART 1
			String s = "";
			int result1 = 0;
			int result2 = 0;
			while ((s=r.readLine()) != null) {
				if(parsePairs1(s)) {
					result1++;
				}
				if(parsePairs2(s)) {
					result2++;
				}
			}
			System.out.println("Part 1 (completely overlapping pairs): " + result1);
			System.out.println("Part 2 (partially overlapping pairs): " + result2);
						
			r.close();
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}		
	}

	private static Boolean parsePairs1(String line) {
		
		String[] pair = line.split(",");
		int a1 = Integer.parseInt(pair[0].split("-")[0]);
		int a2 = Integer.parseInt(pair[0].split("-")[1]);
		int b1 = Integer.parseInt(pair[1].split("-")[0]);
		int b2 = Integer.parseInt(pair[1].split("-")[1]);
		
		//System.out.println(a1 + " " +  a2 + " " + b1 + " " + b2);
		if( ((a1 <= b1) && (a2 >= b2)) || ((a1 >= b1) && (a2 <= b2))) {
			System.out.println(pair[0] + "," + pair[1]);
			return true;
		} else {
			return false;
		}
	}
		
		private static Boolean parsePairs2(String line) {
			
			String[] pair = line.split(",");			
			int a1 = Integer.parseInt(pair[0].split("-")[0]);
			int a2 = Integer.parseInt(pair[0].split("-")[1]);
			int b1 = Integer.parseInt(pair[1].split("-")[0]);
			int b2 = Integer.parseInt(pair[1].split("-")[1]);
			//System.out.println(a1 + " " +  a2 + " " + b1 + " " + b2);
			if( ( ((a1 >= b1) && (a1 <= b2)) || ((a2 >= b1) && (a2 <= b2)) ) ||
					(((b1 >= a1) && (b1 <= a2)) || ((b2 >= a1) && (b2 <= a2)))) {
				System.out.println(pair[0] + "," + pair[1]);
				return true;
			} else {
				return false;
			}
		
		
	}
	
}


