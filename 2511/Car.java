public class Car {
    public String model;
    public int wheel;
    public Car(String m){
        this.model = m;
        this.wheel = 4;
    }
    
    public void drive()
    {
        if (this.wheel < 4) {System.out.println(this.model + "  no go vroom");}
        else System.out.println(this.model + "  go vroom");
    }

    public void driveinditch(int wheelslost){
        this.wheel -= wheelslost;
        return ;
    }

    public int getwheels()
    {    return this.wheel;
    }
    public static void main(String[] args)
    {    Car c1,c2;
        c1 = new Car("Civic Type R");
        c2 = new Car("Typstp crame");
        c1.drive();
        c1.driveinditch(2);
        c1.drive();
        System.out.println(c2.getwheels());

    }

}
