package test_oop;

public class teacher {
	String name;
	int id;
	
	public teacher(String name,int id)
	{
		this();
		this.name = name;
		this.id = id;
	}
	public teacher()
	{
		System.out.println("����һ������");
	}
	public void setName(String name)
	{
		this.name = name;
	}
}
