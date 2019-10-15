/* ------------------------------------------------------------
 * File: Flappy_pong.pde
 * Developed by: Esteban Alvarado 
 * Project: FunSkills- Game
 * version: 0.1
 * last edited by: Esteban Alvarado:: 14.10.2019
 *
 * Description: This is an example source code for screen 
 * handling, 3D rendering and game logic management. 
 * This is expected to be modified to be the balloon game.
 *
 *
 * TEC 2019 | CE3104 - Lenguajes, Compiladores e Interpretes
 * ------------------------------------------------------------*/

// According to its status is the screen that runs
// 0: Initial Screen
// 1: Game Screen
// 2: Game-over Screen
int game_Screen = 0;

int ball_X,ball_Y;
int ball_Size = 40;
int ball_Color = color(214, 36, 63);

void setup(){
  size(500,500,P3D);

  ball_X = width/4;
  ball_Y = height/5;
}


void draw(){
  
  // Game Screen Selector
  if(game_Screen == 0){
    init_Screen();
  } else if(game_Screen == 1){
    game_Screen();
  } else if(game_Screen == 2){
    game_Over_Screen();
  }
  
}

/* ------------------------------------------------------
 *                    SCREEN CONTENTS
 * -----------------------------------------------------*/

void init_Screen(){
  background(0);
  textAlign(CENTER);
  text("Click to Start", height/2, width/2);
}

void game_Screen(){

  background(255);

  draw_Ball();

}

void game_Over_Screen(){

}

/* ------------------------------------------------------
 *                     INPUT EVENTS
 * -----------------------------------------------------*/

/** 
 * @brief - For this example the entry is the mouse. This function must 
 *  be adapted to the kinect inputs
 */
public void mousePressed(){
  if(game_Screen == 0){
    start_Game();
  }
}

/* ------------------------------------------------------
 *                    OTHER FUNCTIONS
 * -----------------------------------------------------*/

void draw_Ball(){

  fill(ball_Color);
  // Function to create "spheres"
  //ellipse(ball_X, ball_Y, ball_Size, ball_Size);
  
  noStroke();
  
  lights();
  translate(ball_X, ball_X, 0);
  lightSpecular(255, 255, 255);
  specular(255,255,255);
  
  sphere(ball_Size);
}

/** 
 * @brief :Sets the necessary variables to start the game
 */ 
void start_Game(){
  game_Screen = 1;
}
