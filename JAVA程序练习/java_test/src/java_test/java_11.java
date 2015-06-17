package java_test;

import java.util.*;
public class java_11 {
	public static void main(String args[])
	{
		Scanner in  = new Scanner(System.in);
		
		System.out.println("how much numbers do you need to draw");
		int k = in.nextInt();
		
		System.out.println("what is highest number you can draw");
		int n = in.nextInt();
		
		int lotteryOdds = 1;
		for(int i = 1;i <= k;i++)
		{
			lotteryOdds = lotteryOdds + (n-i +1)/i;
		}
		System.out.println("your odds are 1 in"+ lotteryOdds + "Good luck");
	}
}
