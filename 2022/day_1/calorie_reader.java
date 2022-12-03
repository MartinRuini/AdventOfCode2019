package day_1;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import javax.swing.text.AbstractDocument.Content;

public class calorie_reader {

	private static final String path = "src/day_1/input_1";
	
	public static void main(String[] args) {
		
		List<Integer> calories = new ArrayList<>();
		Integer max_amount = 0;
		
		FileReader myReader;
		try {
			myReader = new FileReader (path);
			BufferedReader r = new BufferedReader ( myReader );
			String s = "a";
			Integer sum = 0;
			while ((s=r.readLine()) != null) {
				
				if (!s.isEmpty()) {
					sum = sum + Integer.parseInt(s);
				}else {
					calories.add(sum);
					if (sum > max_amount) {
						max_amount=sum;
					}
					sum = 0;
				}		
				
			}
			System.out.println("First: " + max_amount);
			System.out.println("Top three: " + top_three(calories));
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}		
	}
	
	private static Integer top_three(List<Integer> list) {
		
		Integer first = 0;
		Integer second = 0;
		Integer third = 0;
		
		for (Integer c:list) {
			if(c>first) {
				third=second;
				second=first;
				first=c;
			}else if(c>second) {
				third=second;
				second=c;
			}else if(c>third) {
				third=c;
			}
		}
		return first+second+third;
	}
}

