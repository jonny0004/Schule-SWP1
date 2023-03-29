package PrinterProxy;

public class Client {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 PrinterProxy printer = new PrinterProxy();

	     printer.print("Hallo in SW");
	  
	     printer.switchTo(new ColorPrinter());
        
	     printer.print("Hallo in Farbe");
	}

}
