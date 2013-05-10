def es_palindromo(palabra,i,j):
	if palabra[j]!=palabra[i] :
		return False
	if palabra[j]==palabra[i] and j:
		resp=palindromo(palabra,i+1,j-1)
	return True



palabra=input("ingrese palabra ")
print(len(palabra))
resp=palindromo(palabra,0,len(palabra)-1)
if resp:
	print("si es palindromo")
else:
	print("no es palindroma")

