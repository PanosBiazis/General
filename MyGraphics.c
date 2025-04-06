#include <stdio.h>
#include <stdlib.h>

	void face1(){
	printf("\t\t\t\t*\n");
	printf("\t\t\t*\t\t*\n");
	printf("\t\t*\t  [*]   \t[*]\t*\n");
	printf("\t*\t\t\t\t\t\t*\n");
	printf("\t\b*\t\t\t\t\t\t\t\b\b\b\b\b\b\b*\n");
	printf("\t\b\b|\t\t\t\t\t\t\t\t\b\b\b\b\b\b|\n");
	printf("\t\b*\t\t\t\t\t\t\t\b\b\b\b\b\b\b*\n");
	printf("\t*\t\t\t\t\t\t*\n");
	printf("\t\t*\t\t\t\t*\n");
	printf("\t\t\t*\t(----)\t*\n");
	printf("\t\t\t\t*\n");	
	}
	
	void tringle(){
	printf("............/\\\n");
	printf("...........*..*\n");
	printf("..........*....*\n");	
	printf(".........*......*\n");
	printf("........*........*\n");
	printf(".......*..........*\n");
	printf("......*............*\n");
	printf(".....*..............*\n");
	printf("....*................*\n");
	printf("...*..................*\n");
	printf("..*....................*\n");
	printf(".*......................*\n");
	printf("*........................*\n");
	printf("--------------------------\n");
	}
	
	void circle(){
	printf("..................**********\n");
	printf(".............*...................*\n");
	printf("..........*........................*\n");
	printf(".......*.............................*\n");	
	printf("......*................................*\n");
	printf("....*....................................*\n");
	printf("...*......................................*\n");
	printf("..*........................................*\n");
	printf(".*..........................................*\n");
	printf(".*..........................................*\n");
	printf(".*..........................................*\n");
	printf(".*..........................................*\n");
	printf(".*..........................................*\n");
	printf("..*.........................................*\n");
	printf("...*.......................................*\n");
	printf("....*.....................................*\n");
	printf(".....*..................................*\n");
	printf(".......*..............................*\n");
	printf(".........*..........................*\n");
	printf("...........*......................*\n");
	printf(".............*..................*\n");
	printf("..................**********\n");
	}
	
	int Main_Menu(int selection){
Begin:;
	printf("1.General Graphics\n2.Specific Graphics\n3.Exit\n");
	printf("Selection >>");
	scanf("%d",&selection);
	printf("Selected:%d\n",selection);
	switch(selection){
		case 1:
			Shape_selection:;
			printf("Which of the shapes do you want to print:\n");
			printf("1.Tringle\n2.Circle\n3.Exit\n");
			printf("Shape Selection>>");
			scanf("%d",&selection);
			printf("Selected:%d\n",selection);
			switch(selection){
				case 1:
					tringle();
					break;
				case 2:
					circle();
					break;
				case 3:
					printf("OK!!!\a\n");
					break;
				default:
					printf("Select again!!!\a\n");
					goto Shape_selection;
			}
			break;
		case 2:
			face1();
			face1();
			break;
		case 3:
			printf("OK!!!\a\n");
			break;
		default:
			printf("ERROR\a\nWrong input!!!\nTry again\n");
			goto Begin;
			break;
	}
	return selection;
	}
		
int main(){
	int default1=0;
	Main_Menu(default1);
	return 0;
}
