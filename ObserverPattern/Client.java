

public class Client {
    public static void main(String[]args){
        Zentrale messzentrale = new Zentrale(); 
        messzentrale.aboHinzuf�gen(new A1()); 
        messzentrale.setAktuellesWetter(new Wetter("Sch�n",25,30)); 

        ZentralePull messzentralePull = new ZentralePull(); 
        messzentralePull.aboHinzuf�gen(new A2(messzentralePull)); 
        messzentralePull.setAktuellesWetter(new Wetter("Regnerisch",10,80)); 

    }
}
