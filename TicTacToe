#include<bits/stdc++.h>
using namespace std;
bool draw=false;
char win;
int board[9];
char turn;
int mat[4][4];
int r[5],c[5],d[5];

void initialise()
{
	int i;
	for(i=0;i<9;i++)
	{   //initialised to 0
		board[i]=0;  
	}
}
void update()
{
r[0]=board[0]+board[1]+board[2];
r[1]=board[3]+board[4]+board[5];
r[2]=board[6]+board[7]+board[8];
c[0]=board[0]+board[3]+board[6];
c[1]=board[1]+board[4]+board[7];
c[2]=board[2]+board[5]+board[8];
d[0]=board[0]+board[4]+board[8];
d[1]=board[2]+board[4]+board[6];
}

void print()
{   int c=0;
	int i,j;
	//asssignment
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			mat[i][j]=board[c];
			c++;
		}
	}
	//print
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			cout<<mat[i][j]<<"\t";
		}
		cout<<"\n";
	}
	
	
	return;
}
void check(char turn)
{   //turn of c/h
	int i,j;
	for(i=0;i<3;i++)
	{
		if((r[i]==9)||(c[i]==9)||(d[0]==9)||(d[1]==9))
		{
			win='h';
		}
		else if((r[i]==15)||(c[i]==15)||(d[0]==15)||(d[1]==15))
		{   
			win='c';
		}
	}
}

void humanmove()
{
	int n,i;
	//check for draw before next human move
	for(i=0;i<9;i++)
	{
		if(board[i]==0)
		break;
		else
		continue;
	}
	if(i==9)
	{
		//all slots filled
		draw=true;
		return;
	}
	cout<<"enter the block you want to enter in";
	cin>>n;
	board[n]=3;
	//updates the row,col and diagonal sums
	update();
	turn='c';
	check(turn);
	if(win=='h')
	return; 
}

void blockORmove(char id,int i)
{   
    int j;
	if(id=='r')
	{
		if(i==0)
		{ for(j=0;j<3;j++)
		    { if (board[j]==0)
		        { board[j]=5;
		          update();
		          turn='h';
		          return;
				}
			}
			
		}
		if(i==1)
		{ for(j=3;j<6;j++)
		    { if (board[j]==0)
		        { board[j]=5;
		          update();
		          turn='h';
		          return;
				}
			}
			
		}
		if(i==2)
		{ for(j=6;j<9;j++)
		    { if (board[j]==0)
		        { board[j]=5;
		          update();
		          turn='h';
		          return;
				}
			}
			
		}
	}
	if(id=='c')
	{  
	if(i==0)
		{ for(j=0;j<7;j=j+3)
		    { if (board[j]==0)
		        { board[j]=5;
		          update();
		          turn='h';
		          return;
				}
			}
			
		}
		if(i==1)
		{ for(j=1;j<8;j=j+3)
		    { if (board[j]==0)
		        { board[j]=5;
		          update();
		          turn='h';
		          return;
				}
			}
			
		}
		if(i==2)
		{ for(j=2;j<9;j=j+3)
		    { if (board[j]==0)
		        { board[j]=5;
		          update();
		          turn='h';
		          return;
				}
			}
			
		}
		
	}
	if(id=='d')
	{
		if(i==0)
		{ for(j=0;j<9;j=j+4)
		    { if (board[j]==0)
		        { board[j]=5;
		          update();
		          turn='h';
		          return;
				}
			}
			
		}
		if(i==1)
		{ for(j=2;j<7;j=j+2)
		    { if (board[j]==0)
		        { board[j]=5;
		          update();
		          turn='h';
		          return;
				}
			}
			
		}
	}
	
}

