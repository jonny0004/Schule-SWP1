
public class Iterativ {

	public static void main(String[] args) {
		System.out.println(Summieren(3));

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
