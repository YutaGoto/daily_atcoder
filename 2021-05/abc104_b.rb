s = gets.chomp

if s[0] != 'A'
  puts 'WA'
  exit
end

if s[1] == s[1].upcase
  puts 'WA'
  exit
end

if s[-1] == s[-1].upcase
  puts 'WA'
  exit
end

if s[2..-2].count('C') == 1
  s[2..-2].each_char do |e|
    if e != 'C' && e == e.upcase
      puts 'WA'
      exit
    end
  end
  puts 'AC'
else
  puts 'WA'
  exit
end
