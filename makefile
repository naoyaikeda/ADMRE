ADMRE:	main.o individual.o deme.o world.o
		g++ -o ADMRE main.o individual.o deme.o world.o
main.o:	main.cpp
		g++ -c main.cpp
deme.o: deme.cpp
		g++ -c deme.cpp
individual.o: individual.cpp
		g++ -c individual.cpp
world.o: world.cpp
		g++ -c world.cpp
