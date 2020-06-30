const HEIGHT = 16;
const WIDTH = 16;
const PIXEL = 4;
const FRAME_RATE = 6000;

var lastx = 0, lasty = 0;

//var xor_values = [49, 17, 58, 13, 1, 22, 39, 24, 26, 100, 2, 2, 2, 75, 44, 102, 66, 23, 11, 2, 50, 54, 92, 106, 48, 1, 2, 21, 38, 47,63,60,70,80,22,0,64,87,59,61,27,38,43,28,91,108,51,95,7,70,28,11,1,25]
//1011110110101100100101101001101110011010100011001010101001101010001011101100011011110010111101101010111000111011110110101100100101101001101110011010100011001010101001101010001011101100011011110010111101101010111000111011110110101100100101101001101110011010100011001010101001101010001011101100011011110010111101101010111000111011110110101100100101101001101110011010100011001010101001101010001011101100011011110010111101101010111000111011110110101100100101101001101110011010100011001010101001101 
var xor_values = [49, 17, 58, 13, 1, 22, 39, 24, 26, 100, 2, 2, 2, 75, 44, 102, 66, 23, 11, 2, 50, 54, 92, 106, 48, 1, 2, 21, 38, 47, 63, 60, 70, 80, 22, 0, 64, 87, 59, 61, 27, 38, 43, 28, 91, 108, 51, 95, 7, 70, 28, 11, 1, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, 1, 48, 0, 0, 0, 0, 0, 19, 0, 0, 0]
var buff = "";
var buff2 = "";
var buffTot = "";
var buffFin = "";
var counter = 0;
var i = 0;
var i1 = 0;
var x_snake = 0;
var y_snake = 0;
var start = true;
var start2 = true;
var start3 = true;
var destra = true;
var up = true;
var down = false;
function update_buffer(x, y, c) {
	buffTot += c;
	
  if (x !== lastx || y !== lasty) {
  		//console.log("Got fruit!", counter);
  		counter += 1;
	    lastx = x;
	    lasty = y;
		buff += c;
		console.log(buff)
		if (c == "0")
			buff2 += "1";
		else
			buff2 += "0";
		if (counter % 8 == 0)
			buff += "  "
  }
}



var get_ctx = () => document.getElementById('canvas').getContext('2d');
var g_key;



function get_random(min, max) {
  var num = Math.floor(Math.random() * (max - min)) + min;
  return num;
}

function draw_body(x, y) {
	x_snake = x;
	y_snake = y;
  var ctx = get_ctx();
  ctx.fillStyle = '#246417';
  ctx.fillRect(x, y, HEIGHT, WIDTH);
}

function remove_body(x, y) {
  var ctx = get_ctx();
  ctx.fillStyle = '#9dff00';
  ctx.fillRect(x, y, HEIGHT, WIDTH);
}

function draw_fruit_1(x, y) {
  /**  *  *
        **
        **
       *  *   2 */
  update_buffer(x, y, "1")
  var ctx = get_ctx();
  ctx.fillStyle = '#246417';
  ctx.fillRect(x, y, PIXEL, PIXEL);
  ctx.fillRect(x + (3 * PIXEL), y, PIXEL, PIXEL);
  ctx.fillRect(x + (1 * PIXEL), y + (1 * PIXEL), (2 * PIXEL), (2 * PIXEL));
  ctx.fillRect(x, y + (3 * PIXEL), PIXEL, PIXEL);
  ctx.fillRect(x + (3 * PIXEL), y + (3 * PIXEL), PIXEL, PIXEL);
}

function draw_fruit_2(x, y) {
  /**    **
         **
        *  *
        *  *   3 */
  	
  update_buffer(x, y, "0");
  var ctx = get_ctx();
  ctx.fillStyle = '#246417';
  ctx.fillRect(x + PIXEL, y, (2 * PIXEL), (2 * PIXEL));
  ctx.fillRect(x, y + (2 * PIXEL), PIXEL, (2 * PIXEL));
  ctx.fillRect(x + (3 * PIXEL), y + (2 * PIXEL), PIXEL, (2 * PIXEL));
}

function draw_at(x, y, type) {
  switch (type) {
    case 0:
      draw_body(x, y)
      break
    case 1:
      remove_body(x, y)
      break
    case 2:
      draw_fruit_1(x, y)
      break
    case 3:
      draw_fruit_2(x, y)
      break
  }
}

function input_store(key, state) {
  g_key = key;
}

function get_input() {

	if (start) {
		if (x_snake == 0 && y_snake == 496) {
			start = false;
			return 3;
		}
		if (x_snake == 0) {
			return 5;
		}
		if (y_snake == 480) {
			return 12;
		}
		return 5;
	}
	if (start2) {

		if (x_snake == 0 && y_snake == 496 && down) {
			down = false;
			destra = true;
			up = true;
			return 3;
		}
		if ((x_snake == 0 && y_snake == 0) || down) {
			down = true;
			return 5;
		}
		if (x_snake == 16 && y_snake != 496 && y_snake != 0 &&  up) {
			up = false;
			if (destra)
				destra = false;
			else
				destra = true;
			return 10;
		}

		if (x_snake == 560 && up) {
			up = false;
			if (destra)
				destra = false;
			else
				destra = true;
			return 10;
		}

		up = true;
		if (destra)
			return 3;
		else
			return 12;
	}
  switch (g_key) {
    case "ArrowUp":
      return 10;
    case "ArrowDown":
      return 5;
    case "ArrowRight":
      return 3;
    case "ArrowLeft":
      return 12;
    case " ":
      return 15;
    case "r":
    case "R":
      g_key = ""
      return 1;

    default:
      return 0
  }
}

function draw_clear_board() {
  var ctx = get_ctx();
  ctx.fillStyle = '#9dff00';
  ctx.fillRect(0, 0, canvas.width, canvas.height)
}

function draw_game_lost() {
  var ctx = get_ctx();
  ctx.fillStyle = '#9dff00';
  ctx.fillRect(0, 0, canvas.width, canvas.height)

  ctx.font = "bold 30px Courier New";
  ctx.fillStyle = '#246417';
  ctx.textAlign = "center";
  ctx.fillText("Game Over!", canvas.width / 2, canvas.height / 2);

  ctx.font = "bold 20px Courier New";
  ctx.fillText("(R)eplay", canvas.width / 2 - 2, canvas.height / 2 + 40);

  ctx.lineWidth = 2;
  ctx.strokeStyle = "#246417";
  ctx.strokeRect(canvas.width / 2 - 104, canvas.height / 2 - 30, 204, 40)
}

imports = {
  draw_at: draw_at,
  get_input: get_input,
  console_log: arg => console.log(arg),
  stackSave: () => 0,
  stackRestore: () => 0,
  get_random: get_random,
  draw_game_lost: draw_game_lost,
  draw_clear_board: draw_clear_board


}

if (typeof mergeInto !== 'undefined') mergeInto(LibraryManager.library, imports);

function game_start(game_iter) {
  interval = setInterval(game_iter, 1000 / FRAME_RATE);
}

function game_stop() {
  clearInterval(interval);
}