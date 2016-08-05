require 'socket'

class Server
  def initialize(port = 3333)
    @server   = TCPServer.new('127.0.0.1', port)
    @handlers = {}
  end

  def handle(pattern, &block)
    @handlers[pattern] = block
  end

  def run
    while session = @server.accept
      msg   = session.gets
      match = nil

      @handlers.each do |pattern, block|
        if match = msg.match(pattern)
          break session.puts(block.call(match))
        end
      end

      unless match
        session.puts "Server received unknown message: #{msg}"
      end
    end
  end

  def self.run(port = 3333, &block)
    server = Server.new(port)
    server.instance_eval(&block)
    server.run
  end
end

Server.run do
  handle(/hello/i) { "Hello from server at #{Time.now}" }
  handle(/goodbye/i) { "Goodbye from server at #{Time.now}" }
  handle(/name is (\w+)/) { |m| "Nice to meet you #{m[1]}!!" }
end
