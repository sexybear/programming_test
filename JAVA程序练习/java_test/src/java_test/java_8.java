package java_test;

import java.util.*;
import java.io.Console;

public class java_8 {
	public static void main(String args[]){
		String s = "wuwenxiao";
		String w = s.substring(0,3);
		
		String ss = "wuwen";
		
		String sww = "sjkjdla";
		
		String fin = ss+sww;
		
		
		System.out.println(w);
		
		System.out.println(fin);
		
		int age = 13;
		
		String wu = w+age;
		
		System.out.println(wu);
		
		String d = "WUWEn";
		String f = "wuWen";
		
		if(d.equalsIgnoreCase(f))
		{
			System.out.println("yes");
			
		}
		
		StringBuilder builder = new StringBuilder();
		
		builder.append(w);
		
		builder.append(ss);
		
		System.out.println(builder);
		
		
		String fin_builder = builder.toString();
		
		System.out.println(fin_builder);
		
		Scanner in = new Scanner(System.in);
		
		System.out.println("please enter:");
		
		String name = in.nextLine();
		
		System.out.println(name);
		
		System.out.println("please enter int:");
		
		int ageas = in.nextInt();
		
		System.out.println(ageas);
		
		/*Console cons = System.console();
		
		String username = cons.readLine("user name:");
		
		char[] passwd = cons.readPassword("password:");
		*/
		
		
		
		
		
		
		
		
	}
	
	
	

}
