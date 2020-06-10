program fibonacci;
main()
var int n, n1, n2, n3, it;
{
	print("Ingresa un valor para n");
	read(n);
	n1 = 1;
	n2 = 1;

	it = 0;
	print(n1);
	print(n2);
	while (n > it){
		n3 = n1 + n2;
		print(n3);
		n1 = n2;
		n2 = n3;
		it = it + 1;
	}

}
end