void computermove()
{   char id;   //id represents row,column,diagonal
	int pointer;
	int i,j,k;
	
	  check(turn);
	  if(win=='c')
	  return;
	  
	  //target win
	   for(k=0;k<3;k++)
	   	 	   {
	   if((r[k]==10)||(c[k]==10)||(d[0]==10)||(d[1]==10))
	   	 		    {
	   	 		     	if(r[k]==10)
	                       	{   
							    win='c';
							    id='r';
			                    pointer=k;
			                    blockORmove(id,pointer);
		                     	return;
		                    }
		                    if(c[k]==10)
	                       	{   
							    win='c';
							    id='c';
			                    pointer=k;
			                    blockORmove(id,pointer);
		                     	return;
		                    }
		                if((d[0]==10)||(d[1]==10))
		                    {  
		                        win='c';
							    id='d';
			                    if(d[0]==10)
			                    pointer=0;
			                    else
			                    pointer=1;
		                     	blockORmove(id,pointer);
			                    return;
	                       	}
					}
	   
	     }
	     
	  // blocking
     //if any sum is 6 we need to block
     if((d[0]==6)||(d[1]==6))
     { 
     if (d[0]==6)
	  	  { for(k=0;k<9;k=k+4)
		    { if (board[k]==0)
		        { board[k]=5;
		          update();
		          turn='h';
		          return;
				}
			}
		  }
		  else 
	   	  { for(k=2;k<7;k=k+2)
		    { if (board[k]==0)
		        { board[k]=5;
		          update();
		          turn='h';
		          return;
				}
			}
	      }
    //end of if
	 }
     for(i=0;i<3;i++)
     {
	  if((r[i]==6)||(c[i]==6))
	    {  
		 	if(r[i]==6)
	    	{ id='r';
			pointer=i;
			blockORmove(id,pointer);
			break;
		    }
		   else if(c[i]==6)
		   {id='c';
			pointer=i;
			blockORmove(id,pointer);
			break;
		   }   
	   }
      }
     
	 if(i==3) 
	 { 
	   
	  	//target diagoals
	  	if((d[0]==5)||(d[1]==5))
	  	{
	  	  if (d[0]==5)
	  	  { for(k=0;k<9;k=k+4)
		    { if (board[k]==0)
		        { board[k]=5;
		          update();
		          turn='h';
		          return;
				}
			}
		  }
		  else
	   	  { for(k=2;k<7;k=k+2)
		    { if (board[k]==0)
		        { board[k]=5;
		          update();
		          turn='h';
		          return;
				}
			}
	      }
	   } //place your move
	else
	      {  
	   	 	for(k=0;k<3;k++)
	   	 	   {  
	   	 		   if((r[k]==5)||(c[k]==5)||(r[k]==3)||(c[k]==3))
	   	 		    {
	   	 		     	if((r[k]==5)||(r[k]==3))
	                       	{   
							   
							    id='r';
			                    pointer=k;
			                    blockORmove(id,pointer);
		                     	break;
		                    }
		                if((c[k]==5)||(c[k]==3))
		                    {  
							    id='c';
			                    pointer=k;
		                     	blockORmove(id,pointer);
			                    break;
	                       	}
					}
					
		    	}
		    	if(k==3)
		    	{  
		    		draw=true;
		    		return;
				}
	       }
	  			
		}
	 

return;
	
}

int main()
{   cout<<"board positions are as follow\n";
    cout<<"0  1  2\n";
    cout<<"3  4  5\n";
    cout<<"6  7  8\n";

	initialise();
	cout<<"enter who starts the game h-human/c-computer\n";
	cin>>turn;
	
	if(turn=='c')
	{   
	    cout<<"After computer move\n";
		board[4]=5;
		update();
		print();
		turn='h';
	}
	else
	{
	  humanmove();
	  cout<<"After humans move\n";
	  print();
    }
	while(true)
	{  
	
	if((draw==true)||(win=='c')||(win=='h'))
	  break;
	else
	{
		if(turn=='c')
	{   
	    computermove();
	    
	    cout<<"After computers move\n";
	    print();
	}
	else
	{
	
	  humanmove();
	  cout<<"After humans move\n";
	  print();
	}
   }
  }
	
	//declare the winner
	if(win=='c')
	{
		cout<<"computer is the winner\n";
		
	}
	else if(win=='h')
	{
		cout<<"human is the winner\n";
	}
	else
	{
		cout<<"match draw\n";
	}
	
return true;
	
}
