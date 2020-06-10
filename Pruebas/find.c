program find;

main()
var int lugar, arr[5], it, valor;
{	
	arr[0] = 10;
	arr[1] = 20;
	arr[2] = 30;
	arr[3] = 40;
	arr[4] = 50;

	it = 0;
	while (it < 5) {
		print(arr[it]);
		it = it + 1;
	}

	valor = arr[1 + 1] + 32 * 2; 
	print(valor);
	
}
end