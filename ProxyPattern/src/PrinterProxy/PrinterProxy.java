package PrinterProxy;

class PrinterProxy implements Printer {
    private Printer currentPrinter;

    public PrinterProxy() {
        currentPrinter = new SWPrinter();
    }

    public void switchTo(Printer newPrinter) {
    	this.currentPrinter = newPrinter;
    }

    public void print(String text) {
        currentPrinter.print(text);
    }
}







