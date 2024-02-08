from utilityModule import File, creerArbre, prefixPath, infixPath, subfixPath


tree = creerArbre()
print(tree)

prefixPath(tree)
print("\n")
infixPath(tree)
print("\n") 
subfixPath(tree)
