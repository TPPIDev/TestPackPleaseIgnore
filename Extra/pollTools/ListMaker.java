package pollTools;

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
			if (str.length() > 4 && str.charAt(0) != '(')
				System.out.println(str);
		}
		
		scan.close();
	}
}