
public class Iterativ {

	public static void main(String[] args) {
		final long timeStart = System.nanoTime();
		
		System.out.println(Summieren(10000));
		 	  
	    final long timeEnd = System.nanoTime();
	    System.out.println("Verlaufszeit der Schleife: " + (timeEnd - timeStart)/1000 + " Mikrosek.");
		
	}
	
	public static int Summieren(int number) {
		int i = 0;
		int wert = 0;
		while(i < number ) {
			i++;
			wert = wert +i;
		}
		return wert;
	}
}
