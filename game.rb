require 'curses'

class SnakeGame
  def initialize
    Curses.init_screen
    Curses.curs_set(0) # Hide the cursor
    Curses.timeout = 100 # Set delay for getch to 100ms
    @window = Curses.stdscr

    @snake = [[4, 4], [4, 3], [4, 2]]
    @direction = 'right'
    @new_direction = 'right'

    # Place the first food
    place_food

    play_game
  end

  def place_food
    begin
      @food = [rand(Curses.lines), rand(Curses.cols)]
    end until @snake.include?(@food)
  end

  def play_game
    loop do
      handle_input
      move_snake
      handle_collisions
      render

      sleep 0.1
    end
  end

  def handle_input
    case @window.getch
    when 'w'
      @new_direction = 'up'    unless @direction == 'down'
    when 's'
      @new_direction = 'down'  unless @direction == 'up'
    when 'a'
      @new_direction = 'left'  unless @direction == 'right'
    when 'd'
      @new_direction = 'right' unless @direction == 'left'
    end
    @direction = @new_direction
  end

  def move_snake
    head = @snake.first.dup

    case @direction
    when 'up'    then head[0] -= 1
    when 'down'  then head[0] += 1
    when 'left'  then head[1] -= 1
    when 'right' then head[1] += 1
    end

    @snake.unshift(head)
    @snake.pop unless head == @food
  end

  def handle_collisions
    # Check collisions with walls
    if @snake.first[0] < 0 || @snake.first[0] >= Curses.lines ||
       @snake.first[1] < 0 || @snake.first[1] >= Curses.cols
      end_game
    end

    # Check collisions with itself
    if @snake[1..].include?(@snake.first)
      end_game
    end

    # Check if food is eaten
    if @snake.first == @food
      place_food
    end
  end

  def render
    @window.clear
    
    # Draw the food
    @window.setpos(@food[0], @food[1])
    @window.addch('F')

    # Draw the snake
    @snake.each do |segment|
      @window.setpos(segment[0], segment[1])
      @window.addch('O')
    end

    @window.refresh
  end

  def end_game
    @window.setpos(Curses.lines / 2, Curses.cols / 2 - 5)
    @window.addstr("Game Over!")
    @window.refresh
    sleep 2
    Curses.close_screen
    exit
  end
end

SnakeGame.new
