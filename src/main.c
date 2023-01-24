
#include <ncurses.h>
#include <math.h>

int main( int argc, char* argv ) {
   int max_x = 0,
      max_y = 0,
      i = 0;
   float r = 0;

   initscr();

   getmaxyx( stdscr, max_y, max_x );

   mvaddch( max_y / 2, max_x / 2, 'x' );

   for( r = 0 ; 3 > r ; r += 0.1 ) {
      mvaddch(
         (max_y / 2) + (sinf( r ) * 5),
         (max_x / 2) + (cosf( r ) * 5), '+' );
   }

   refresh();
   getch();
   endwin();

   return 0;
}

