package sampleexam;

public class Item implements Collectable {
	protected int yearBought;
	protected int yearMade;
	protected int pricePaid;
	protected String label;
	public Item(String l, int yb, int ym, int pp) {
		label = l;
		setYearBought(yb);
		setYearMade(ym);
		setPricePaid(pp);
	}
	public String getLabel() { return label; }
	public int getYearBought() { return yearBought; }
	public int getPrice() { return pricePaid; }
	public int getYearMade() { return yearMade; }
	public int insurableValue(int thisYear) {
		return pricePaid;
	}
	public int currentWorth(int thisYear) {
		return pricePaid;
}
// what it¡¯s worth on the open market.
public void setYearBought(int yb) {
	assert yearBought > 0;
	yearBought = yb;
}
public void setPricePaid(int pp) {
	assert pp > 0;
	pricePaid = pp;
}
public void setYearMade(int ym) {
	assert ym > 0;
	yearMade = ym;
}
}