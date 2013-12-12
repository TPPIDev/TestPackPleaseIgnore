package mods;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class ListMaker
{
	public static void main (String[] args) throws FileNotFoundException
	{
		Scanner scan = new Scanner(System.in);
		
		String s = scan.nextLine().toLowerCase();
		
		String[] modNames = s.split(" ");
		
		Arrays.sort(modNames);
		
		for (String str : modNames)
		{
			System.out.println(str);
		}
		
	}
}