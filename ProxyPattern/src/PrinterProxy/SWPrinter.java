package PrinterProxy;

class SWPrinter implements Printer {
    public void print(String text) {
        System.out.println("SW-Drucker: " + text);
    }
}