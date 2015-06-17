package sampleexam;
import java.util.*;
public final class MyCollection {
private List<Collectable> myStuff;
public MyCollection() {
	myStuff = new ArrayList<Collectable>();
}
public void add(String s, int yb, int ym, int pp) {
	Item myItem = new Model(s, yb, ym, pp);
myStuff.add(myItem);
}
public void add(Collectable col) {
myStuff.add(col);
}
public void printStatus(int thisYear) {
/**
* Write to a string a description of the collection.
* Print whether each item is worth more or less
* and highlight the items that should be cleaned out.
*/
	String str = new String();
	for (Collectable col : myStuff) {
			Item it = (Item) col;
			str = it.getLabel() + ": cost me $" + it.getPrice();
			int worth = it.currentWorth(thisYear);
			str += ", now worth $" + worth + ".";
			if (worth <= 0) {
				str += "\n * Lost all its value: get rid of it! *";
			} else if (worth < it.getPrice()) {
				str += "\n - Lost some value -";
			}
			System.out.println(str);
	}
}
public void cleanOutRubbish(int thisYear, int minWorth) {
/**
* Remove all the items that have less than minWorth
* value this year.
*/
// You will write this method
	String str = new String();
	for(Collectable col : myStuff)
	{
		Item it = (Item) col;
		if(it.currentWorth(thisYear) <= minWorth)
		{
			myStuff.remove(col);
		}
	}
}
public Collectable findBiggestGain(int thisYear) {
/**
* Find the Item in the collection that has gained
* the most in value from when it was bought.
*/
	Collectable item = null;
	// You will write this method
	return item;
}
}