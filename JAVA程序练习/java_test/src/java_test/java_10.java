package java_test;

import java.util.*;
public class java_10 {
	public static void main(String args[])
	{
		Scanner in = new Scanner(System.in);
		
		System.out.println("how much money will you contributes every year");
		double payment = in.nextDouble();
		
		System.out.print("interest rate in %");
		double interestRate = in.nextDouble();
		
		double balance  = 0;
		int year = 0;
		
		String input;
		
		do
		{
			balance += payment;
			double interest = balance * interestRate /100;
			
			balance += interest;
			
			year++;
			
			System.out.printf("after year %d,your balance is %.2f%n",year,balance);
			
			System.out.print("Ready tp retire(Y/N)");
			input= in.next();
			
		}
		while(input.equals("N"));
	}

}
