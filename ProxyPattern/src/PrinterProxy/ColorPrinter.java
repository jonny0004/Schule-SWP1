package PrinterProxy;

class ColorPrinter implements Printer {
    public void print(String text) {
        System.out.println("Farbdrucker: " + text);
    }
}

