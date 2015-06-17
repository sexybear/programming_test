package sampleexam;

public class MatchboxCar extends Model {
	private boolean stillInBox; // true if the item is still wrapped
	public MatchboxCar(String l, int yb, int ym, int pp, boolean inBox) {
		super(l, yb, ym, pp);
		stillInBox = inBox;
	}
	public int currentWorth(int thisYear) {
		double increase = 0.0;
		if (stillInBox) {
			increase = getPrice() / 10;
		} else {
			increase = -getPrice() / 100;
		}
		return (int) increase * (thisYear - yearBought);
	}
	public int insurableValue(int thisYear) {
		if (stillInBox)
			return pricePaid*(thisYear - yearMade);
		return pricePaid;
	}
}
