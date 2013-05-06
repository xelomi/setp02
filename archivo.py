def palindromo(palabra,i,j):
	if palabra[j]!=palabra[i] :
		return 0
	if palabra[j]==palabra[i] and j:
		resp=palindromo(palabra,i+1,j-1)
	return 1



palabra=input("ingrese palabra ")
print(len(palabra))
resp=palindromo(palabra,0,len(palabra)-1)
if resp:
	print("si es palindromo")
else:
	print("es terrible shora")

