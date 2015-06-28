import java.util.*;

public class T1 {
	public static void main(String[] args)
	{
		int ri,repeat,m,n,i;
		double s;
		Scanner in = new Scanner(System.in);
		repeat = in.nextInt();
		double[] finalnumbers;
		for(ri = 1;ri<repeat;ri++)
		{
			m = in.nextInt();
			String op = in.next();
			n = in.nextInt();		
			
			
			if(op.equals("+"))
			{
				s = m+n;
				System.out.printf("result = %f",(int)(s));
			}
			else if(op.equals("-"))
			{
				s = m-n;
				System.out.printf("result = %f",(int)(s));
			}
			else if(op.equals("*"))
			{
				s = m*n;
				System.out.printf("result = %f",(int)(s));
			}
			else if(op.equals("/"))
			{
				s = (double)(m/n);
				System.out.printf("result = %f",s);
			}
			else
			{
				
				System.out.println("ERROR");
			}
		}
		
	}

}
