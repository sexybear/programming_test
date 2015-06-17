package java_test;
/**
 * 
 * @author Admin
 *
 */
public class java_13 {
	
	static int a = 0;
	public static void test01()
	{
		a++;
		System.out.println("test01"+a);
		if(a<10)
		{
			test01();
		}
	}
	public static void test02()
	{
		System.out.println("test02");
	}
	
	public static long factorial(int n)
	{
		if(n == 1)
		{
			return 1;
		}
		else
		{
			return n*factorial(n-1);
		}
	}
	public static void main(String args[])
	{
		test01();
		System.out.println(factorial(10));
	}
}
