package day_2;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class point_counter {

	private static final String path = "src/day_2/encrypted_strategy_guide";
	
	public static void main(String[] args) {
		
		FileReader myReader;
		try {
			myReader = new FileReader (path);
			BufferedReader r = new BufferedReader (myReader);
			String s = "";
			Integer sum1 = 0;
			Integer sum2 = 0;
			while ((s=r.readLine()) != null) {
				sum1 += count_points_1(s);
				sum2 += count_points_2(s);
			}
			System.out.println(sum1);
			System.out.println(sum2);
			r.close();
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}		
	}

	private static Integer count_points_1(String line) {
		
		switch(line) {
		case "A X":
			return 1+3;
		case "A Y":
			return 2+6;
		case "A Z":
			return 3+0;
		case "B X":
			return 1+0;
		case "B Y":
			return 2+3;
		case "B Z":
			return 3+6;
		case "C X":
			return 1+6;
		case "C Y":
			return 2+0;
		case "C Z":
			return 3+3;
		}
		
		return 0;
	}
	
private static Integer count_points_2(String line) {
		
		switch(line) {
		case "A X":
			return 3+0;
		case "A Y":
			return 1+3;
		case "A Z":
			return 2+6;
		case "B X":
			return 1+0;
		case "B Y":
			return 2+3;
		case "B Z":
			return 3+6;
		case "C X":
			return 2+0;
		case "C Y":
			return 3+3;
		case "C Z":
			return 1+6;
		}
		
		return 0;
	}
	
	}


