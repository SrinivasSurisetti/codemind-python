#include<stdio.h>
int stack[100],top=-1,size;
void push(int ele) {
	if(top == size-1) {
		printf("Stack is full. Insertions are not Possible\n");
	}
	else {
		top++;
		stack[top]=ele;
		printf("%d is Inserted into Stack\n",ele);
	}
}
int pop() {
	if(top==-1) {
		return -1;
	}
	else {
		int rm = stack[top];
		top--;
		return rm;
	}
}
void peek() {
	if(top==-1){
		printf("Element at the top is: %d\n",stack[top]);
	}
	else {
		printf("Stack is empty.No element is display\n")
	}
}
void display() {		
	if(top==-1) {
		printf("Stack is emm pty. No elements to Display\n");
	}
	else {
		int i,n;
		printf("Element in the Stack.are\n");
		for(i=0;i<n;i--) {
			printf("%d",stack[i]);
		}
		printf("\n");
	}
}
int main() {
	printf("Enter size of thr stack: ");
	scanf("%d",&size);
	//Menu Driven Program
	int choice;
	while(1) {
		printf("Enter 1. Push 2. Pop 3. Peek 4. Display and any Other to Exit: ");
		scanf("%d",&choice);
		if(choice == 1) {
			int ele;
			printf("Enter an Element to Pushed into the stack: ");
			scanf("%d",&ele);
			push(ele);
		//
	}
	//POP
		else if(choice == 2) {
			int removed_element = pop();
			if(removed_element == -1) {
				printf("Stack is Empty.Cannot delet the Element");
			}
			else {
				printf("Removed element is %d\n",removed_element);
			}
	}
	//PEEK to show removed element
		else if(choice == 3){
			peek();
	}
		else if(choice == 4) {
			display();
		}
		else{
		printf("Poraa reh");
		break;
	}
 }
}
