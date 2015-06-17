package test_oop;

public class Student {
	private String name;
	private int id;
	private int age;
	private String gender;
	private int weight;
	
	public void study()
	{
		System.out.println(name+"ÔÚÑ§Ï°");
	}
	public void sayhello(String sname)
	{
		System.out.println("name"+sname+"ÄãºÃ");
	}
	
	public static void main(String args[])
	{
		Student s1 = new Student();
		s1.name = "sss";
		s1.study();
	}

}
