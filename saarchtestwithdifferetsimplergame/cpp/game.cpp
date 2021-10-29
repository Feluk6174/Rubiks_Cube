#include <iostream>
using namespace std;

class game{
	public:
		int pos[3];
		void set(int x[3]){
			pos[0] = x[0];
			pos[1] = x[1];
			pos[2] = x[2];
		}
		
		int * get(){
			return pos;
		}
		
		void mov1(){
			if(pos[0] != 9){
				pos[0]++;
			}
			else{
				pos[0] = 0;
			}
		}
		
		void mov2(){
			if(pos[0] != 0){
				pos[0]--;
			}
			else{
				pos[0] = 9;
			}
			if(pos[1] != 9){
				pos[1]++;
			}
			else{
				pos[1] = 0;
			}
			if(pos[2] != 0){
				pos[2]--;
			}
			else{
				pos[2] = 9;
			}
		}
		
			
		void mov3(){
			if(pos[2] != 9){
				pos[2]++;
			}
			else{
				pos[2] = 0;
			}
		}
		
		void move(int m){
			if(m == 0){mov1();}
			if(m == 1){mov2();}
			if(m == 2){mov3();}
		}
		
		bool solved(){
			return (pos[0] == pos[1] && pos[0] == pos[2]);
			
		}
					
};

void print(int p[3]){
	cout << p[0] << " " << p[1] << " " << p[2] << endl;
}

int main(){
	game g;
	bool game_over = true;
	int i[3] = {4, 2, 1};
	int p[3], m;
	g.set(i);
	print(p);
	
	while (!g.solved()){
		cout << "move: ";
		cin >> m;
		
		g.move(m);
		
		p[0] = g.get()[0];
		p[1] = g.get()[1];
		p[2] = g.get()[2];
	
		print(p);
	}
}