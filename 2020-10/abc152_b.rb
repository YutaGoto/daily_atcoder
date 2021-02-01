a, b = gets.chomp.split(" ").map(&:to_i)

bb = b.to_s * a
aa = a.to_s * b

if aa <= bb
    puts aa
else 
    puts bb
end
