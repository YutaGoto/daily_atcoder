n = gets.chomp.to_i
s = gets.chomp

if n.odd?
  puts "No"
elsif s[0..(n/2-1)] == s[(n/2)..(n-1)]
  puts "Yes"
else
  puts "No"
end
