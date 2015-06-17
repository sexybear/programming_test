package sampleexam;

public class Main {
	public static void main(String[] args) {
		MyCollection theStuff = new MyCollection();
		Collectable col1 = new MatchboxCar("Ford Capri", 1990, 1970, 250, true);
		Collectable col2 = new Figurine("China Cat", 2002, 2001, 120);
		((Figurine)col2).setNumCracks(5);
		Item col3 = new Model("Unknown Thing", 2005, 2004, 5);
		theStuff.add(col1);
		theStuff.add(col2);
		theStuff.add(col3);
		theStuff.printStatus(2007);
		theStuff.cleanOutRubbish(2007, 100);
		theStuff.printStatus(2007);
}
}
