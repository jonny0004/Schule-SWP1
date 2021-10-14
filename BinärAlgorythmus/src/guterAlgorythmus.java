import java.util.Scanner;

public class guterAlgorythmus {
	  int[] feld;
	  static int counter = 0;
	static void binaerSuche(int[] feld, int links,int rechts, int kandidat) {
	        int mitte;
	        
	    do{
	    	counter++;
	        System.out.println("Intervall [" + links +
	                "," + rechts + "]");

	            mitte = (rechts + links) / 2;
	            if(feld[mitte] < kandidat){
	                links = mitte + 1;
	            } else {
	                rechts = mitte - 1;
	            }
	     } while(feld[mitte] != kandidat && links <= rechts);
	     if(feld[mitte]== kandidat){
	            System.out.println("Position: " + mitte);
	            System.out.println("Anzahl: "+ counter);
	        } else {
	            System.out.println("Wert nicht vorhanden!");
	        }
	    }


	    public static void main(String[] args) {
	        int groesse=200;
	        int[] feld = new int[groesse];
	        Scanner sc = new Scanner(System.in);
	        System.out.println("Welche zahl suchen sie:");
	        int zahl = sc.nextInt();
	        for (int i=0; i<feld.length;i++)
	            feld[i] = 2*i; 
	        System.out.println("Suche zahl=" + zahl);
	        binaerSuche(feld, 0,(feld.length-1), zahl);
	    }
	}
//http://www.scalingbits.com/java/javakurs2/suchalgorithmen/binaersuche

