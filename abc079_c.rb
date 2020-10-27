a, b, c, d = gets.chomp.split("").map(&:to_i)

['+', '-'].each do |o1|
  ['+', '-'].each do |o2|
    ['+', '-'].each do |o3|
      if a.method(o1).(b).method(o2).(c).method(o3).(d) == 7
        puts "#{a}#{o1}#{b}#{o2}#{c}#{o3}#{d}=7"
        exit
      end
    end
  end
end
