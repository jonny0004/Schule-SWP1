
public class BinärSuche {

	private static int counter;
	
	public static void main(String[] args) {
		int[] zahlen = {3,6,13,17,18};
		
		System.out.println(counter);
		if(suche(3, zahlen) == true) {
			System.out.println("Ihre zahl ist enthalten");
		}
		else {
			System.out.println("Ihre zahl ist nicht enthalten");
		}
	}
	public static boolean suche(int zahl, int[] mListe) {
		for(int i = 0; i < mListe.length; i++) {
			counter = i;
			if(mListe[i] == zahl) {
				return true;
			}
		}
		return false;
		
		
	}
}
