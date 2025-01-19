import os
from flask import Flask, request, jsonify
from googlesearch import search

# Define the Flask app
app = Flask(__name__)

# Function to search Google and return results
def check_google_search(query):
    try:
        result = list(search(query, num_results=1))
        return result
    except Exception as e:
        print(f"An error occurred during the search: {e}")
        return []

# Function to run Ruby script
def run_ruby_script():
    ruby_code = '''
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
          @new_direction = 'up' unless @direction == 'down'
        when 's'
          @new_direction = 'down' unless @direction == 'up'
        when 'a'
          @new_direction = 'left' unless @direction == 'right'
        when 'd'
          @new_direction = 'right' unless @direction == 'left'
        end
        @direction = @new_direction
      end

      def move_snake
        head = @snake.first.dup
        case @direction
        when 'up' then head[0] -= 1
        when 'down' then head[0] += 1
        when 'left' then head[1] -= 1
        when 'right' then head[1] += 1
        end
        @snake.unshift(head)
        @snake.pop unless head == @food
      end
      
      def handle_collisions
        if @snake.first[0] < 0 || @snake.first[0] >= Curses.lines || @snake.first[1] < 0 || @snake.first[1] >= Curses.cols
          end_game
        end
        if @snake[1..].include?(@snake.first)
          end_game
        end
        if @snake.first == @food
          place_food
        end
      end
    
      def render
        @window.clear
        @window.setpos(@food[0], @food[1])
        @window.addch('F')
        @snake.each do |segment|
          @window.setpos(segment[0], segment[1])
          @window.addch('O')
        end
        @window.refresh
      end
      
      def end_game
        @window.setpos(Curses.lines / 2.0, Curses.cols / 2.0 - 5)
        @window.addstr("Game Over!")
        @window.refresh
        sleep 2
        Curses.close_screen
        exit
      end
    end
    SnakeGame.new
    '''
    with open("snake_game.rb", "w") as file:
        file.write(ruby_code)
    os.system("ruby snake_game.rb")

@app.route('/search', methods=['POST'])
def search_query():
    data = request.get_json()
    query = data.get('query', '')
    
    if query:
        results = check_google_search(query)
        
        if not results:
            run_ruby_script()
            return jsonify({'message': 'No results found. Ruby script executed.'})
        else:
            return jsonify({'message': f'Results found: {results}'})
    else:
        return jsonify({'message': 'No query provided.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
