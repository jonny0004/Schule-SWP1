
public class endRekursiv {

	public static void main(String[] args) {
		final long timeStart = System.nanoTime();
		
		System.out.println(sum(1000));
		 	  
	    final long timeEnd = System.nanoTime();
	    System.out.println("Verlaufszeit der Schleife: " + (timeEnd - timeStart)/1000 + " Mikrosek.");
		 
	}

	public static long add_sum(long m, long n) {
		   if (n == 0) {
		     return m;
		   }
		   else {
		     return add_sum (m+n, n-1);
		   }
		 }
	public static long sum(long n) {
		return add_sum(0, n);
	}
}
