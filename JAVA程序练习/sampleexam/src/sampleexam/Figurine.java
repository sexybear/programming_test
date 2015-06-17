package sampleexam;

public class Figurine extends Item {
	protected int numCracks;
	public Figurine(String s, int yb, int ym, int pp) {
		super(s, yb, ym, pp);
		numCracks = 0;
	}
	public void setNumCracks(int n) { numCracks = n; }
	public int currentWorth(int thisYear) {
		// Figurines gradually increase their value
		// at 5% of the original cost per year.
		double value = (thisYear - getYearBought()) / 10;
		return (int) ((double) getPrice() * value) - 10*numCracks;
	}
	public int insurableValue(int thisYear) {
		// Enough cracks will make this worthless.
		return Math.max(pricePaid - 10*numCracks, 0);
	}
}