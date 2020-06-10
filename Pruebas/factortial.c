program factorial;

main()
var int n, i, x, fact;
{
    print("Ingrese un numero");
    read (n);
    fact = 1;
    if(n < 0) then { 
        print("No valido");
     }
    else {
        x = 1;
        while(x <= n){
            fact = fact * x;
            x = x + 1;
        }
        print(fact);
     }
           
}
end 