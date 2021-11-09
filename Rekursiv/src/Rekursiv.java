
public class Rekursiv {
	static int wert = 0;
	public static void main(String[] args) {
		final long timeStart = System.nanoTime();
		
		System.out.println(Summieren(10000));
		 	  
	    final long timeEnd = System.nanoTime();
	    System.out.println("Verlaufszeit der Schleife: " + (timeEnd - timeStart)/1000 + " Mikrosek.");
		
	}

	public static int Summieren(int number) {				
		
		if( number > 0) {
			wert = wert + number;
			return Summieren(number - 1);
		}
		else {
		return wert;
		}
	}
}
