package sampleexam;

public class Model extends Item {
	public Model(String l, int yb, int ym, int pp) {
		super(l, yb, ym, pp);
	}
	public int currentWorth(int thisYear) {
		return pricePaid + (yearBought - thisYear);
	}
	public int insurableValue(int thisYear) {
		return pricePaid;
}
}
