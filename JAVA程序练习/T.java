
import java.util.Scanner;

public class T {
	public static void main(String[] args)
	{
		int ri,repeat,a,b,k,flag;
		long n;
		Scanner in  = new Scanner(System.in);
		repeat = in.nextInt();
		for(ri = 1;ri <= repeat;ri++)
		{
			a = in.nextInt();
			b = in.nextInt();
			int l = Integer.toString(b).length();
			if(a >= 0)
			{
				n =  (long) (a*Math.pow(10,l)+b);

			}
			else
			{
				n =  (long) ((-1)*a*Math.pow(10,l)+b);
				n =  (-1)*n;
			}
			System.out.println(n);
			
		}
	}

}
