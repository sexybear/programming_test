package sampleexam;

public class FineWine extends Item
{
  protected String type;
  protected String vineyard;
  public FineWine(String l,int yb,int ym,int pp)
  {
    super(l,yb,ym,pp);
    type = new String();
    vineyard = new String();
  }
  
  

  public int currentWorth(int thisyear)
  {
    return (getPrice()+(thisyear-getYearBought())*5);
  }
  
  public int insurableValue(int thisYear)
  {
		return (getPrice()+5);
  }
  
  public void setType(String name){type = name;}
  
  public void setVineyard(String name){vineyard = name;}
}