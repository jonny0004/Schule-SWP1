
public class Rekursiv {
	static int wert = 0;
	public static void main(String[] args) {		
		System.out.println(Summieren(3));
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
